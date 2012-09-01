#!/usr/bin/python
#!-*- coding:utf-8 -*-

from shutil import *
from commands import *

print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
copytree('example', '/tmp/example')
print 'AFTER:'
print getoutput('ls -rlast /tmp/example')

