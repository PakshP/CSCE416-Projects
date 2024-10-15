
from socket import *
from sys import argv
from select import select

# List to keep track of connected clients
clients = []

# Function to broadcast a message to all clients except the sender
def broadcast(message, sender_sock):
    for client in clients:
        if client != sender_sock:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

# Server needs the port number to listen on
if len(argv) != 2:
    print('usage:', argv[0], '<port>')
    exit()

serverPort = int(argv[1])

# Create the server socket
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', serverPort))
serverSock.listen()

print('Server is listening on port', serverPort)

while True:
    # Use select to monitor multiple sockets
    read_sockets, _, _ = select([serverSock] + clients, [], [])

    for sock in read_sockets:
        if sock == serverSock:
            # New client connection
            clientSock, clientAddr = serverSock.accept()
            clients.append(clientSock)
            print(f"Client {clientAddr} connected.")
        else:
            # Existing client sending a message
            try:
                message = sock.recv(1024).decode()
                if message:
                    print(f"Received message: {message}")
                    broadcast(message, sock)
                else:
                    # Client disconnected
                    print(f"Client {sock.getpeername()} disconnected.")
                    clients.remove(sock)
                    sock.close()
            except:
                continue
