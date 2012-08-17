#!/usr/bin/python
#!-*- coding:utf-8 -*-

import codecs
from cStringIO import StringIO

buffer = StringIO()
stream = codecs.getwriter('rot_13')(buffer)

text = 'abcdefghijklmnopqurstuvwxyz'

stream.write(text)
stream.flush()

print 'Original :', text
print 'ROT-13   :', buffer.getvalue()
