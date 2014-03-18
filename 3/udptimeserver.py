#!/usr/bin/env python
#UDP wrong time server
import socket, traceback, time, struct

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    try:
        message, address = s.recvfrom(8192)
        print "Get request from: ", address
        secs = int(time.time())
        secs -= 60*60*24
        secs += 2208988800      #convert to secs since 1/1/1900
        reply = struct.pack("!I",secs)
        print reply
        s.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
