#!/usr/bin/python
#!-*- coding:utf-8 -*-


import string

values = { 'var':'foo' }

t = string.Template("$var is here but $missing is not provided")

try:
    print 'TEMPLATE:', t.substitute(values)
except KeyError, err:
    print 'ERROR:', str(err)

print 'TEMPLATE:', t.safe_substitute(values)
