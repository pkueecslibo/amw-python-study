#!/usr/bin/python
#!-*- coding:utf-8 -*-

'''
Formatting  and Parsing
format: 将时间格式化
parse : 将时间解析
'''

import datetime

format = '%a %b %d %H:%M:%S %Y'

today = datetime.datetime.today()
print 'ISO      :', today

s = today.strftime(format)
print 'strftime :', s

d = datetime.datetime.strptime(s, format)
print 'strptime :', d.strftime(format)
