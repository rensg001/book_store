#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class Shape(object):
    def __init__(self, color):
        """

        :param Color color:
        """
        self._color = color

    def foo(self):
        raise NotImplementedError()


class Circle(Shape):
    def foo(self):
        print("%s circle" % self._color.foo())


class Color(object):
    def foo(self):
        raise NotImplementedError()


class Red(Color):
    def foo(self):
        return "red"


class Blue(Color):
    def foo(self):
        return "blue"


if __name__ == "__main__":
    circle = Circle(Blue())
    circle.foo()
