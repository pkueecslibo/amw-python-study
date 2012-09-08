#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序6】
题目：用*号输出字母C的图案。
"""

if __name__ == '__main__':
    l = [5, 4, 3, 2, 2]
    c = [3, 1, 1, 1, 1]

    for line in range(5):
        print ' ' * l[line], '*' * c[line]

    for line in range(4, -1, -1):
        print ' ' * l[line], '*' * c[line]
