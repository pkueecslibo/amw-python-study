#!/usr/bin/python
#!-*- coding:utf-8 -*-

# This example is taken from the source for difflib.py

from difflib import SequenceMatcher

A = " abcd"
B = "abcd abcd"

# The %s specifier converts the object using str(), and %r converts it using repr().
print 'A = %r' % A
print 'B = %r' % B

print '\nWidthout junk detection:'

#SequenceMatcher 第一个参数可以用来排除一些不需要比较的字符，可以用一个lambda表达式，返回为true表示此字符不需要比较 
s = SequenceMatcher(None, A, B)
i, j, k = s.find_longest_match(0, 5, 0, 9)
print ' i = %d' % i
print ' j=  %d' % j
print ' k = %d' % k
print ' A[i:i+k] = %r' % A[i:i+k]
print ' B[j:j+k] = %r' % B[j:j+k]

print '\nTreat spaces as junk:'

s = SequenceMatcher(lambda x: x == ' ', A, B)
i, j, k = s.find_longest_match(0, 5, 0, 9)
print ' i = %d' % i
print ' j=  %d' % j
print ' k = %d' % k
print ' A[i:i+k] = %r' % A[i:i+k]
print ' B[j:j+k] = %r' % B[j:j+k]


