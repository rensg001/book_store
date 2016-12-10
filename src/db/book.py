#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from db.base import book_store_db
from db.book_model import Book
from service.book_info import BookInfo


class BookRepository(object):
    def create(self, book_info: BookInfo):
        with book_store_db.session as session:
            book = Book(name=book_info.name,
                        blurb=book_info.blurb,
                        cover=book_info.cover,
                        is_valid=book_info.is_valid,
                        update_time=book_info.update_time,
                        create_tiem=book_info.create_time)
            session.add(book)
            session.commit()
            book_id = book.book_id
        return book_id
