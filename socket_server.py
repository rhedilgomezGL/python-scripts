#!/usr/bin/env python

import socket
import sys

print >>sys.stderr, 'Starting server, use <Ctrl-C> to stop'
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Listen for incoming connections
sock.listen(1)
try:
    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
    
        try:
            print >>sys.stderr, 'connect from', client_address
    
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >>sys.stderr, 'no data from', client_address
                    break
    
        finally:
            # Clear up the connection
            connection.close()

except KeyboardInterrupt:
    print >>sys.stderr, "Stop the server......"
