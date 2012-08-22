#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os.path

for user in [ '', 'dhellmann', 'postgres' ]:
    lookup = '~' + user
    print lookup, ':', os.path.expanduser(lookup)
