#!/usr/bin/pyton
#!-*- coding:utf-8 -*-

import os
import sys

def convert(filename, in_enc='GBK', out_enc='UTF-8'):
    try:
        print 'convert: ', filename
        content = open(filename).read()
        new_content = content.decode(in_enc).encode(out_enc)
        open(filename, 'w').write(new_content)
        print 'done'
    except:
        print 'error'

def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            convert(path)


def main():
    if len(sys.argv) <= 1:
        print 'usage: iconv path [, path] [FILE]'
    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print '地址:', path, '无效'
            continue
        else:
            if os.path.isfile(path):
                convert(path)
            else:
                explore(path)


if __name__ == '__main__' :
    main()
