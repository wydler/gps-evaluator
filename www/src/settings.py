#!/usr/bin/python

import serial

FPGA_PORT = '/dev/ttyUSB1'
FPGA_BAUD_RATE = 9600
FPGA_PARITY_MODE = serial.PARITY_EVEN

GPS_PORT = '/dev/ttyUSB0'
GPS_BAUD_RATE = 9600
GPS_PARITY_MODE = serial.PARITY_NONE
