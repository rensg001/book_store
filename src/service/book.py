#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime

from awesome.utils.pagination import Pagination
from db.book import BookRepository
from service.book_info import BookBasicInfo, BookInfo


class BookService(object):
    def __init__(self):
        self.book_repository = BookRepository()

    def create(self, book_basic_info: BookBasicInfo):
        now = datetime.now()
        book_info = BookInfo(book_id=0,
                             name=book_basic_info.name,
                             blurb=book_basic_info.blurb,
                             cover=book_basic_info.cover,
                             is_valid=True,
                             update_time=now,
                             create_time=now)
        return self.book_repository.create(book_info)

    def get_list(self, page, page_size, name=None):
        paging = Pagination(page, page_size)
        book_list, total = self.book_repository.get_list(paging.start, paging.page_size, name)
        total_page = total // page_size + (1 if total % page_size else 0)
        return book_list, total_page
