#!/usr/bin/python

import array
import binascii
import tempfile

a = array.array('i', xrange(5))
print 'A1: ', a

# Write teh array of numbers to the file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

# Read the raw data
input = open(output.name, 'rb')
raw_data = input.read()
print 'Raw Contents: ', binascii.hexlify(raw_data)

# Read the data into an array
input.seek(0)
a2 = array.array('i')
a2.fromfile(input, len(a))
print 'A2: ', a2
