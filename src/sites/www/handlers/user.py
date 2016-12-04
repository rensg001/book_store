#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.errors import ErrorEnum
from awesome.handler import MessageResult, SuccessMSGResult
from service.user import UserService
from service.user_info import UserSignupInfo, UserLoginInfo
from sites.www.forms.user import UserSignUpForm, UserLoginForm
from sites.www.handlers.handler import BaseRequestHandler
from tornado.options import options


class LoginHandler(BaseRequestHandler):
    def post(self):
        form = UserLoginForm(self.request.arguments)
        if not form.validate():
            return self.write_error_msg(code=ErrorEnum.argument_error.value,
                                        msg=form.first_error)
        self.clear_all_cookies()
        login_info = UserLoginInfo(login_id=form.login_id.data,
                                   password=form.password.data)
        login_ret = UserService().login(login_info)
        if login_ret < 0:
            return self.write_error_msg(login_ret)
        self.set_secure_cookie(name=options.USER_COOKIE_NAME,
                               value="{0}".format(login_ret),
                               expires_days=None)
        return self.write_success()


class LogoutHandler(BaseRequestHandler):
    def get(self):
        self.clear_all_cookies()
        return self.write_success()


class SignUpHandler(BaseRequestHandler):
    def post(self):
        form = UserSignUpForm(self.request.arguments)
        if not form.validate():
            return self.write_error_msg(code=ErrorEnum.argument_error.value,
                                        msg=form.first_error)
        self.clear_all_cookies()
        user_info_v = UserSignupInfo(user_id=0,
                                     login_id=form.login_id.data,
                                     password=form.password.data,
                                     gender=form.gender.data,
                                     mobile=form.mobile.data,
                                     name=form.name.data,
                                     nickname=form.nickname.data,
                                     birthday=form.birthday.data,
                                     address=form.address.data,
                                     avatar=form.avatar.data)
        user_id = UserService().create(user_info_v)
        self.set_secure_cookie(name=options.USER_COOKIE_NAME,
                               value="{0}".format(user_id),
                               expires_days=None)
        return self.write(SuccessMSGResult())
