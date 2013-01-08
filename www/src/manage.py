#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import socket
import threading
import multiprocessing
import argparse
import settings
import threads
import time
import traceback

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("runserver")
	parser.add_argument("--debug", action="store_true")
	args = parser.parse_args()

	if args.runserver:
		runserver(args.debug)
		
def runserver(debug):
	if debug:
		print "Debugging mode is enabled."
		
	try:
		# create message queue.
		queue = multiprocessing.Queue()

		# create fpga reader queue.
		fpga=threads.FPGAThread(queue, debug)
		fpga.start()

		gps=threads.GPSThread(queue, debug)
		gps.start()

		sse=threads.SSEThread(queue)
		sse.start()

		tcp=threads.TCPThread(queue)
		tcp.start()

		print 'Starting server, use <Ctrl-C> to stop.'
		while True:
			time.sleep(100)
	except (KeyboardInterrupt, SystemExit):
		tcp.server.shutdown()
		print '\nReceived keyboard interrupt, quitting threads.'
	except Exception as ex:
		traceback.print_exc() 
		#print ex

if __name__ == "__main__":
	main()