# -*- coding: utf-8 -*-

import context
import sample.classmodule

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_myclass(self):				
		my_object = sample.classmodule.MyClass('TestName')
		my_object.say_name()
		assert True


if __name__ == '__main__':
    unittest.main()