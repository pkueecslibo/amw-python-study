#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

#集合的队列是指：按进入集合的顺序有序
# Add to the right
d = collections.deque()
d.extend('abcdefg')
print 'extend   :', d
d.append('h')
print 'append   :', d

# Add to the left
d = collections.deque()
d.extendleft('abedefg')
print 'extend   :', d
d.appendleft('h')
print 'appendleft:', d

