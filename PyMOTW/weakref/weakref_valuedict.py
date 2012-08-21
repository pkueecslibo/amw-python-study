#!/usr/bin/python
#!-*- coding:utf-8 -*-

import gc
from pprint import pprint
import weakref
import sys

gc.set_debug(gc.DEBUG_LEAK)

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name
    def __del__(self):
        print '(Deleting %s)' % self

def demo(cache_factory):
    # hold objects so any weak references 
    # are not removed immediately
    all_refs = {}
    # the cache using the factory we're given
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print 'all_refs = '
    pprint(all_refs)
    print 'Before, cache contains:', cache.keys()
    for name, value in cache.items():
        print ' %s = %s' % (name, value)
        del value # decref
        #这是的value也会对对象增加一次引用，如果不主动del这个变量，那么对前两个对象的引用会自动消去，但是对最后一个元素的引用的消去时间不容易确定

    # Remove all references to our objects except the cache
    print 'Cleanup:',
    del all_refs
    gc.collect()

    print 'After, cache contains:', cache.keys()
    for name, value in cache.items():
        print ' %s = %s' % (name, value)
    print 'demo returning'
    return

demo(dict)
print
demo(weakref.WeakValueDictionary)
