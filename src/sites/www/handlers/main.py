#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from service.book import BookService
from sites.www.handlers.handler import UserRequestHandler


class MainHandler(UserRequestHandler):

    def get(self):
        book_list = BookService().get_book_list()
        self.render("/index.html", book_list=book_list)
