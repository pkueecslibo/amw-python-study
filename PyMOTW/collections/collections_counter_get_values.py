#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

c = collections.Counter('abcdaab')

#对于未知的item,不会抛出关键字异常。如果一个item不存在，它的计数为0
for letter in 'abcde':
    print '{:2} : {}'.format(letter, c[letter])
