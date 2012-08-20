#!/usr/bin/python
#!-*- coding:utf-8 -*-

import sched
import time

# 当某一事件延迟后,后面的事件依次延迟
# 而且当此事件完成后,后面的事件立即开始

scheduler = sched.scheduler(time.time, time.sleep)

def long_event(name):
    print 'BEGIN EVENT  :', time.time(), name
    time.sleep(2)
    print 'FINISH EVENT :', time.time(), name

print 'START:', time.time()
scheduler.enter(2, 1, long_event, ('first', ))
scheduler.enter(3, 1, long_event, ('second', ))

scheduler.run()
