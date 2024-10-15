# These instructions are for running TwoWayAsyncMesg application written in python

# First, run the server program with a port number (say 50000)
% python TwoWayAsyncMesgServer.py 50000

# Then, run the client program with the server's whereabouts
% python TwoWayAsyncMesgClient.py localhost 50000

# Type messages at the client/server and see them displayed at the server/client
# Client and server do not have to take turns to send messages to each other

# To end the client or server, type Ctrl-D (on Windows Ctrl-Z followed by # return)
# This is referred to as EOF (end of file), meaning end of input
# Then, the other will also quit saying server/client closed the connection
