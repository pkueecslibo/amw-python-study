#!/usr/bin/python

import codecs
import sys

from codecs_to_hex import to_hex

error_handling = sys.argv[1]

text = u'pi: \u03c0'
print 'Original     :', text

# Save the data with the one encoding
with codecs.open('decode_error.txt', 'w', encoding='utf-16') as f:
    f.write(text)

# Dump the bytes from file
with open('decode_error.txt', 'rb') as f:
    print 'File contents: ', to_hex(f.read(), 1)

# Try to read the data with the wrong encoding
with codecs.open('decode_error.txt', mode='r',
        encoding='utf-8',
        errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError, err:
        print 'ERROR: ', err
    else:
        print 'Read     :', repr(data)


