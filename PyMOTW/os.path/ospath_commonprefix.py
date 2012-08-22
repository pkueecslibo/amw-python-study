#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
print paths
print os.path.commonprefix(paths)
