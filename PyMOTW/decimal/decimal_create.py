#!/usr/bin/python
#!-*- coding:utf-8 -*-

import decimal

fmt = '{0:<20} {1:<20}'
print fmt.format('Input', 'Output')
print fmt.format('-' * 20, '-' * 20)

# Integer
print fmt.format(5, decimal.Decimal(5))

# String 
print fmt.format('3.14', decimal.Decimal('3.14'))

# Float
print fmt.format(repr(0.1), decimal.Decimal(str(0.1)))

