#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import tornado.ioloop
import tornado.web
import os
import jinja2

from sites.www.routes import handlers
from tornado_jinja2 import Jinja2Loader



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path), autoescape=False)
    jinja2_loader = Jinja2Loader(jinja2_env)

    settings = {
        "debug": True,
        "login_url": "/",
        # "template_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
        "static_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
        "template_loader": jinja2_loader
    }
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8300)
    tornado.ioloop.IOLoop.current().start()