# These instructions are for running OneWayMesg application written in c

# Compile the server and client programs
% gcc OneWayMesgServer.c -o OneWayMesgServer
% gcc OneWayMesgClient.c -o OneWayMesgClient

# First, run the server with a port number (say 50000)
% ./OneWayMesgServer 50000

# Then, run the client with the server's whereabouts
% ./OneWayMesgClient localhost 50000

# Type messages at the client and see them displayed at the server

# To end the client, type Ctrl-D (on Windows Ctrl-Z followed by return)
# This is referred to as EOF (end of file), meaning end of input
# Then, the server will also quit saying client closed the connection
