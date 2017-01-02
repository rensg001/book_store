#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime, date


class BookInfo(object):
    def __init__(self,
                 book_id: int,
                 name: str,
                 blurb: str,
                 cover: str,
                 is_valid: bool,
                 update_time: datetime,
                 create_time: datetime
                 ):
        self.book_id = book_id
        self.name = name
        self.blurb = blurb
        self.cover = cover
        self.is_valid = is_valid
        self.update_time = update_time
        self.create_time = create_time


class BookBasicInfo(object):
    def __init__(self,
                 book_id: int,
                 name: str,
                 blurb: str,
                 cover: str):
        self.book_id = book_id
        self.name = name
        self.blurb = blurb
        self.cover = cover


class BookDetailInfo(object):
    def __init__(self,
                 book_id: int,
                 author: str,
                 price: str,
                 editor_blurb: str,
                 author_blurb: str,
                 content_blurb: str,
                 catalog: str,
                 preface: str,
                 publish: str,
                 isbn: str,
                 edition: int,
                 language: str,
                 page_num: int,
                 word_num: int,
                 pub_date: date,
                 update_time: datetime,
                 create_time: datetime):
        self.book_id = book_id
        self.author = author
        self.price = price
        self.editor_blurb = editor_blurb
        self.author_blurb = author_blurb
        self.content_blurb = content_blurb
        self.catalog = catalog
        self.preface = preface
        self.publish = publish
        self.isbn = isbn
        self.edition = edition
        self.language = language
        self.page_num = page_num
        self.word_num = word_num
        self.pub_date = pub_date
        self.update_time = update_time
        self.create_time = create_time