#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.web import URLSpec as url
from sites.admin.handlers import user, main, book
from awesome.handler import FileUploadHandler

handlers = [
    url(r"/", main.MainHandler, name="main"),
    url(r"/login", user.LoginHandler, name="login"),
    url(r"/logout", user.LogoutHandler, name="logout"),
    url(r"/file/upload", FileUploadHandler, name="file_upload"),

    url(r"/admin/book", book.BookHandler, name="admin_book"),
    url(r"/admin/book/detail", book.BookDetailHandler, name="admin_book_detail")
]
