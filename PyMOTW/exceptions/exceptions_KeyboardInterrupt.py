#!/usr/bin/python

try:
    print 'Press Return or Ctrl-c:'
    ignored = raw_input()
except Exception, err:
    print 'Caught exception:', err
except KeyboardInterrupt, err:
    print 'Caught exception:'
else:
    print 'No exception'
