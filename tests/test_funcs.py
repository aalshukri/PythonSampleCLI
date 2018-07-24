# -*- coding: utf-8 -*-

import context
import sample.funcmodule

import unittest

# if use
# from sample import funcmodule
# then can use
#  funcmodule.my_function("text")

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_myfunction(self):
		print(sample.funcmodule.my_function("text"))		
		assert True


if __name__ == '__main__':
    unittest.main()