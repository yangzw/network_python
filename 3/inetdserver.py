#!/usr/bin/env python
#basic inetd server
import sys
print "Welcome."
print "Please enter a string:"
sys.stdout.flush()
line = sys.stdin.readline().strip()
print "You entered %d characters." % len(line)
