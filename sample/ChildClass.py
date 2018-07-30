from ParentClass import Parent
import logging
class Child(Parent):
		
	def main(self):
		logging.debug('Child Main')
		self.firstAction()
		self.secondAction()
		self.thirdAction()
		self.secondAction()
		self.firstAction()
