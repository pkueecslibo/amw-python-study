#!/usr/bin/python

import codecs
from codecs_to_hex import to_hex

#BOM    :   byte order mask
#BOM is an alias for BOM_UTF16, BOM_LE for BOM_UTF16_LE and BOM_BE for BOM_UTF16_BE
for name in ['BOM', 'BOM_BE', 'BOM_LE', 
        'BOM_UTF8', 
        'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE',
        'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE']:
    print '{:12} : {}'.format(name, to_hex(getattr(codecs, name), 2))
