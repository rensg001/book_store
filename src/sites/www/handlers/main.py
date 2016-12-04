#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.www.handlers.handler import UserRequestHandler


class MainHandler(UserRequestHandler):
    def get(self):
        self.render("/index.html")