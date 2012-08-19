#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

def default_factory():
    return 'default value'

# defaultdict 对不存在的item设置默认值，这样给出不存在的key时不会出现KeyError.
d = collections.defaultdict(default_factory, foo='bar')
print 'd:', d
print 'foo=>', d['foo']
print 'bar=>', d['bar']

