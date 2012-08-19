#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

c = collections.Counter()
with open('/usr/shar/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
#most_common: 最常出现。参数表示前多少名
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)

