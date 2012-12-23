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

				self.wfile.write('event: gps\nid: 20\ndata: %s\n\n' % data)
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

try:
	#clk_data = serial.Serial(FPGA_PORT, FPGA_BAUD_RATE, timeout=1, parity=FPGA_PARITY_MODE)

	serveraddr = ('', 8002)
	srvr = HTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
except Exception as ex:
	print ex
