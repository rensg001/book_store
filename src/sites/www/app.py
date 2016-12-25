#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import logging

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.log
import jinja2

from awesome.utils.readconfig import read_config_file, read_log_config
from tornado_jinja2 import Jinja2Loader


def make_app(cur_dir):
    tornado.options.parse_command_line()
    config_path = os.path.join(cur_dir, "app.conf")
    template_path = os.path.join(cur_dir, "templates")

    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path), autoescape=False)
    jinja2_loader = Jinja2Loader(jinja2_env)

    # 读取应用配置
    logger.info("read config.")
    read_config_file(config_path)
    settings = {
        "debug": True,
        "login_url": "/",
        "static_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
        "template_loader": jinja2_loader,
        "cookie_secret": tornado.options.options.COOKIE_SECRETE
    }
    from sites.www.routes import handlers
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    # 读取logging配置
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    log_config_path = os.path.join(cur_dir, "logconfig.json")
    read_log_config(path=log_config_path)

    logger = logging.getLogger("sites.www")
    logger.info("server is starting.")
    app = make_app(cur_dir)
    app.listen(8300)
    logger.info("server started.")
    tornado.ioloop.IOLoop.current().start()
