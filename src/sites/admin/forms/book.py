#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


from awesome.form import BaseForm
from wtforms.fields import StringField, DecimalField, DateField
from wtforms.validators import InputRequired, Length


class BookForm(BaseForm):
    name = StringField(validators=[InputRequired(message="书名不能为空"), Length(max=32, message="书名不能超过32个字符")])
    blurb = StringField(validators=[Length(max=512, message="简介不能超过512个字符")])
    cover = StringField(validators=[InputRequired(message="封面不能为空")])


class BookDetailForm(BaseForm):
    book_id = StringField()
    author = StringField(validators=[InputRequired(message="作者不能为空"), Length(max=32, message="作者姓名不能超过32个字符")])
    price = DecimalField(validators=[InputRequired(message="价格不能为空")])
    editor_blurb = StringField()
    author_blurb = StringField()
    content_blurb = StringField()
    catalog = StringField()
    preface = StringField()
    publish = StringField(validators=[InputRequired(message="出版社不能为空"), Length(max=64, message="出版社名称不能超过64个字符")])
    isbn = StringField(validators=[InputRequired(message="ISBN码不能为空"), Length(max=64, message="ISBN码不能超过64个字符")])
    edition = StringField(validators=[InputRequired(message="版次不能为空")])
    language = StringField(validators=[InputRequired(message="语言不能为空"), Length(max=32, message="语言不能超过32个字符")])
    page_num = StringField(validators=[InputRequired(message="页数不能为空")])
    word_num = StringField(validators=[InputRequired(message="字数不能为空")])
    pub_date = DateField(validators=[InputRequired(message="发行日期不能为空")])
