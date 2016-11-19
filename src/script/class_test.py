#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import tornado.web
import tornado.log
import logging

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


class BaseRequestHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("heheda.")
        self.get_action()

class MyHandler(BaseRequestHandler):
    def get_action(self):
        logging.info("handler a get request.")


def main():
    tornado.log.enable_pretty_logging()
    settings = {"debug": True}
    app = tornado.web.Application(handlers=[(r"/", MyHandler)],
                                  **settings)

    http_server = HTTPServer(app)
    http_server.listen(8888)
    logging.info("start server1.")
    IOLoop().current().start()

if __name__ == "__main__":
    main()