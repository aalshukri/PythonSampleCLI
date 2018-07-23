import logging
class MyClass():
	def __init__(self, name):
		""" Constructor """
		self.name = name
		
	def say_name(self):
		logging.debug('name is {}'.format(self.name))