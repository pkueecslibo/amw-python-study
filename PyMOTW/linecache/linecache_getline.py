#!/usr/bin/python

import linecache
from linecache_data import *

filename = make_tempfile()

# pick out the same line from source and cache
# (Notice that linecache counts from 1).
print 'SOURCE: ', lorem.split('\n')[4]
print 'CACHE : ', linecache.getline(filename, 5).rstrip()

cleanup(filename)
