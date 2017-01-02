#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.errors import ErrorEnum, ERROR_MAP
from service.book import BookService
from sites.www.handlers.handler import UserRequestHandler
from tornado.web import authenticated


class BookDetailHandler(UserRequestHandler):
    @authenticated
    def get(self, book_id):
        try:
            if book_id:
                book_id = int(book_id)
        except ValueError:
            return self.write_error_msg(ErrorEnum.argument_error.value,
                                        msg=ERROR_MAP.get(ErrorEnum.argument_error.value))
        book_info = BookService().get_one(book_id)
        return self.render("/book/detail.html", book_info=book_info)
