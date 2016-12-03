#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import unittest
import mock

def foo(x):
    return x

class MyTestCase(unittest.TestCase):
    @mock.patch(__name__+".foo", autospec=True)
    def test_foo(self, mock_obj):
        mock_obj.return_value = 15
        ret = foo(11)
        self.assertEqual(ret, 15)

if __name__ == "__main__":
    unittest.main()