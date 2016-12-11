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
                        create_time=book_info.create_time)
            session.add(book)
            session.commit()
            book_id = book.book_id
        return book_id

    def get_book_list(self):
        with book_store_db.session as session:
            books = session.query(Book).all()
            book_list = []
            for book in books:
                book_list.append(BookInfo(book_id=book.book_id,
                                          name=book.name,
                                          blurb=book.blurb,
                                          cover=book.cover,
                                          is_valid=book.is_valid,
                                          update_time=book.update_time,
                                          create_time=book.create_time))
        return book_list