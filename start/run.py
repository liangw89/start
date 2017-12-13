#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import time
import os
import socket
import uuid
import subprocess
from shutil import copyfile
try:
	import urllib2
	from urllib2 import urlopen
except:
	from urllib.request import urlopen

import decimal

import sys, time


MY_PORT = 1234

BUFSIZE = 1024 * 64

# create a new context for this task
ctx = decimal.Context()

# 20 digits should be enough for everyone :D
ctx.prec = 20

def fstr(f):
	"""
	Convert the given float to a string,
	without resorting to scientific notation
	"""
	d1 = ctx.create_decimal(repr(f))
	return format(d1, 'f')


def stat_basic():
	# Test if have visited the container before
	log_file = 'D:\\local\\Temp\\test_access.log'
	new_id = str(uuid.uuid4())
	try:
		exist_id = open(log_file).read().strip('\n')
	except:
		open(log_file, 'w').write(new_id)
		exist_id = new_id

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	eip = s.getsockname()[0]

	iip = socket.gethostbyname(socket.getfqdn()[:-1])

	# Get cgroup ids
	rip = "None"
	try:
		rip = str(urlopen('http://ip.42.pl/raw').read())
	except:
		pass
	# Get uptime
	
	return [exist_id, new_id, rip, eip, iip]




tm_st = time.time() * 1000

basic_info = stat_basic()

tm_ed = time.time() * 1000
# Only return info of interest
timing_info = [fstr(tm_st), fstr(tm_ed), fstr(tm_ed - tm_st)]

res = '#'.join(basic_info + timing_info)


response = open(os.environ['res'], 'w')
response.write(res)
response.close()
