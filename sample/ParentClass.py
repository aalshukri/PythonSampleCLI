import logging
class Parent():
	def __init__(self,name):
		""" Constructor """
		self.actionCount=0
		self.name=name
		pass
		
	def firstAction(self):
		self.actionCount+=1
		logging.debug('FirstAction ['+self.name+'] * '+str(self.actionCount)+'.')

	def secondAction(self):
		self.actionCount+=1
		logging.debug('secondAction ['+self.name+'] * '+str(self.actionCount)+'.')

	def thirdAction(self):
		self.actionCount+=1
		logging.debug('thirdAction ['+self.name+'] * '+str(self.actionCount)+'.')
