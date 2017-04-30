#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pickle

class MyClass(object):
    def __init__(self):
        self.name = "fsdfsdf"

    def __reduce__(self):
        raise NotImplemented()


if __name__ == "__main__":
    print(pickle.dumps(MyClass()))