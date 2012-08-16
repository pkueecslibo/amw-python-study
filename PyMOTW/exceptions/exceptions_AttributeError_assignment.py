#!/usr/bin/python

class MyClass(object):
    
    @property
    def attribute(self):
        return 'This is the attribute value'

o = MyClass()
print o.attribute
o.attribute = 'New value'
