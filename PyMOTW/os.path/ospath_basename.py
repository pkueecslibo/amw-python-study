#!/usr/bin/python

import os.path

for path in [   '/one/two/three',
                '/onw/two/three/',
                '/',
                '.',
                '']:
    print '"%s" : "%s"' % (path, os.path.basename(path))
