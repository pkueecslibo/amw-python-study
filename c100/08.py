#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序8】
题目：输出9*9口诀。
"""

if __name__ == '__main__':
    for row in range(1, 10, 1):
        for col in range(1, row+1, 1):
            print '%d * %d = %d'  % (col, row, row*col),
        print 
    print 

