#!/usr/bin/python
#!-*- coding:utf-8 -*-

import decimal

# Set up a context with limited precision
c = decimal.getcontext().copy()
c.prec = 3

# Create your constant
pi = c.create_decimal('3.1415')

# The constant value is rounded off
print 'PI:', pi

# The result of using the constant uses the global context
print 'RESULT:', decimal.Decimal('2.01') * pi

