#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


from awesome.form import BaseForm
from wtforms.fields import StringField
from wtforms.validators import InputRequired, Length


class BookForm(BaseForm):
    name = StringField(validators=[InputRequired(message="书名不能为空"), Length(max=32, message="书名不能超过32个字符")])
    blurb = StringField(validators=[Length(max=512, message="简介不能超过512个字符")])
    cover = StringField(validators=[InputRequired(message="封面不能为空")])
