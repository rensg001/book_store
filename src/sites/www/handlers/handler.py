#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import urllib.parse

from awesome.handler import BaseRequestHandler
from tornado.options import options
from service.user import UserService


class UserRequestHandler(BaseRequestHandler):

    @staticmethod
    def upload_url(path):
        return urllib.parse.urljoin(options.FILE_UPLOAD_PREFIX, path)

    def get_current_user(self):
        user_id = self.get_secure_cookie(options.USER_COOKIE_NAME)
        if user_id:
            user_id = user_id.decode("utf8")
            user_id = int(user_id)
        if user_id is None:
            user_id = 0
        user = UserService().get_profile_by_id(user_id)
        return user

    def get_template_namespace(self):
        namespace = super(UserRequestHandler, self).get_template_namespace()
        namespace.update(user=self.current_user)
        namespace.update(upload_url=self.upload_url)
        return namespace
