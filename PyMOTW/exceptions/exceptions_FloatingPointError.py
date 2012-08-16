#!/usr/bin/python

import math
import fpectl

print 'Control off:', math.exp(1000)
fpectl.turnon_sigfpe()
print 'Control off:', math.exp(1000)
