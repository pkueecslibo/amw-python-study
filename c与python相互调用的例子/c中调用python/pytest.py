#!/usr/bin/python
#-*- coding:utf-8 -*-


#定义一个函数
def add(a, b):
    print 'in python function add'
    print 'a = ', str(a)
    print 'b = ', str(b)
    print 'ret = ', a + b
    return a + b


#定义一个类
class Person():
    def sayHi(self, Name):
        print 'Hello, Mr.', Name

