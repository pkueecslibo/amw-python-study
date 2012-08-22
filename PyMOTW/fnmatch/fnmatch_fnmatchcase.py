#!/usr/bin/python
#!-*- coding:utf-8 -*-

import fnmatch
import os

'''
默认是大小写不敏感
'''
pattern = 'FNMATCH_*.PY'
print 'Pattern:', pattern
print

files = os.listdir('.')

for name in files:
    print 'Filename: %-25s %s' % (name, fnmatch.fnmatchcase(name, pattern))

