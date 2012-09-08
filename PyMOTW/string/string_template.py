#!/usr/bin/python
#!-*- coding:utf-8 -*-

import string

values = { 'var':'foo'}

t = string.Template("""
        $var
        $$
        ${var}iable
        """)

print 'TEMPLATE:', t.substitute(values)

s = """
%(var)s
%%
%(var)siable
"""

print 'INTERPLOATION:', s % values

