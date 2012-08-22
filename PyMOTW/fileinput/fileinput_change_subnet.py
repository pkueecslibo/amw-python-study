#!/usr/bin/python

import fileinput
import sys

from_base = sys.argv[1]
to_base = sys.argv[2]
files = sys.argv[3:]

for line in fileinput.input(files, inplace=True):
    line = line.strip().replace(from_base, to_base)
    print line # 尽管这里有print方法,但是,实际程序并没有输出到标准输出窗口,因为fileinput把输出映射到了原文件
