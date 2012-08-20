#!/usr/bin/python
#!-*- coding:utf-8 -*-

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print 'EVENT:', time.time(), name

now = time.time()
print 'START:', now
scheduler.enterabs(now + 2, 2, print_event, ('first',))
scheduler.enterabs(now + 2, 1, print_event, ('second',))
# enterabs 第一个参数是事件运行的绝对时间
# enter 第一个参数是事件运行的延迟时间

scheduler.run()
    
