#!/usr/bin/python

import gobject
import signal_def as sd

class Modul():
    def __init__(self):
        print '__init__ Modul'

    def run(self):
        print 'modual run and sender signal'
        sd.sender.emit('uKi_signal')
        print 'modual run end'
