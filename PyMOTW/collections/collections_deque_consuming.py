#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

print 'From the right:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.pop()
    except IndexError:
        break

print '\nFrom the left:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.popleft()
    except IndexError:
        break


