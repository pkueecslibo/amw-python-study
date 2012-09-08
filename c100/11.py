#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序11】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""

if __name__ == '__main__':
    r1 = 2
    r2 = 0
    r3 = 0
    fmt = '成熟体:{0}\t二月体:{1}\t一月体:{2}\t总数:{3}'

    print fmt.format(r3, r2, r1, r1+r2+r3)

    for month in range(10):
        r3 += r2
        r1, r2 = r3, r1
        print fmt.format(r3, r2, r1, r1+r2+r3)


