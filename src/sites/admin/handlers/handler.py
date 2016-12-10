#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.handler import BaseRequestHandler
from service.user import UserService
from tornado.options import options


class AdminRequestHandler(BaseRequestHandler):
    def get_current_user(self):
        admin_id = self.get_secure_cookie(options.USER_COOKIE_NAME)
        if not admin_id:
            return None
        admin_id = int(admin_id.decode("utf8"))
        admin = UserService().get_admin_by_id(admin_id)
        return admin
