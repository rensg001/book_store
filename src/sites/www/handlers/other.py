#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import json
import logging
import tornado.web


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("/other/about.html")


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("/test.html")

    def post(self):
        args = self.get_argument("name")
        self.write(json.dumps({"message": args, "success": False}))
        self.finish()
