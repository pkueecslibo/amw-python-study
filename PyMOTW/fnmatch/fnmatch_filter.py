#!/usr/bin/python

import fnmatch
import os

pattern = 'fnmatch_*.py'
print 'Pattern:', pattern

files = os.listdir('.')
print 'Files:', files

print 'Matches :', fnmatch.filter(files, pattern)
