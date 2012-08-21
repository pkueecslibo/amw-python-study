#!/usr/bin/python
#!-*- coding:utf-8 -*-

import Queue

q = Queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
