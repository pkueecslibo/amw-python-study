#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

for path in [ 'one//two//three',
            'one/./two/./three',
            'one/../one/two/three',
            ]:
    print path, ':', os.path.normpath(path)
