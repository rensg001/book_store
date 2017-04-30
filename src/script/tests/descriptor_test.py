#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from functools import partial


class MyDescriptor(object):
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner):
        func = partial(self._func, instance)
        return func

    def __set__(self, instance, value):
        pass


class Base(object):
    pass


class MyClass(Base):

    def __new__(cls, bind=None):
        ins = super().__new__(cls)
        if bind:
            setattr(cls, bind.__name__, partial(bind, ins))
        return ins

    def __init__(self, bind=None):
        self.name = "my class."
        self.foo = 1


class MyClass2(Base):

    def __new__(cls):
        print("my class 2 __new__ called.")


def foo(self):
    print(self.name)


if __name__ == "__main__":
    setattr(MyClass, "foo", MyDescriptor(foo))
    m = MyClass()
    m.foo()