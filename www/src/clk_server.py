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

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/event-stream')
		self.end_headers()
		
		data = {}
		while True:
			#bytes = clk_data.read(8)
			
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
			self.wfile.write('event: clk\ndata: %s\n\n' % data)
			
			# pause 1 second, only for debugging
			time.sleep(1)

try:
	#clk_data = serial.Serial(FPGA_PORT, FPGA_BAUD_RATE, timeout=1, parity=FPGA_PARITY_MODE)

	serveraddr = ('', 8001)
	srvr = HTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
except Exception as ex:
	print ex
