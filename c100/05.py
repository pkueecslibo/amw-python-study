#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出
"""

if __name__ == '__main__':
    input = raw_input()
    numbers = map(int, input.split(' '))
    numbers.sort()
    print numbers
