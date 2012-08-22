#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

for parts in [('one', 'two', 'three'),
              ('/', 'one', 'two', 'three'),
              ('/one', '/two', '/three'),
              ]:
    print parts, ':', os.path.join(*parts)# join 接受不定參數,帶昨號表示一個任意長的元組,兩個星號表示參數字典
