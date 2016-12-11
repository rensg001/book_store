#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.errors import ErrorEnum
from service.book import BookService
from service.book_info import BookBasicInfo
from sites.admin.forms.book import BookForm
from sites.admin.handlers.handler import AdminRequestHandler
from tornado.web import authenticated


class BookHandler(AdminRequestHandler):
    @authenticated
    def get(self):
        return self.render("/admin/book.html")

    @authenticated
    def post(self):
        form = BookForm(self.request.arguments)
        if not form.validate():
            return self.write_error_msg(ErrorEnum.argument_error.value,
                                        form.first_error)

        book_basic_info = BookBasicInfo(book_id=0,
                                        name=form.name.data,
                                        blurb=form.blurb.data,
                                        cover=form.cover.data)
        BookService().create(book_basic_info)
        return self.write_success()
