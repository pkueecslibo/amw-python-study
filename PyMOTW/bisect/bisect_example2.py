#!/usr/bin/python
#!-*- coding:utf-8 -*-

import bisect
import random

# Reset the seed
random.seed(1)

# Use bisect_left and insort_left
l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect_left(l, r)
    bisect.insort(l, r)
    print '%2d %2d' % (r, position), l

