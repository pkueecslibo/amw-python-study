#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
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
        i += 2 # 加2而不是加1的原因是因为 到这一步的n只能是奇数，那么只能分解成两个奇数相乘，所以直接判断n能否被一个奇数求模就可以了。
    return True

if __name__ == '__main__':

    for n in range(101, 200, 1):
        if isPrime(n):
            print n


