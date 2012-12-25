#!/usr/bin/python

import multiprocessing
import array
import struct
import json
import time
import random
import settings

class FPGA(multiprocessing.Process):
	def __init__(self, result_queue):
		# base class initialization
		multiprocessing.Process.__init__(self)

		# job management stuff
		self.result_queue = result_queue
		self.kill_received = False
		
		# open serial port
		#self.serial = serial.Serial(settings.FPGA_PORT, settings.FPGA_BAUD_RATE, timeout=1, parity=settings.FPGA_PARITY_MODE)

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
			
class GPS(multiprocessing.Process):
	def __init__(self, result_queue):
		# base class initialization
		multiprocessing.Process.__init__(self)

		# job management stuff
		self.result_queue = result_queue
		self.kill_received = False
		
		# open serial port
		#self.serial = serial.Serial(settings.GPS_PORT, settings.GPS_BAUD_RATE, timeout=1, parity=settings.GPS_PARITY_MODE)

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
