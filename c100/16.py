#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序16】
题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
"""

#最大公约数
def gcd(m, n):
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m % n
    return m

def lcm(m, n):
    return m * n / gcd(m, n)

if __name__ == '__main__':
    """
    """
    input = eval(raw_input('输入以逗号隔开的m,n:'))
    m = input[0]
    n = input[1]

    print '最大公约数:', gcd(m, n)
    print '最小公倍数:', lcm(m, n)



