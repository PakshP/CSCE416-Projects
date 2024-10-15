
from socket import *
from sys import stdin, argv
from threading import Thread

# Client needs server's contact information
if len(argv) != 4:
    print("usage:", argv[0], "<server name> <server port> <username>")
    exit()

serverName = argv[1]
serverPort = int(argv[2])
username = argv[3]

# Create a socket and connect to the server
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverName, serverPort))
print(f"Connected to server at ('{serverName}', '{serverPort}')")

# Send username to the server
sock.send(f"{username} has joined the chat.".encode())

# Function to handle sending messages
def send_message():
    while True:
        message = stdin.readline().strip()
        if message:
            full_message = f"{username}: {message}"
            sock.send(full_message.encode())

# Function to handle receiving messages
def receive_message():
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(message)
            else:
                print("Connection to server lost.")
                sock.close()
                break
        except:
            break

# Start the send and receive threads
Thread(target=send_message).start()
Thread(target=receive_message).start()
