#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

print 'dict         :',
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'E'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'E'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'OrderedDict  :',

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'E'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'E'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2
