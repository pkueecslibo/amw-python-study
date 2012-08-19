#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections
'''
这里所谓的旋转，是将队列的数据首尾相联
    x → x → x → x → x
    ↑               ↓
    ← ← ← ← ← ← ← ← ←
形成一个环，右旋就是将这个环顺时针旋转，左旋则是逆时针
'''
d = collections.deque(xrange(10))
print 'Normal           :', d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Right rotation   :', d

d = collections.deque(xrange(10))
d.rotate(-2)
print 'Left rotation    :', d

