#!/usr/bin/python
#!-*- coding:utf-8 -*-

import decimal

a = decimal.Decimal('5.1')
b = decimal.Decimal('3.14')
c = 4
d = 3.14

print 'a    =', a
print 'b    =', b
print 'c    =', c
print 'd    =', d

print 'a+b  =', a + b
print 'a-b  =', a - b
print 'a*b  =', a * b
print 'a/b  =', a / b
print 

print 'a+c  =', a + c
print 'a-c  =', a - c
print 'a*c  =', a * c
print 'a/c  =', a / c

print 'a + d = ',
try:
    print a + d
except TypeError, e:
    print e

