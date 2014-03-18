# !/usr/bin/env python
#simple server
import socket

host = ''   #bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." % port

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("you entered %d character.\n" % len(line))
    clientfile.close()
    clientsock.close()
