#!/usr/bin/python
#!-*- coding:utf-8 -*-

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

# heapify可以称为堆化
# 也就是可以将一个普通的list转变为一个堆
# 原地，线性时间
print 'random   :', data
heapq.heapify(data)
print 'heapified:'
show_tree(data)

