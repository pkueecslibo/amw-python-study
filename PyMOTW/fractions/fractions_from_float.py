#!/usr/bin/python

import fractions

for v in [0.1, 0.5, 1.5, 2.0]:
    print '%s = %s' % (v, fractions.Fraction.from_float(v))
