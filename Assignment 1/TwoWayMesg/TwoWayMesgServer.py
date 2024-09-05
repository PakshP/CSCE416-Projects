# Paksh Patel

import sys
import socket

if len(sys.argv) != 3:
    print("Usage: python TwoWayMesgServer.py portNumber serverName")
    sys.exit(1)

# Extract port number and server name from the arguments
port = int(sys.argv[1])
server_name = sys.argv[2]

# Create socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print("Waiting for a client ...")
clientSock, clientAddress = serverSock.accept()
print(f"Connected to a client at {clientAddress}")

# Wrap the socket with a file object for easier reading/writing
clientSockFile = clientSock.makefile('rwb')

while True:
    # Read a message from the client
    message = clientSockFile.readline().decode()

    # If no message ==> client closed the connection
    if not message:
        print('Client closed connection')
        clientSockFile.close()
        clientSock.close()
        break

    # Display the client's message
    print(f"{message}", end='')

    # Get a response from the server user
    response = input('Enter your message: ')

    # Send the response to the client with the server name
    clientSockFile.write((server_name + ": " +  response + '\n').encode())
    # Make sure the message is sent immediately
    clientSockFile.flush()  
