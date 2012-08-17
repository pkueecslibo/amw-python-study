#!/usr/bin/python
#!-*- coding:utf-8 -*-

import codecs
import sys

text = u'pi: π'

# Wrap sys.stdout with a writer that knows how to handle encoding 
# Unicide data.
wrapped_stdout = codecs.getwriter('UTF-8')(sys.stdout)
wrapped_stdout.write(u'Via write: ' + text + '\n')

# Replace sys.stdout with a writer
sys.stdout = wrapped_stdout

print u'Via write: ', text
