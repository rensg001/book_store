#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import json
import tornado.web


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("/other/about.html")


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_argument("user_name", None)
        print(user_name)
        context = dict(check=True)
        if user_name is not None and user_name != "test":
            context["check"] = False
        return self.render("/test.html", **context)

    def post(self):
        args = self.get_argument("name")
        self.write(json.dumps({"message": args, "success": False}))
        self.finish()
