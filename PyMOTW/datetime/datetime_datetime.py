#!/usr/bin/python
#!-*- coding:utf-8 -*-

import datetime

#本地时间，可以指定时间，这样取得就是指定时区的时间
#如果默认的话，在cn就是UTC+8的时间 
print 'Now      :', datetime.datetime.now()
print 'Today    :', datetime.datetime.today()
#UTC 世界标准时间或世界協調時,就是0时区的时间
print 'UTC Now  :', datetime.datetime.utcnow()

d = datetime.datetime.now()
for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print '{:15} : {}'.format(attr, getattr(d, attr))

