#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""基于redis实现web会话管理"""
import uuid
import hashlib
import json

import redis

from tornado.web import gen_log

from redis import RedisError


class SessionError(Exception):
    """会话错误"""
    pass


class SessionIDError(SessionError):
    """错误的session id"""
    pass


class SessionData(dict):
    """会话数据"""

    def __init__(self, session_id, **kwargs):
        self._session_id = session_id
        super(SessionData, self).__init__(**kwargs)

    @property
    def session_id(self):
        return self._session_id


class Session(SessionData):
    """会话"""

    def __init__(self, session_manager, handler):
        """初始化session

        :param session_manager:
        :type session_manager: `SessionManager`
        :param handler:
        :type handler: `tornado.web.RequestHandler`
        """

        self._session_manager = session_manager
        self._handler = handler

        session_id = self._handler.get_secure_cookie("session_id")
        self._session_id = session_id

        session_info = session_manager.get(session_id)
        self._session_info = session_info

        # 这里使用session manager返回的session id填充session data因为新建会话时无session id
        session_id = session_info.pop("session_id")
        super(Session, self).__init__(session_id, **session_info)

    def __setitem__(self, key, value):
        self._session_manager.set(self._session_id, key, value)
        super(Session, self).__setitem__(key, value)
        self._handler.set_secure_cookie(name="session_id", value=self.session_id, expires_days=None)


class SessionManager(object):
    """会话管理器"""

    def __init__(self, secret, options, timeout):
        self._secret = secret
        self._options = options
        self._timeout = timeout

        try:
            if "password" in options:
                self._redis = redis.StrictRedis(host=options["host"],
                                                port=options["port"],
                                                db=options["db"],
                                                password=options["password"])
            else:
                self._redis = redis.StrictRedis(host=options["host"],
                                                port=options["port"],
                                                db=options["db"])

        except RedisError:
            gen_log.error("Connect redis server error.", exec_info=True)
            raise

    def _fetch(self, session_id):
        try:
            raw_data = self._redis.get(session_id)
            if raw_data:
                self._redis.setex(session_id, self._timeout, raw_data)
                return json.loads(raw_data.decode("utf8"))
        except IOError:
            gen_log.error("Fetch session data error.", exec_info=True)
            raise
        else:
            return {}

    def get(self, session_id):
        if not session_id:
            session_id = self._generate_id()
        session_data = self._fetch(session_id)
        session_data["session_id"] = session_id
        return session_data

    def set(self, session_id, key, value):
        session_data = self.get(session_id)
        session_data.pop("session_id")
        session_data[key] = value
        raw_data = json.dumps(session_data)
        self._redis.setex(session_id, self._timeout, raw_data)

    def _generate_id(self):
        msg = self._secret + str(uuid.uuid4())
        return hashlib.sha256(msg.encode("utf8")).digest()
