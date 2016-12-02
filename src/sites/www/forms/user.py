#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from wtforms.fields import StringField, DateField
from wtforms.validators import InputRequired, Length
from awesome.form import BaseForm


class UserSignUpForm(BaseForm):
    login_id = StringField(validators=[InputRequired(message="登陆ID不能为空")])
    password = StringField(validators=[InputRequired(message="密码不能为空")])
    gender = StringField(validators=[InputRequired(message="性别不能为空")])
    birthday = DateField(validators=[InputRequired(message="出生日期不能为空")])
    name = StringField(validators=[InputRequired(message="姓名不能为空"), Length(max=20, message="姓名不能超过20个字符")])
    nickname = StringField(validators=[InputRequired(message="昵称不能为空"), Length(max=20, message="昵称不能超过20个字符")])
    mobile = StringField(validators=[InputRequired(message="手机号不能为空"), Length(max=20, message="手机号不能超过20个字符")])
    address = StringField(validators=[Length(max=256, message="地址不能超过256个字符")])
