# Implementation of a two-way async message server in python

# Import socket related methods
from socket import *

# Import argv related methods
from sys import *

# Import select method
from select import *

# Import thread API
import threading
from threading import Thread

# Server needs the port number to listen on
if len(argv) != 2:
    print('usage:', argv[0], '<port>')
    exit()

# Get the port on which server should listen */
serverPort = int(argv[1])

# Create the server socket
serverSock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the given port
serverSock.bind(('', serverPort))

# Set the server for listening */
serverSock.listen()

# Wait to receive a connection request
print('Waiting for a client ...')
clientSock, clientAddr = serverSock.accept()
print('Connected to a client at', clientAddr)

# No other clients, close the server socket
serverSock.close()

# Make a file stream out of client socket
clientSockFile = clientSock.makefile()

def send_message(clientSock, clientSockFile):
	try:
		while True:
			# Read a line form the keyboard
			line = stdin.readline()
			# If EOF ==> sever wants to close connection
			if not line:
			    print('*** Server closing connection')
			    break
			
			# Send the line to server
			clientSock.send(line.encode())
		
		# Close the connection
		clientSockFile.close()
		clientSock.close()

	except:
		print('*** Server closing connection')

def receive_message(clientSock, clientSockFile):
	try:
		while True:
			# Read a message from the client
			line = clientSockFile.readline()
			
			# If EOF ==> client closed the connection
			if not line:
			    print('*** Client closed connection')
			    break
			
			# Display the line
			print('Client:', line, end='')

		# Close the connection
		clientSockFile.close()
		clientSock.close()

	except:
		print('*** Client closed connection')

Thread(target=send_message, args=(clientSock, clientSockFile, )).start()  
Thread(target=receive_message, args=(clientSock, clientSockFile,)).start()

