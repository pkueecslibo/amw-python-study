#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

c = collections.Counter('extremely')
c['z'] = 0
print c
#elements()返回所有已知的item，但不保证顺序，也不包括计数为0的item
print list(c.elements())

