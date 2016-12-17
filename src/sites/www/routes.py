#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.web import URLSpec as url
from sites.www.handlers import user, main, other
from awesome.handler import FileUploadHandler

handlers = [
    url(r"/", main.MainHandler),
    url(r"/book/list", main.MainListHandler, name="book_list"),
    url(r"/signup", user.SignUpHandler, name="signup"),
    url(r"/login", user.LoginHandler, name="login"),
    url(r"/logout", user.LogoutHandler, name="logout"),
    url(r"/about", other.AboutHandler, name="about"),
    url(r"/file/upload", FileUploadHandler, name="file_upload"),
    url(r"/test", other.TestHandler)
]
