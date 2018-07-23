import sys
import logging
import argparse
	
from classmodule import MyClass
from funcmodule import my_function

def main(): 
	init() 
	logging.debug('Main')

	# function
	my_function('hello world')
	
	# class
	my_object = MyClass('TestName')
	my_object.say_name()
#/main()
	
def init():
	""" init """
	
	#
	# Command line arguments
	#
	cmdparser = argparse.ArgumentParser()
	cmdparser.add_argument("-d", "--debug", help="debug output", required=False)
	
	args = cmdparser.parse_args()
	
	if args.debug: 	
		#logging.basicConfig(filename='example.log',level=logging.DEBUG)# --- log to file
		logging.basicConfig(level=logging.DEBUG)			  			# --- log to screen
	else: logging.basicConfig(level=logging.WARNING) # --- turn off debug logging		
		
#/init()

	
if __name__ == '__main__':
	main()