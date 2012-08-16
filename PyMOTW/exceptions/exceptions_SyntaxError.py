#!/usr/bin/python

try:
    print eval('five times three')
except SyntaxError, err:
    print 'Syntax error %s (%s-%s): %s' % \
            (err.filename, err.lineno, err.offset, err.text)
