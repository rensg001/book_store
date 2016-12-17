#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from service.book import BookService
from sites.www.handlers.handler import UserRequestHandler


class MainHandler(UserRequestHandler):
    def get(self):
        self.render("/index.html")


class MainListHandler(UserRequestHandler):
    def get(self):
        page = self.get_argument("page")
        page_size = self.get_argument("page_size")
        name = self.get_argument("name", None)
        page = int(page)
        page_size = int(page_size)
        book_list, total_page = BookService().get_list(page, page_size, name)
        for book in book_list:
            book.cover = self.upload_url(book.cover)
        self.write_data(data=dict(page=page,
                                  total_page=total_page,
                                  list=book_list))