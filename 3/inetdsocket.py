#!/usr/bin/env python
#socket-based inetd server

import sys,socket,time
s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
s.sendall("Welcome.\n")
s.sendall("According to our records, you are connected from %s.\n" % str(s.getpeername()))
s.sendall("The local time is %s.\n" % time.asctime())
