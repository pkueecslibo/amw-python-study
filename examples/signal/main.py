#!/usr/bin/python

import gobject
import signal_def as sd
import signal_emit as se

def hello():
    print 'hekko'

class A():
    def __init__(self):
        print '__init__'
        self.value = 10

    def run(self):
        print 'run'
        print 'befor change: ', self.value
        sd.sender.connect('uKi_signal', self.end)
        self.md = se.Modul()
        self.md.run()
        print 'after change: ', self.value

    def end(self, object):
        self.value = 100
        print self.value
        sd.sender.emit('uKi_signal')

if __name__ == '__main__':
    a = A()
    a.run()
