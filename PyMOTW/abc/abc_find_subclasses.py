#!/usr/bin/python
#!-*-encoding=utf-8-*-

import abc
from abc_base import PluginBase
import abc_register
import abc_subclass

for sc in PluginBase.__subclasses__():
	print sc.__name__