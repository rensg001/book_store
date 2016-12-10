#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.admin.handlers.handler import AdminRequestHandler
from tornado.web import authenticated


class BookHandler(AdminRequestHandler):

    @authenticated
    def get(self):
        return self.render("/admin/book.html")
