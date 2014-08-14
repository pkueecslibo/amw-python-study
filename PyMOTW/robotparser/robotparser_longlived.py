#!/usr/bin/python

import robotparser
import time
import urlparse

AGENT_NAME = "PyMOTW"
parser = robotparser.RobotFileParser()
# Using the local copy
parser.set_url('robot.txt')
parser.read()
parser.modified()

PATHS = [
	'/',
	'PyMOTW/',
	'/admin/',
	'/downloads/PyMOTW-1.92.tar.gz',
	]

for n, path in enumerate(PATHS):
	print
	age = int(time.time() - parser.mtime())
	print 'age:', age
	if age > 1:
		print 're-reading robots.txt'
		parser.read()
		parser.modified()
	else:
		print
	print '%6s : %6s' % (parser.can_fetch(AGENT_NAME, path), path)
	# Simulate a delay in processing
	time.sleep(1)