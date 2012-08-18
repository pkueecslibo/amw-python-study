#!/usr/bin/python

import difflib
from difflib_data import *

#unified_diff只显示修改的行和一点上下文
diff = difflib.unified_diff(text1_lines, text2_lines)
print '\n'.join(list(diff))
