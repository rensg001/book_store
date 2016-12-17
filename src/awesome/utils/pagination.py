#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
分页工具
"""


class Pagination(object):
    def __init__(self, page, page_size):
        self.page = page
        self.page_size = page_size
        self._start = None

        self._start = (page - 1) * page_size

    @property
    def start(self):
        return self._start
