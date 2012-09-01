#!/usr/bin/python
#!-*- coding:utf-8 -*-

from shutil import *
from glob import glob

f = open('example.txt', 'wt')
f.write('contents')
f.close()

print 'BEFORE:', glob('example*')
mv('example.txt', 'example.out')
print 'AFTER:', glob('example*')

