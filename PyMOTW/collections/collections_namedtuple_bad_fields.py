#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

#不能使用一些特殊的关键字
try:
    collections.namedtuple('Person', 'name class age gender')
except ValueError, err:
    print err
#不能使用重复的关键字
try:
    collections.namedtuple('Person', 'name age gender age')
except ValueError, err:
    print err

