# -*- coding: utf-8 -*-
#
# © 2016 Krux Digital, Inc.
#
# Standard libraries
#

from __future__ import absolute_import
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
