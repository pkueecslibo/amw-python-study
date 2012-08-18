#!/usr/bin/python
#!-*- coding:utf-8 -*-

import datetime

today = datetime.date.today()
print today
print 'ctime    :', today.ctime() # 返回一个代表日期的字符串
print 'tuple    :', today.timetuple()
print 'ordinal  :', today.toordinal() # 从公元1年1月1日开始到现在的天数.
print 'Year     :', today.year
print 'Mon      :', today.month
print 'Day      :', today.day
print 'Weekday  :', today.weekday() # 今天是这个星期的第几天，从星期一是第0天开始
