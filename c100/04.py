#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序4】
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""

if __name__ == '__main__':
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]

    year = eval(raw_input('输入年份:'))
    month = eval(raw_input('输入月份：'))
    day = eval(raw_input('输入日期:'))

    days_count = 0
    
    days_count += sum(month_day[0:month - 1])

    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month >= 3:
        days_count += 1

    days_count += day
    
    print days_count

