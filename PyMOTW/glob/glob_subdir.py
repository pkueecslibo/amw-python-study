#!/usr/bin/python
#!-*- coding:utf-8 -*-

import glob

print 'Named explicitly:'
for name in glob.glob('dir/subdir/*'):
    print '\t', name

print 'Named with wildcard:'
for name in glob.glob('dir/*/*'):
    print '\t', name

# 因为dir/目录下只有一个目录,所以以是两种方式的结果是一样的
# 但是,假如dir/目录下有多个子目录,那么第二种方式将会匹配所有的子目录,并将所有子目录下的文件都显示出来
