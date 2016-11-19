#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.www.handlers.handler import BaseRequestHandler
from tornado.web import RequestHandler


class LoginHandler(BaseRequestHandler):
    def get(self):
        self.render("login/login.html")