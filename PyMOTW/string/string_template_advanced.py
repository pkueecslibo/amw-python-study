#!/usr/bin/python
#!-*- coding:utf-8 -*-

import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate('%% %with_underscore %notunderscored')
d = { 'with_underscore':'replaced', 
        'notunderscored':'not replaced',
        }

print t.safe_substitute(d)

