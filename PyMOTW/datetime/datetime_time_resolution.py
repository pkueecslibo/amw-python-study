#!/usr/bin/python
#!-*- coding:utf-8 -*-

import datetime

#实际上，resolution 表示的是两个不相等的时间的最小可能差别
for m in [1, 0, 0.1, 0.6]:
    try:
        print '%02.1f :' % m, datetime.time(0, 0, microsecond=m)
    except TypeError, err:
        print 'ERROR: ', err
