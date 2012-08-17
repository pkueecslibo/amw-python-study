#!/usr/bin/python

import array

a = array.array('i', xrange(5))
print 'Initial: ', a

a.extend(xrange(5))
print 'Extends: ', a

print 'Slice: ', a[3:6]

print 'Iterator: ', list(enumerate(a))
