#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class Base(object):
    def do_something(self, info):
        pass


class Papa(Base):
    def do_something(self, info):
        print("papa do %s." % info)
        super(Papa, self).do_something(info)


class Mama(Base):
    def do_something(self, info):
        print("mama do %s." % info)
        super(Mama, self).do_something(info)


class Me(Papa, Mama):
    def do_something(self, info):
        print("i do %s." % info)
        super(Me, self).do_something(info)

if __name__ == "__main__":
    me = Me()
    me.do_something("work")
