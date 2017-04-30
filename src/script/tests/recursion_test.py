#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def f(n, total):
    if n == 1:
        return total
    return f(n - 1, n * total)


def han_no(num, a, b, c):
    if num == 1:
        print("%s->%s" % (a, c))
    else:
        han_no(num - 1, a, c, b)
        print("%s->%s" % (a, c))

        han_no(num - 1, b, a, c)

han_no(3, "A", "B", "C")
