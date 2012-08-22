#!/usr/bin/python
#!-*- coding:utf-8 -*-

import glob

for name in glob.glob('dir/file?.txt'):
    print name
