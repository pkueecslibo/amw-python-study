#!/usr/bin/python
#!-*- coding:utf-8 -*-
'''
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

import os
import sys
import itertools

if __name__ == '__main__':
    l = (1, 2, 3, 4)
    r = []

    for i in itertools.permutations(range(1, 5), 3):
        r.append(eval('%d*100 + %d*10 + %d' % i))

    print '共有：', len(r)
    print '排序如下：', r

    

