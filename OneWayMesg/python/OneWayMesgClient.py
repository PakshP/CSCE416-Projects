# Implementation of the one way message client in python

# Import socket related methods
from socket import *

# Import argv related methods
from sys import *


# Client needs server's contact information
if len(argv) != 3:
    print("usage:", argv[0], "<server name> <server port>")
    exit()

# Get server's whereabouts
serverName = argv[1]
serverPort = int(argv[2])

# Create a socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to the server
sock.connect((serverName, serverPort))
print(f"Connected to server at ('{serverName}', '{serverPort}')");

# Make a file stream out of socket
sockFile = sock.makefile(mode='w')

# Keep reading lines and send to server
for line in stdin:
    # Send the line to server
    sock.send(line.encode())

# done
print("Closing connection")
sock.close()
