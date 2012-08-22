#!/usr/bin/python

import tempfile

temp = tempfile.NamedTemporaryFile(suffix='_suffix',
                                    prefix='prefix_',
                                    dir='/tmp',
                                    )
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()
