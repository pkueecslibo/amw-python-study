#!/usr/bin/python

import array
import binascii

s = 'This is the array.'
a = array.array('c', s)

print 'As tring:', s
print 'As array:', a
print 'As hex   :', binascii.hexlify(s)
