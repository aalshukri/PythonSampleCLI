import sys
import logging
import argparse

from classmodule import MyClass
from funcmodule import my_function

import core


def main():
	print("Main")
	
	init() 
	logging.debug('Main')	
	
	print(sys.argv[1:])

	# function
	my_function('hello world')
	
	# class
	my_object = MyClass('TestName')
	my_object.say_name()	
	
	# core
	print(core.get_hmm())
	core.hmm()
	
def init():
	""" init """
	
	#
	# Command line arguments
	cmdparser = argparse.ArgumentParser()

	# Debug
	cmdparser.add_argument('-d', '--debug', dest='debug', action='store_true')
	cmdparser.add_argument('debugfile', nargs='?', default=None)

	# add option to have an argument for debug output to log file
	args = cmdparser.parse_args()
	
	if args.debug: 	
		if args.debugfile: logging.basicConfig(filename=args.debugfile,level=logging.DEBUG)  # --- log to file
		logging.basicConfig(level=logging.DEBUG)			  		     # --- log to screen
	else: logging.basicConfig(level=logging.WARNING) 					     # --- turn off debug	
		

#/init()	
	
if __name__ == '__main__':
	main()
