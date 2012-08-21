#!/usr/bin/python
#!-*- coding:utf-8 -*-

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

obj = ExpensiveObject()
r = weakref.ref(obj)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'deleting ojb'
del obj
print 'r():', r()
