#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime

from awesome.errors import ErrorEnum
from service.book import BookService
from service.book_info import BookBasicInfo, BookDetailInfo
from sites.admin.forms.book import BookForm, BookDetailForm
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


class BookDetailHandler(AdminRequestHandler):
    @authenticated
    def get(self):
        book_id = self.get_argument("book_id", None)
        detail_info = None
        if book_id:
            detail_info = BookService().get_detail(book_id)

        return self.render("/admin/book/detail.html",
                           detail_info=detail_info)

    @authenticated
    def post(self):
        form = BookDetailForm(self.request.arguments)
        if not form.validate():
            return self.write_error_msg(ErrorEnum.argument_error.value,
                                        form.first_error)
        now = datetime.now()
        book_detail_info = BookDetailInfo(book_id=form.book_id.data,
                                          author=form.author.data,
                                          price=form.price.data,
                                          editor_blurb=form.editor_blurb.data,
                                          author_blurb=form.author_blurb.data,
                                          content_blurb=form.content_blurb.data,
                                          catalog=form.catalog.data,
                                          preface=form.preface.data,
                                          publish=form.publish.data,
                                          isbn=form.isbn.data,
                                          edition=form.edition.data,
                                          language=form.language.data,
                                          page_num=form.page_num.data,
                                          word_num=form.word_num.data,
                                          pub_date=form.pub_date.data,
                                          update_time=now,
                                          create_time=now)
        BookService().create_detail(book_detail_info)
        self.write_success()
