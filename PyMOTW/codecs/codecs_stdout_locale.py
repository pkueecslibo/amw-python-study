#!/usr/bin/python
#!-*- coding:utf-8 -*-

import codecs
import sys
import locale

text = u'pi: π'

# Configure locale from the user's environment settings.
locale.setlocale(locale.LC_ALL, '')

# Wrap stdout with an encoding-aware writer
lang, encoding = locale.getdefaultlocale()
print 'Locale encoding  :', encoding
sys.stdout = codecs.getwriter(encoding)(sys.stdout)

print 'With wrapped stdou:', text
