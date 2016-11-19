#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.www.handlers.handler import BaseRequestHandler


class TestHandler(BaseRequestHandler):
    def get(self):
        return self.render("/test.html")