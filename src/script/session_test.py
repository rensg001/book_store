#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import hashlib
import hmac
import uuid
import redis
import logging
import ujson
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.web

logging.basicConfig(level=logging.INFO)

class SessionData(dict):
    def __init__(self, sesison_id, hmac_key, **kwargs):
        self.session_id = sesison_id
        self.hmac_key = hmac_key
        super(SessionData, self).__init__(**kwargs)

class Session(SessionData):
    def __init__(self, session_manager, request_handler):
        self.session_manager = session_manager
        self.request_handler = request_handler
        try:
            current_session = session_manager.get(request_handler)
        except:
            current_session = session_manager.get()
        for key, value in current_session.items():
            self[key] = value
        super(Session, self).__init__(current_session.session_id, current_session.hmac_key)

    def save(self):
        self.session_manager.set(self.request_handler, self)


class InvalidSessionException(Exception):
    pass


class SessionManager(object):
    def __init__(self, secret, options, timeout):
        self.secret = secret
        self.options = options
        self.timeout = timeout
        self.redis = None
        try:
            if "pass" in options:
                self.redis = redis.StrictRedis(host=options["host"],
                                           port=options["port"],
                                           password=options["pass"])
            else:
                self.redis = redis.StrictRedis(host=options["host"],
                                               port=options["port"])
        except Exception as e:
            logging.info("connect to redis server failed.")
            raise e
    def _fetch(self, session_id):
        try:
            session_data = raw_data = self.redis.get(session_id)
            if raw_data:
                self.redis.setex(session_id, self.timeout, raw_data)
                session_data = ujson.loads(raw_data)
                return session_data
            else:
                return {}
        except IOError:
            return {}

    def get(self, request_handler=None):
        if not request_handler:
            session_id = None
            hmac_key = None
        else:
            session_id = request_handler.get_secure_cookie("session_id")
            hmac_key = request_handler.get_secure_cookie("verification")

        if not session_id:
            session_exist = False
            session_id = self._generate_id()
            hmac_key = self._generate_hmac(session_id)
        else:
            session_exist = True

        check_hamc = self._generate_hmac(session_id)
        if hmac_key != check_hamc:
            raise InvalidSessionException()

        session = SessionData(session_id, hmac_key)
        if session_exist:
            session_data = self._fetch(session_id)
            for key, value in session_data.items():
                session[key] = value
        return session

    def set(self, request_handler, session):
        request_handler.set_secure_cookie("session_id", session.session_id)
        request_handler.set_secure_cookie("verification", session.hmac_key)
        raw_data = ujson.dumps(dict(session.items()))
        self.redis.setex(session.session_id, self.timeout, raw_data)

    def _generate_id(self):
        msg = self.secret+str(uuid.uuid4())
        new_id = hashlib.sha256(msg.encode("utf8"))
        return new_id.digest()

    def _generate_hmac(self, session_id):
        return hmac.new(self.secret.encode("utf8"), session_id, hashlib.sha256).digest()

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.session = Session(SessionManager("mysecret",
                                              {
                                                  "host": "127.0.0.1",
                                                  "port": 6379,}, 180), self)

class TestHandler(BaseHandler):
    def get(self):
        self.session["id"] = 123
        self.write("set your id to %s" % self.session["id"])
        self.session.save()
        self.finish()


class OtherHandler(BaseHandler):
    def get(self):
        self.write("get your id %s" % self.session["id"])
        self.finish()

def main():
    handlers = [
        (r"/", TestHandler),
        (r"/other", OtherHandler)
    ]
    app = tornado.web.Application(handlers=handlers, Debug=True, cookie_secret="hdkjfhsk")
    server = HTTPServer(app)
    server.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()