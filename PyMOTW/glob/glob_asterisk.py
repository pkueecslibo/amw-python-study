#!/usr/bin/python
#!-*- coding:utf-8 -*-

import glob

# 模式匹配每个文件或是文件夹,但是不会递归到它的子目录中去
for name in glob.glob('dir/*'):
    print name
