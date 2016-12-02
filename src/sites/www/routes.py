#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.web import URLSpec as url
from sites.www.handlers import user, main, other

handlers = [
    url(r"/", main.MainHandler),
    url(r"/signup", user.SignUpHandler, name="signup"),
    url(r"/login", user.LoginHandler, name="login"),
    url(r"/about", other.AboutHandler, name="about"),
    url(r"/test", other.TestHandler)
]