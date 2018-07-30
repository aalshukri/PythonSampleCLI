from ParentClass import Parent
import logging
class AnotherChild(Parent):
		
	def main(self):
		logging.debug('AnotherChild Main')
		self.firstAction()
		self.secondAction()
		self.thirdAction()
		self.secondAction()
		self.firstAction()
		self.firstAction()
		self.secondAction()
		self.thirdAction()
		self.secondAction()
		self.firstAction()
