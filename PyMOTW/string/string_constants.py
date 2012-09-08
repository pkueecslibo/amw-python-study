#!/usr/bin/python
#!-*- coding:utf-8 -*-

import string

for n in dir(string):
    if n.startswith(' '):
        continue
    v = getattr(string, n)
    if isinstance(v, basestring):
        print '%s = %s' % (n, repr(v))
        print

