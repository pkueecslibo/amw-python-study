#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

for path in ['.', '..', './one/two/three', '../one/two/three']:
    print '"%s" : "%s"' % (path, os.path.abspath(path))

