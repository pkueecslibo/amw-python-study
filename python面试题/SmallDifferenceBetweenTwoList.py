#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
这个解法有问题！！！！！！！！！！！！！！！！！！！！！１

有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
1. 将两序列合并为一个序列，并排序，为序列Source
2. 拿出最大元素Big，次大的元素Small
3. 在余下的序列S[:-2]进行平分（每次选择两个），将大的放在min序列，小的放在max序列 
4. 将Small加到max序列，将Big加大min序列，重新计算新序列和，和大的为max，小的为min。
"""

import random

def gernerateList(a):
    for i in range(10):
        a.append(random.randint(1, 99))


def reallocateList(a, b):
    c = a + b
    c.sort()

    #clear a & b
    for idx in range(len(a)):
        del a[0]
        del b[0]
    
    big1 = c[len(c) - 1]
    big2 = c[len(c) - 2]
    print 'big1: ', big1
    print 'big2: ', big2


    suma = 0
    sumb = 0
    for i in range(0, len(c) - 2, 2):
        a.append(c[i])
        suma += c[i]
        b.append(c[i+1])
        sumb += c[i+1]
    if suma > sumb:
        a.append(big2)
        b.append(big1)
        suma += big2
        sumb += big1
    else:
        a.append(big1)
        b.append(big2)
        suma += big1
        sumb += big2

    print 'a: ', a, 'sum: ', suma
    print 'b: ', b, 'sum: ', sumb



if __name__ == '__main__':
    a = []
    b = []
    gernerateList(a)
    gernerateList(b)
    print a
    print b
    reallocateList(a, b)

