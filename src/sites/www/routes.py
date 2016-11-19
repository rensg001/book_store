#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.web import URLSpec as url
from sites.www.handlers import login, test

handlers = [
    url(r"/", login.LoginHandler),
    url(r"/test", test.TestHandler)
]