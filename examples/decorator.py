#!/usr/bin/python

#decorator

class MyClass:


	@classmethod
	def say_classmethod(self):
		print 'classmethod'

	@property
	def say_property(self):
		print 'property'

	@staticmethod
	def say_staticmethod():
		print 'staticmethod'


def compose_greet_func():
	def get_message(name):
		return 'Hello there'

	return get_message

greet = compose_greet_func
print greet()