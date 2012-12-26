#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

import multiprocessing
import argparse
import settings
import workers

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/event-stream')
		self.end_headers()
		while True:
			try:
				#self.wfile.write('event: clk\nid: 1\ndata: {0}\ndata:\n\n'.format(time.time()))
				global result_queue
				self.wfile.write(result_queue.get())
			except Exception as ex:
				print ex
				self.wfile.flush()

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
		# create a queue to pass to workers to store the results
		global result_queue
		result_queue = multiprocessing.Queue()

		# start fpga worker
		fpga_worker = workers.FPGA(result_queue, debug)
		fpga_worker.start()
	
		# start gps worker
		gps_worker = workers.GPS(result_queue, debug)
		gps_worker.start()
	
		serveraddr = ('', 8001)
		srvr = HTTPServer(serveraddr, RequestHandler)
		srvr.serve_forever()
	except KeyboardInterrupt:
		fpga_worker.terminate()
		gps_worker.terminate()
		pass
	except Exception as ex:
		print ex

if __name__ == "__main__":
	main()
