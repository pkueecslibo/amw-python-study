#!/usr/bin/python
#!-*- coding:utf-8 -*-

""" 就是按文件的擴展名來分割 """
import os.path

for path in [ 'filename.txt', 'filename', '/path/to/filename.txt', '/', '']:
    print '"%s" :'% path, os.path.splitext(path)
