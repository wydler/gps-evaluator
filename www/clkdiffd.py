#!/usr/bin/python

import serial
import struct
import array
import time

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1, parity=serial.PARITY_EVEN)
bytes = None

while 1:
	bytes = ser.read(8)
#	print bytes
	cnt = 8
	#bytes = array.array('B', '\x00\x0f\x42\x40\x00\x00\x00\x01')
	
	if (len(bytes) == 8):
		cnts = struct.unpack('<II', bytes)
		print "Counter 1: " + str(cnts[0])
		print "Counter 2: " + str(cnts[1])
	time.sleep(0.5)
