#!/usr/bin/python
#!-*- coding:utf-8 -*-
'''
【程序2】
题目：企业发放的奖金根据利润提成。利润(i)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润i，求应发放奖金总数？
'''

import os
import sys

if __name__ == '__main__':

    bonus_per = (0.0, 0.1, 0.075, 0.05, 0.03, 0.015, 0.01)
    key_point = (0, 10, 20, 40, 60, 100)
    profit = eval(raw_input())
    bonus = 0

    for i in range(1, 6, 1):
        if profit > key_point[i]:
            bonus += (key_point[i] - key_point[i-1]) * bonus_per[i]
        else:
            bonus += (profit - key_point[i - 1]) * bonus_per[i]
            break
    print 'bonus =', bonus
