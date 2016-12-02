#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import tornado.ioloop
import tornado.web
import tornado.options
import os
import jinja2
from awesome.utils.readconfig import read_config_file
from tornado_jinja2 import Jinja2Loader


def make_app():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(cur_dir, "app.conf")
    template_path = os.path.join(cur_dir, "templates")
    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path), autoescape=False)
    jinja2_loader = Jinja2Loader(jinja2_env)

    settings = {
        "debug": True,
        "login_url": "/",
        "static_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
        "template_loader": jinja2_loader
    }
    # 读取应用配置
    read_config_file(config_path)
    from sites.www.routes import handlers
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8300)
    tornado.ioloop.IOLoop.current().start()