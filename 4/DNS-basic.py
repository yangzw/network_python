#!/usr/bin/env python
import sys, DNS

query = sys.argv[1]
DNS.DiscoverNameServers() #find name serverses in your system. /etc/resolv.conf in unix.

reqobj = DNS.Request()

answerobj = reqobj.req(name = query, qtype = DNS.Type.ANY)
if not len(answerobj.answers):
    print "Not found."
for item in answerobj.answers:
    print "%-5s %s" % (item['typename'], item['data'])
