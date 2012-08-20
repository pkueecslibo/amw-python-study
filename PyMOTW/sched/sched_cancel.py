#!/usr/bin/python
#!-*- coding:utf-8 -*-

import sched
import threading
import time

scheduler = sched.scheduler(time.time, time.sleep)

# Set up a global to be modified by the threads
counter = 0

def increment_counter(name):
    global counter
    print 'EVENT:', time.time(), name
    counter += 1
    print 'NOW:', counter

print 'START:', time.time()
e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

# Start a thread to run the events
t = threading.Thread(target=scheduler.run)
t.start()

# Back in the main thread, cancel the first scheduled event
scheduler.cancel(e1)

# Wait for the scheduler to finish running in the thread
t.join()
# join([timeout])方法将会阻塞当前操作直到线程结束
# 如果带有参数,表示超时时间阀值

print 'FINAL:', counter
