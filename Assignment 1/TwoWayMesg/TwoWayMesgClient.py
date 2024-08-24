import sys
import socket

if len(sys.argv) != 4:
    print("Usage: python TwoWayMesgClient.py localhost portNumber clientName")
    sys.exit(1)

# Extract server address, port number, and client name from the arguments
server_address = sys.argv[1]
port = int(sys.argv[2])
client_name = sys.argv[3]

# Create socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((server_address, port))

# Wrap the socket with a file object for easier reading/writing
clientSockFile = clientSock.makefile('rwb')

print(f"Connected to server at {clientSock.getsockname()}")

while True:
    # Get user input
    message = input('Enter your message: ')

    # Send the message to the server with the client name
    clientSockFile.write(( message + '\n').encode())
    clientSockFile.flush()  # Ensure the message is sent immediately

    # Wait for a response from the server
    response = clientSockFile.readline().decode()

    # Display the server's response
    print(f"Server: {response}", end='')
