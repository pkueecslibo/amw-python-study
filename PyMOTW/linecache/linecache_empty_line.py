#!/usr/bin/python

import linecache
from linecache_data import *

filename = make_tempfile()

# Blank lines include the newline
print '\nBLANK : "%s"' % linecache.getline(filename, 0)

cleanup(filename)
