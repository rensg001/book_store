#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from awesome.form import BaseForm
from wtforms.fields import StringField
from wtforms.validators import InputRequired


class LoginForm(BaseForm):
    login_id = StringField(validators=[InputRequired(message="登陆ID不能为空")])
    password = StringField(validators=[InputRequired(message="密码不能为空")])
    next = StringField()
