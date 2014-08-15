#!-*- coding=utf-8 -*-
import logging
import sys

class NSLogger(object):
	log_modules = set()
	log_level = logging.DEBUG


	@staticmethod
	def get_logger(moduleName):
		if moduleName in NSLogger.log_modules:
			return logging.getLogger(moduleName)
		logger = logging.getLogger(moduleName)
		logger.setLevel(logging.DEBUG)
		
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		

		formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(message)s')
		ch.setFormatter(formatter)

		logger.addHandler(ch)

		NSLogger.log_modules.add(moduleName)
		return logger



