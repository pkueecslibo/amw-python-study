#!/usr/bin/python
#!-*- coding:utf-8 -*-

import bisect
import random

# Use a constant see to ensure that we wee 
# the same pseudo-random numbers each time
# we run the loop.
random.seed(1)

# Generate 20 random numbers and
# insert them into a list in sorted
# order.
# func_left() func_right()它们的区别是如果插入值x， 它已经 有相同的值y，如果x要插入到y左边就是_left，否则是_right
l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print '%2d %2d' % (r, position), l

