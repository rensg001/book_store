#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class UndefinedError(Exception):
    def __init__(self, code: int, *args):
        super(UndefinedError, self).__init__(*args)
        self.code = code
