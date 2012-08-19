#!/usr/bin/python
#!-*- coding:utf-8 -*-

import collections

Person = collections.namedtuple('Person', 'name old gender')

print 'Type of Person:', type(Person)

bob = Person(name='bob', old=30, gender='male')
print '\nRepresentation:', bob

jane = Person(name='Jane', old = 29, gender='female')
print '\nField by name:', jane.name

print '\nFields by index:'
for p in [bob, jane]:
    print '%s is a %d year old %s' % p

