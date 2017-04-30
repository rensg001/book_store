#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from enum import Enum


class MyMeta(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return {"heheda": True}

    def __new__(metacls, class_name, bases, class_dict):
        my_class = super().__new__(metacls, class_name, bases, class_dict)
        return my_class

    def __init__(cls, class_name, bases, class_dict):
        print("meta __init__ called.")

    def __call__(cls, value):
        print("meta class __call__ with value: %s" % value)
        return super().__call__(value)

    def hehe(cls):
        print("meta hehe")


class MyClass(object, metaclass=MyMeta):
    def __new__(cls, value):
        print("my_class __new__ called.")

if __name__ == "__main__":
    m = MyClass(1)
    MyClass.hehe()