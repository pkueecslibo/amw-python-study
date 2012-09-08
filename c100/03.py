#!/usr/bin/python
#!-*- coding:utf-8 -*-

import math

"""
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""

if __name__ == '__main__':
    for i in range(0, 100000):
        x = (int)(math.sqrt(i + 100))
        if x * x != (i + 100):
            continue
        y = (int)(math.sqrt(i + 268))
        if y * y != (i + 268):
            continue
        print i

