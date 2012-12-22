#!/usr/bin/python

import serial
import json
import time

def dms2deg(dms):
	if dms != '':
		dms = dms.split('.')
		d = float(dms[0][:-2])
		m = float(dms[0][-2:])/60
		s = float(dms[1])*60/10000/3600

		return round(d + m + s, 6)
	else:
		return 0

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print ser

sentence = ''
data = {}

while 1:
	c = ser.read()
	#c = ser.read(1)
	if c == '\n':
		#print sentence
		s = sentence[1:-4].split(',')
		if s[0] == 'GPGGA':
			print sentence
			data["time"] = s[1][0:2]+":"+s[1][2:4]+":"+s[1][4:6]
			data["latitude"] = [dms2deg(s[2]), s[3]]
			data["longitude"] = [dms2deg(s[4]), s[5]]
			data["altitude"] = [s[9], s[10]]
			data["quality"] = s[6]
			data["satellites"] = s[7]
			#print data
		elif s[0] == 'GPGSA':
			data["fix"] = s[2]
			data["pdop"] = s[15]
			data["hdop"] = s[16]
			data["vdop"] = s[17]
		elif s[0] == 'GPRMC':
			data["date"] = s[9][0:2]+"."+s[9][2:4]+".20"+s[9][4:6]
		elif s[0] == 'GPVTG':
			f = open('data.json', 'w+')
			f.write(json.JSONEncoder().encode(data))
			f.close()

		sentence = ''
	else:
		sentence += c