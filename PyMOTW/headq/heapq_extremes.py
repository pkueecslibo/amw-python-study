#!/usr/bin/python
#!-*- coding:utf-8 -*-

import heapq
from heapq_heapdata import data

# 只有在n比较小的情况下才比较高效
print 'all       :', data
print '3 largest :', heapq.nlargest(3, data)
print 'from sort :', list(reversed(sorted(data)[-3:]))
print '3 smallest:', heapq.nsmallest(3, data)
print 'from sort :', sorted(data)[:3]

