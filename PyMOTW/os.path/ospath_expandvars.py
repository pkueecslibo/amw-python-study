#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

os.environ['MYVAR'] = 'VALUE'

print os.path.expandvars('/path/to/$MYVAR')
