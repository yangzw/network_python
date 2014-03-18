#!/usr/bin/env python
#XML-RPX Basic Client

import xmlrpclib
url = 'http://www.oreillynet.com/meerkat/xml-rpc/server.php'
s = xmlrpclib.ServerProxy(url)
catdata = s.meerkat.getCategories()
cattitles = [item['title'] for item in catdata]
cattitiles.sort()
for item in cattitles:
    print item
