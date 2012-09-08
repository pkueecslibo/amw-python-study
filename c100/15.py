#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序15】
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""

if __name__ == '__main__':
    """
    """
    score = eval(raw_input('输入分数:'))

    if score >= 90:
        print 'A'
    elif score < 90 and score >= 60:
        print 'B'
    else:
        print 'C'
