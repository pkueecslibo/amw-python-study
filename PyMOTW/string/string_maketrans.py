#!/usr/bin/python
#!-*- coding:utf-8 -*-

import string

leet = string.maketrans('abegiloprstz', '463611092572')

s = 'The quick brown fox jumped over the lazy dog.'

print s
print s.translate(leet)

