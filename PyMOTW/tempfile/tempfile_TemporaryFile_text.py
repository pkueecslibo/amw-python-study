#!/usr/bin/python

import tempfile

f = tempfile.TemporaryFile(mode='w+t')
try:
    f.writelines(['first\n', 'second\n'])
    f.seek(0)
    
    for line in f:
        print line.strip()
finally:
    f.close()
