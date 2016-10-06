#!usr/bin/env python
#encoding=utf-8

import urllib
import urllib2
import re

page = 1

url = 'http://www.iqshw.com/' 

headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

request = urllib2.Request(url,headers = headers)

response = urllib2.urlopen(request)

content = response.read()

print content