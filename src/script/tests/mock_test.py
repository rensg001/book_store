#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import unittest
import mock

from . import foo


def nimei():
    return foo.dump()


class Me(object):
    def __get__(self, ins, owner):
        if not ins:
            return self
        return "you call me?"


class T(object):
    me = Me()


class MyTestCase(unittest.TestCase):
    @mock.patch("script.foo.dump", autospec=True)
    def test_foo(self, dump_mock):
        dump_mock.return_value = 15
        ret = nimei()
        self.assertEqual(ret, 15)


def mydecorator(func):
    def wrapper():
        print("wrapper do.")
        func()

    return wrapper

def mydecorator_with_args(x):
    print(x)
    def mydecorator(func):
        def wrapper():
            print("wrapper do.")
            func()
        return wrapper
    return mydecorator

@mydecorator_with_args(123)
def fff():
    print("fff do.")

if __name__ == "__main__":
    # unittest.main()
    # t = T()
    # print(t.me)
    fff()
