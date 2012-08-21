#!/usr/bin/python
#!-*- coding:utf-8 -*-

import copy
import pprint

class Graph:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
    def addConnection(self, other):
        self.connections.append(other)
    def __repr__(self):
        return '<Graph(%s) id=%s>' % (self.name, id(self))
    def __deepcopy__(self, memo):
        print
        print repr(self)
        not_there = []
        existing = memo.get(self, not_there)
        if existing is not not_there:
            print 'ALREADY COPIED TO', repr(existing)
            return existing
        pprint.pprint(memo, indent=4, width=40)
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print ' COPYING TO', repr(dup)
        memo[self] = dup
        for c in self.connections:
            dup.addConnection(copy.deepcopy(c, memo))
        return dup

root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.addConnection(a)
root.addConnection(b)

dup = copy.deepcopy(root)
