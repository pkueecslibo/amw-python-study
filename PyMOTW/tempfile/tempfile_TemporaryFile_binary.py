#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os
import tempfile

temp = tempfile.TemporaryFile()
try:
    temp.write('Some data')
    temp.seek(0)

    print temp.read()
finally:
    temp.close()
