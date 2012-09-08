#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    """
    """
    for x in range(2,1000):
        x_tmp = x
        factors = []
        for i in range(1, x):
            if x % i == 0:
                factors.append(i)

        if sum(factors) == x_tmp:
            print '%d 是一个完数' % x_tmp, factors





