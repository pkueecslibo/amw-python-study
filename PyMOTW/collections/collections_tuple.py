#!/usr/bin/python
#!-*- coding:utf-8 -*-

bob = ('Bob', 30, 'male')
print 'Representation:', bob

jane=  ('Jane', 29, 'female')
print '\nField by index:', jane[0]

print 'Fields by index:'
for p in [bob, jane]:
    print '%s is a %d year old %s' % p


