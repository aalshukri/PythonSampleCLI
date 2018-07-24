# -*- coding: utf-8 -*-

#from .context import sample

import context
#from context import sample
#from sample import classmodule

import sample.core

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_core(self):
        #self.assertIsNone(sample.hmm())
		self.assertIsNone(sample.core.hmm())


if __name__ == '__main__':
    unittest.main()
