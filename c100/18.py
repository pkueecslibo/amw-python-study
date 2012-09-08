#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序18】
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
"""

if __name__ == '__main__':
    """
    """
    a = raw_input('输入a:')
    n = input('输入n:')

    result = 0
    s = ''
    print a,
    for i in range(n):
        s = s+a
        print '+', s,
        result += eval(s)
    
    print result

