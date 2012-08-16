#!/usr/bin/python
#!-*- coding:utf-8 -*-

#包含yield语句的函数会被特地编译成生成器
#所以可以对此对象的实例调用next()和close()方法
#也可以说此对象的实例是可迭代的

def my_generator():
    try:
        for i in range(5):
            print 'Yielding', i
            yield i
    except GeneratorExit:
        print 'Exiting early'

g = my_generator()
print g.next()
g.close()

f = my_generator()
for i in f:
    print i
