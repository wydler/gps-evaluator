import socket
import string
import time

address = ('', 8003)
mySocket = socket.socket()

mySocket.connect(address)
print("Connected successfully!")
while True:
	var = raw_input("Enter something: ")
	mySocket.send(var.encode())

	if var.strip() == 'bye':
		break