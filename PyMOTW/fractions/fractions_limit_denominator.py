#!/usr/bin/python

# Fraction: 分数
import fractions
import math

print 'PI   :', math.pi

f_pi = fractions.Fraction(str(math.pi))
print 'No limit = ', f_pi

for i in range(1, 100, 5):
    limited = f_pi.limit_denominator(i)
    print '{0:8} = {1}'.format(i, limited)
