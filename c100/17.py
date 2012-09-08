#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

if __name__ == '__main__':
    """
    """
    alphanet_num = 0
    blank_num = 0
    numberic_num = 0
    other_num = 0

    s = raw_input('请输入一行字符串:')
    
    for i in range(len(s)):
        if ord(s[i]) in range(ord('a'), ord('z')+1) or s[i] in range(ord('A'), ord('Z')):
            alphanet_num += 1
        elif ord(s[i]) in range(ord('0'), ord('9')+1):
            numberic_num += 1
        elif s[i] == ' ':
            blank_num += 1
        else:
            other_num += 1

    print '字母:', alphanet_num
    print '数字:', numberic_num
    print '空格:', blank_num
    print '其它字符:', other_num


