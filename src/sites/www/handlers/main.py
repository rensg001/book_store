#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import logging

from service.book import BookService
from sites.www.handlers.handler import UserRequestHandler

logger = logging.getLogger(__name__)


class MainHandler(UserRequestHandler):
    def get(self):
        self.render("/index.html")


class MainListHandler(UserRequestHandler):
    def get(self):
        page = self.get_argument("page")
        page_size = self.get_argument("page_size")
        name = self.get_argument("name", None)
        page = int(page)
        page_size = int(page_size)
        logger.info("page:{page}, page_size:{page_size}, name:{name}".format(page=page, page_size=page_size, name=name if name else ""))
        logger.info("session username: %s" % self.session["username"])
        book_list, total_page = BookService().get_list(page, page_size, name)
        for book in book_list:
            book.cover = self.upload_url(book.cover)
        self.write_data(data=dict(page=page,
                                  total_page=total_page,
                                  list=book_list))
