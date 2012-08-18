#!/usr/bin/python
#! -*- coding:utf-8 -*-

import datetime
import time

o = 733114
print 'o:', o
print 'fromordinal(o):', datetime.date.fromordinal(o)
t = time.time() # 返回从公元元年开始到现在以浮点数表示的秒数
print 't:', t
print 'fromtimestamp(t):', datetime.date.fromtimestamp(t)
