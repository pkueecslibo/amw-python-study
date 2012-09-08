#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序10】
题目：打印楼梯，同时在楼梯上方打印两个笑脸。 
"""

if __name__ == '__main__':
    m, n = 10, 5
    print u'\u263a' * n
    for i in range(m):
        print ' ' * i, u'\u2588' * n


