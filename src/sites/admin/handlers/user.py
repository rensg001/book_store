#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.errors import ErrorEnum, ERROR_MAP
from service.user import UserService
from service.user_info import AdminLoginInfo
from sites.admin.forms.user import LoginForm
from sites.admin.handlers.handler import AdminRequestHandler
from tornado.options import options


class LoginHandler(AdminRequestHandler):
    def get(self):
        self.clear_all_cookies()
        return self.render("/user/login.html")

    def post(self):
        form = LoginForm(self.request.arguments)
        if not form.validate():
            return self.write_error_msg(ErrorEnum.argument_error.value,
                                        form.first_error)
        admin_login_info = AdminLoginInfo(login_id=form.login_id.data,
                                          password=form.password.data)
        admin_id = UserService().admin_login(admin_login_info)
        if admin_id < 0:
            error_code = admin_id
            return self.write_error_msg(error_code, ERROR_MAP.get(error_code))

        self.set_secure_cookie(name=options.USER_COOKIE_NAME,
                               value="{}".format(admin_id),
                               expires_days=None)
        return self.write_data({"next": form.next.data})


class LogoutHandler(AdminRequestHandler):
    def get(self):
        self.clear_all_cookies()
        return self.redirect(self.reverse_url(name="login"))
        # return self.write_success()
