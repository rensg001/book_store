#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import tornado.web


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("/other/about.html")


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("/test.html")