#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from awesome.handler import MessageResult, SuccessMSGResult
from service.user import UserService
from service.user_info import UserInfoV
from sites.www.forms.user import UserSignUpForm
from sites.www.handlers.handler import BaseRequestHandler


class LoginHandler(BaseRequestHandler):
    def get(self):
        self.render("login/signin.html")


class SignUpHandler(BaseRequestHandler):
    def post(self):
        form = UserSignUpForm(self.request.arguments)
        if not form.validate():
            return self.write(MessageResult(message=form.first_error, code=-1, success=False))
        user_info_v = UserInfoV(user_id=0,
                                login_id=form.login_id.data,
                                password=form.password.data,
                                gender=form.gender.data,
                                mobile=form.mobile.data,
                                name=form.name.data,
                                nickname=form.nickname.data,
                                birthday=form.birthday.data,
                                address=form.address.data)
        UserService().create(user_info_v)
        return self.write(SuccessMSGResult())
