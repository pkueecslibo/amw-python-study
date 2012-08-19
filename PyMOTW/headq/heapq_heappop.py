#!/usr/bin/python
#!-*- coding:utf-8 -*-

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print 'random   :', data
heapq.heapify(data)
print 'heapified:', data
show_tree(data)
print

inorder = []
while data:
    smallest = heapq.heappop(data)
    print 'pop  %3d:' % smallest
    show_tree(data)
    inorder.append(smallest)
print 'inorder  :', inorder

