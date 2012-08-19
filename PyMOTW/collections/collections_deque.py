#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

d = collections.deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

#可以从中间某个值删除
#虽然它是一个队列，但是没有那么严格的要求
d.remove('c')
print 'remove(c):', d

