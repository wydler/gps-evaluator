import serial
import codecs

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

char = ''
satz = ''

while 1:
	c = ser.read()
	if char == '\n':
		print satz[:-1]
		if satz.startswith('GPGGA'):
			sp = satz.split(',')
			#print sp

			lat = sp[2].split('.')
			lat_d = lat[0][:-2]
			lat_m = lat[0][-2:]
			lat_s = lat[1]
			lat_g = float(lat_d) + float(lat_m)/60 + ((float(lat_s)/10000)*60)/3600

			lng = sp[4].split('.')
			lng_d = lng[0][:-2]
			lng_m = lng[0][-2:]
			lng_s = lng[1]
			lng_g = float(lng_d) + float(lng_m)/60 + ((float(lng_s)/10000)*60)/3600

			sa = '{"latitude": ' + str(lat_g) + ', "longitude": ' + str(lng_g) + '}'
			#print sa

			f = open('data.json', 'w+')
			f.write(sa)
			f.close()

		satz = ''
		char = ''
	else:
		satz += c
		char = c