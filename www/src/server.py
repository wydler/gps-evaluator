#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import serial
import struct
import multiprocessing
import Queue as queue
import random
import time
import array
import json

FPGA_PORT = '/dev/ttyS0'
FPGA_BAUD_RATE = 9600
FPGA_PARITY_MODE = serial.PARITY_EVEN

GPS_PORT = '/dev/ttyUSB0'
GPS_BAUD_RATE = 9600
GPS_PARITY_MODE = serial.PARITY_NONE

class FPGAWorker(multiprocessing.Process):
	def __init__(self, result_queue):
		# base class initialization
		multiprocessing.Process.__init__(self)

		# job management stuff
		self.result_queue = result_queue
		self.kill_received = False
		
		# open serial port
		#self.serial = serial.Serial(FPGA_PORT, FPGA_BAUD_RATE, timeout=1, parity=FPGA_PARITY_MODE)

	def run(self):
		# endless loop while process not killed
		data = {}
		while not self.kill_received:
			# read serial data
			#bytes = self.serial.read(8)
			
			# dummy byte array for debugging
			bytes = array.array('B', '\xa4\xf0\xfa\x02\xf8\x96\x98\x00')

			# check data-length
			if (len(bytes) == 8):
				# split data bytes
				cnts = struct.unpack('<II', bytes)
				#print "Counter 1: " + str(cnts[0])
				data['cnt1'] = cnts[0] + random.randrange(-1000,3000)
				#print "Counter 2: " + str(cnts[1])
				data['cnt2'] = cnts[1] + random.randrange(-1000,3000)
			
			# put event messages to queue.
			self.result_queue.put('event: clk\ndata: %s\n\n' % json.JSONEncoder().encode(data))
			
			# pause 1 second, only for debugging
			time.sleep(1)
			
class GPSWorker(multiprocessing.Process):
	def __init__(self, result_queue):
		# base class initialization
		multiprocessing.Process.__init__(self)

		# job management stuff
		self.result_queue = result_queue
		self.kill_received = False
		
		# open serial port
		#self.serial = serial.Serial(GPS_PORT, GPS_BAUD_RATE, timeout=1, parity=GPS_PARITY_MODE)

	def run(self):
		# endless loop while process not killed
		data = {}
		while not self.kill_received:
			#c = self.serial.read()
			if True or c == '\n':
				sentence = '$GPGGA,191410,4735.5634,N,00739.3538,E,1,04,4.4,351.5,M,48.0,M,,*45'
				s = sentence[1:-4].split(',')
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

				self.result_queue.put('event: gps\ndata: %s\n\n' % json.JSONEncoder().encode(data))
				sentence = ''
			else:
				sentence += c
				
			# pause 1 second, only for debugging
			time.sleep(1)
				
	def dms2deg(self, dms):
		if dms != '':
			dms = dms.split('.')
			d = float(dms[0][:-2])
			m = float(dms[0][-2:])/60
			s = float(dms[1])*60/10000/3600

			return round(d + m + s, 6)
		else:
			return 0

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/event-stream')
		self.end_headers()
		while True:
			try:
				#self.wfile.write('event: clk\nid: 1\ndata: {0}\ndata:\n\n'.format(time.time()))
				self.wfile.write(result_queue.get())
			except Exception as ex:
				print ex
				self.wfile.flush()

try:
	#clk_data = serial.Serial(FPGA_PORT, FPGA_BAUD_RATE, timeout=1, parity=FPGA_PARITY_MODE)
	#gps_data = serial.Serial(GPS_PORT, GPS_BAUD_RATE, timeout=1, parity=GPS_PARITY_MODE)

	# create a queue to pass to workers to store the results
	result_queue = multiprocessing.Queue()

	# start fpga worker
	fpga_worker = FPGAWorker(result_queue)
	fpga_worker.start()
	
	# start gps worker
	gps_worker = GPSWorker(result_queue)
	gps_worker.start()
	
	serveraddr = ('', 8001)
	srvr = HTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
except Exception as ex:
	print ex
