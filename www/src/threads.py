#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import SocketServer
import serial
import multiprocessing
import array
import struct
import json
import time
import random
import settings
import sys

class FPGAThread(Thread):
	def __init__(self, queue, debug):
		# call base class constructor.
		Thread.__init__(self)
		# set as daemon thread.
		self.daemon = True
		# set message queue.
		self.queue = queue
		# set debug flag.
		self.debug = debug

		if not self.debug:
			# set serial interface.
			self.serial = serial.Serial(settings.FPGA_PORT, settings.FPGA_BAUD_RATE, timeout=1, parity=settings.FPGA_PARITY_MODE)

	def run(self):
		print "FPGA Thread running..."

		# create empty dictionary.
		data = {}

		# endless loop.
		while True:
			if not self.debug:
				# read 8 bytes (4 bytes for each counter value) from serial interface.
				bytes = self.serial.read(8)
			else:
				# dummy byte array for debugging
				bytes = array.array('B', '\xa4\xf0\xfa\x02\xf8\x96\x98\x00')

			# check data-length.
			if (len(bytes) == 8):
				# split byte array into value.
				cnts = struct.unpack('<II', bytes)
				# save values to data dictionary.
				data['cnt1'] = cnts[0]
				data['cnt2'] = cnts[1]

				print data

				# create random values for debugging.
				if self.debug:
					data['cnt1'] += random.randrange(-1000,3000)
					data['cnt2'] += random.randrange(-1000,3000)
			
			# put event messages to queue.
			self.queue.put('event: clk\ndata: %s\n\n' % json.JSONEncoder().encode(data))
			
			# pause 1 second, only for debugging
			if self.debug:
				time.sleep(1)

class GPSThread(Thread):
	def __init__(self, queue, debug):
		# call base class constructor.
		Thread.__init__(self)
		# set as daemon thread.
		self.daemon = True
		# set message queue.
		self.queue = queue
		# set debug flag.
		self.debug = debug

		if not self.debug:
			# set serial interface.
			self.serial = serial.Serial(settings.GPS_PORT, settings.GPS_BAUD_RATE, timeout=1, parity=settings.GPS_PARITY_MODE)

	def run(self):
		print "GPS Thread running..."

		# create empty dictionary.
		data = {}
		sentence = ''

		# endless loop.
		while True:
			if not self.debug:
				# read one character from serial interface.
				c = self.serial.read()
				
			# if debugging is enabled or eol received.
			if self.debug or c == '\n':
				if self.debug:
					# dummy sentence for debugging.
					sentence = '$GPGGA,191410,4759.2723,N,00765.5896,E,1,04,4.4,351.5,M,48.0,M,,*45'
				
				# split sentence to array.
				# ignore the first and the last 4 characters.
				s = sentence[1:-4].split(',')

				# switch sentence type.
				if s[0] == 'GPGGA':
					data["time"] = s[1][0:2]+":"+s[1][2:4]+":"+s[1][4:6]
					data["latitude"] = [self.dms2deg(s[2]), s[3]]
					data["longitude"] = [self.dms2deg(s[4]), s[5]]
					data["altitude"] = [s[9], s[10]]
					data["quality"] = s[6]
					data["satellites"] = s[7]
				elif s[0] == 'GPGSA':
					data["fix"] = s[2]
					data["pdop"] = s[15]
					data["hdop"] = s[16]
					data["vdop"] = s[17]
				elif s[0] == 'GPRMC':
					data["date"] = s[9][0:2]+"."+s[9][2:4]+".20"+s[9][4:6]

				# put event messages to queue.
				self.queue.put('event: gps\ndata: %s\n\n' % json.JSONEncoder().encode(data))

				# reset sentence.
				sentence = ''
			else:
				# add charater to sentence.
				sentence += c
				
			if self.debug:
				time.sleep(1)

	# convert gps position.
	def dms2deg(self, dms):
		try:
			dms = dms.split('.')
			d = float(dms[0][:-2])
			m = float(dms[0][-2:])/60
			s = float(dms[1])*60/10000/3600

			return round(d + m + s, 6)
		except Exception:
			return 0

class SSEThread(Thread):
	class RequestHandler(BaseHTTPRequestHandler):
		def do_GET(self):
			self.send_response(200)
			self.send_header('content-type', 'text/event-stream')
			self.end_headers()
			while True:
				try:
					data = self.server.queue.get()
					self.wfile.write(data)
				except Exception as ex:
					print ex
					self.wfile.flush()

	def __init__(self, queue):
		# call base class constructor.
		Thread.__init__(self)
		# set as daemon thread.
		self.daemon = True
		# create a http-server with request handler.
		self.server = HTTPServer(('', 8001), self.RequestHandler)
		# set message queue as server context.
		self.server.queue = queue

	def run(self):
		print "SSE Server running..."
		# start endless loop.
		self.server.serve_forever()

class TCPThread(Thread):
	class RequestHandler(SocketServer.BaseRequestHandler):
		def setup(self):
			print '%s:%s connected -' % self.client_address

		def handle(self):
			#self.request.settimeout(1)
			while True:
				data = self.request.recv(1024)
				if not data:
					break
				if (data.strip() != 'bye'):
					self.server.queue.put('event: ext\ndata: %s\n\n' % (data))
				else:
					break

		def finish(self):
			print '%s:%s disconnected -' % self.client_address

	def __init__(self, queue):
		# call base class constructor.
		Thread.__init__(self)
		# set as daemon thread.
		self.daemon = True
		# create a http-server with request handler.
		self.server = SocketServer.ThreadingTCPServer(('', 8003), self.RequestHandler)
		# set flag, that all threads started as daemon.
		self.server.daemon_threads = True
		# set message queue as server context.
		self.server.queue = queue

	def run(self):
		print "TCP Server running..."
		# endless service loop.
		self.server.serve_forever()
