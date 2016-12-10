#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime


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
