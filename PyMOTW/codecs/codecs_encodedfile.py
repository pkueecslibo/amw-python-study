#!/usr/bin/python
#-*- coding:utf-8 -*-

from codecs_to_hex import to_hex

import codecs
from cStringIO import StringIO

# Raw version of the original data.
data = u'pi \u03c0'

# Manually encode it as UTF-8
utf8 = data.encode('utf-8')
print 'Start as UTF-8   :', to_hex(utf8, 1)

# Set up an output buffer, then wrap it as an EncodedFile
output = StringIO()
#data_encoding: 写入wrapped version of file的string使用此參數編碼
#file_encoding:寫入原始file的使用此参数编码
encoded_file = codecs.EncodedFile(output, data_encoding='utf-8', file_encoding='utf-16')
encoded_file.write(utf8) 

# Fetch the buffer contents as a UTF-16 encoded byte string
utf16 = output.getvalue() # 从原始文件中取得值,所以是UTF-16编码
print 'Encoded to UTF-16    :', to_hex(utf16, 2)

# Set up another buffer with the UTF-16 for reading,
# and wrap it with another EncodedFile.
buffer = StringIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8', file_encoding='utf-16')

# Read the utf-8 encoded version of the data
recoded = encoded_file.read() #从包装文件中读取,所以是UTF-8编码
print 'Back to UTF-8    :', to_hex(recoded, 1)
