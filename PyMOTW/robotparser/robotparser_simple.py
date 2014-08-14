#!/usr/bin/python

import robotparser
import urlparse

AGENT_NAME = 'PyMOTW'
URL_BASE = 'http://www.doughellmann.com/'
parser = robotparser.RobotFileParser()
parser.set_url(urlparse.urljoin(URL_BASE, 'robot.txt'))
parser.read()

PATHS = [
	'/',
	'/PyMOTW/',
	'/admin/',
	'/downloads/PyMOTW-1.92.tar.gz',
	]

for path in PATHS:
	# The URL argument to can_fetch() can be a path relative to the root of the site, or full URL
	print '%6s : %6s' % (parser.can_fetch(AGENT_NAME, path), path)	# a path relative to the root of the site
	url = urlparse.urljoin(URL_BASE, path)
	print '%6s : %6s' % (parser.can_fetch(AGENT_NAME, url), url)	# full URL
	print

