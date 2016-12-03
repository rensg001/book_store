#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.handler import BaseRequestHandler
from tornado.options import options
from service.user import UserService


class UserRequestHandler(BaseRequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie(options.USER_COOKIE_NAME)
        user = UserService().get_by_id(user_id)
        return user
