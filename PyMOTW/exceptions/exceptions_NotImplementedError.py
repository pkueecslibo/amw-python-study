#!/usr/bin/python

class BaseClass(object):
    """Defines the interface"""
    def __init__(self):
        super(BaseClass, self).__init__()

    def do_something(self):
        """The interface, not implemented"""
        raise NotImplementedError(self.__class__.__name__ + '.do_something')

class SubClass(BaseClass):
    """Implementes the interface"""
    def do_something(self):
        """really does somethine"""
        print self.__class__.__name__ + ' doing something!'

SubClass().do_something()
BaseClass().do_something()

