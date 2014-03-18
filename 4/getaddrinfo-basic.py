#!/usr/bin/env python
#basic getaddrinfo() basic example

import sys, socket

result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)

counter = 0
for item in result:
    print "%-2d: %s" % (counter, item[4])
    counter += 1
