# -*- coding: utf-8 -*-

import context
import sample.helpers

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_helper_get_answer(self):				
		assert sample.helpers.get_answer()


if __name__ == '__main__':
    unittest.main()