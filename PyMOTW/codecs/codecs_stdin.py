#!/usr/bin/python

import codecs
import locale
import sys

# Configure locale from the user's environment settings.
locale.setlocale(locale.LC_ALL, '')

# Wrap stdin with an encoding-aware reader
lang, encoding = locale.getdefaultlocale()
sys.stdin = codecs.getwriter(encoding)(sys.stdin)

print 'From stdin: ', repr(sys.stdin.read())
