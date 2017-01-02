#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from db.base import book_store_db
from db.book_model import Book, BookDetail
from service.book_info import BookInfo, BookDetailInfo
from sqlalchemy.sql.functions import count


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

    def create_detail(self, book_detail_info: BookDetailInfo):
        with book_store_db.session as session:
            book_detail = BookDetail(book_id=book_detail_info.book_id,
                                     author=book_detail_info.author,
                                     price=book_detail_info.price,
                                     editor_blurb=book_detail_info.editor_blurb,
                                     author_blurb=book_detail_info.author_blurb,
                                     content_blurb=book_detail_info.content_blurb,
                                     catalog=book_detail_info.catalog,
                                     preface=book_detail_info.preface,
                                     publish=book_detail_info.publish,
                                     isbn=book_detail_info.isbn,
                                     edition=book_detail_info.edition,
                                     language=book_detail_info.language,
                                     page_num=book_detail_info.page_num,
                                     word_num=book_detail_info.word_num,
                                     pub_date=book_detail_info.pub_date,
                                     update_time=book_detail_info.update_time,
                                     create_time=book_detail_info.create_time)
            session.add(book_detail)
            session.commit()

    def get_list(self, start, page_size, name):
        with book_store_db.session as session:
            total = session.query(count(Book.book_id)) \
                .filter(Book.is_valid) \
                .filter(Book.name == name if name else True) \
                .scalar()
            books = session.query(Book) \
                .filter(Book.is_valid) \
                .filter(Book.name == name if name else True) \
                .offset(start) \
                .limit(page_size) \
                .all()
            book_list = []
            for book in books:
                book_list.append(BookInfo(book_id=book.book_id,
                                          name=book.name,
                                          blurb=book.blurb,
                                          cover=book.cover,
                                          is_valid=book.is_valid,
                                          update_time=book.update_time,
                                          create_time=book.create_time))
        return book_list, total

    def get_one(self, book_id) -> BookDetailInfo:
        with book_store_db.session as session:
            book_detail = session.query(BookDetail).get(book_id)

        book_detail_info = BookDetailInfo(book_id=book_detail.book_id,
                                          author=book_detail.author,
                                          price=book_detail.price,
                                          editor_blurb=book_detail.editor_blurb,
                                          author_blurb=book_detail.author_blurb,
                                          content_blurb=book_detail.content_blurb,
                                          catalog=book_detail.catalog,
                                          preface=book_detail.preface,
                                          publish=book_detail.publish,
                                          isbn=book_detail.isbn,
                                          edition=book_detail.edition,
                                          language=book_detail.language,
                                          page_num=book_detail.page_num,
                                          word_num=book_detail.word_num,
                                          pub_date=book_detail.pub_date,
                                          update_time=book_detail.update_time,
                                          create_time=book_detail.create_time)
        return book_detail_info
