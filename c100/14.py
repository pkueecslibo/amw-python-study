#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序14】
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    """
    """
    fmt = '{0} = {1}'
    result = []

    n = eval(raw_input('输入一个正整数:'))

    print n, '=',
    if isPrime(n):
        result.append(1)
        result.append(n)
    else:
        for i in range(2, n/2, 1):
            while n % i == 0:
                result.append(i)
                n /= i
    print '*'.join(map(str, result))



        


