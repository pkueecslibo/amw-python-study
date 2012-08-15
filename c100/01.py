#!/usr/bin/python
#!-*- coding:utf-8 -*-

'''
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

if __name__ == '__main__':
    l = (1, 2, 3, 4)
    no = []
    s = set()

    for x in range(len(l)):
        no.append(x)
        for y in range(len(l)):
            if y not in no:
                no.append(y)
                for z in range(len(l)):
                    if z not in no:
                        no.append(z)
                        s.add(l[no[0]]*100 + l[no[1]]*10 + l[no[2]])
                        no.pop()
                no.pop()
        no.pop()

    print '总共有：',len(s)
    print '如下：', s
                        

    

