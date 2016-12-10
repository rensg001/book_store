#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
图书模型
"""

from db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class Book(Base):
    __table_name = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    blurb = Column(String(512), nullable=True)
    cover = Column(String(128), nullable=False)
    is_valid = Column(Boolean, nullable=False)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
