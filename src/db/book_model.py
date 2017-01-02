#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
图书模型
"""

from db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, DECIMAL, Date


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    blurb = Column(String(512), nullable=True)
    cover = Column(String(128), nullable=False)
    is_valid = Column(Boolean, nullable=False)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)


class BookDetail(Base):
    __tablename__ = "book_detail"
    book_id = Column(Integer, primary_key=True)
    author = Column(String(32), nullable=False)
    price = Column(DECIMAL(5, 2), nullable=False)
    editor_blurb = Column(String(1024), nullable=True)
    author_blurb = Column(String(1024), nullable=True)
    content_blurb = Column(String(1024), nullable=True)
    catalog = Column(String(1024), nullable=True)
    preface = Column(String(1024), nullable=True)
    publish = Column(String(64), nullable=False)
    isbn = Column(String(64), nullable=False)
    edition = Column(Integer, nullable=False)
    language = Column(String(32), nullable=False)
    page_num = Column(Integer, nullable=False)
    word_num = Column(Integer, nullable=False)
    pub_date = Column(Date, nullable=False)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)


class BookComment(Base):
    __tablename__ = "book_comment"
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, nullable=False)
    comment = Column(String(256), nullable=False)
    is_valid = Column(Boolean, nullable=False)
    user_id = Column(Integer, nullable=False)
    nickname = Column(String(20), nullable=False)
    avatar = Column(String(128), nullable=False)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
