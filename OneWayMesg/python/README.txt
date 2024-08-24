# These instructions are for running OneWayMesg application written in python

# First, run the server program with a port number (say 50000)
% python OneWayMesgServer.py 50000

# Then, run the client program with the server's whereabouts
% python OneWayMesgClient.py localhost 50000

# Type messages at the client and see them displayed at the server

# To end the client, type Ctrl-D (on Windows Ctrl-Z followed by return)
# This is referred to as EOF (end of file), meaning end of input
# Then, the server will also quit saying client closed the connection
