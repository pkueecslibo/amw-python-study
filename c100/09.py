#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序9】
题目：要求输出国际象棋棋盘。
"""

if __name__ == '__main__':
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                print ' ',
            else:
                print u'\u2587',
        print

