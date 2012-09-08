#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序13】
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
"""

def getDigital(n):
    l = []
    if n == 0:
        l.insert(0, 0)
        return l
    while n:
        l.insert(0, n%10)
        n /= 10
    return l

if __name__ == '__main__':
    """
    """
    for n in range(100, 1000):
        l = getDigital(n)
        ll = [x*x*x for x in l]
        if sum(ll) == n:
            print n
        
