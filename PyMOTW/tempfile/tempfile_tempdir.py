#!/usr/bin/python

import tempfile

tempfile.tempdir = '/tmp/tmp'
print 'gettempdir():', tempfile.gettempdir()
