#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.web import URLSpec as url
from sites.www.handlers import login, main, other

handlers = [
    url(r"/", main.MainHandler),
    url(r"/login", login.LoginHandler),
    url(r"/about", other.AboutHandler),
    url(r"/test", other.TestHandler)
]