#!/usr/bin/python

import itertools

#try to create a MemoryError by allocating a lot of memory
l = []

for i in range(3):
    try:
        for j in itertools.count(1):
            print i, j
            l.append('*' * (2**30))
    except MomeryError:
        print '(error, discarding existing list)'
        l = []
