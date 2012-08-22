#!/usr/bin/python
#!-*- coding:utf-8 -*-

from pprint import pprint

from pprint_data import data

for d in data:
    for c in 'defgh':
        del d[1][c]

for width in [ 80, 20, 5 ]:
    print 'WIDTH =', width
    pprint(data, width=width)
    print
