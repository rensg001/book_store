#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from wtforms_tornado import Form


class BaseForm(Form):
    @property
    def first_error(self):
        if self.errors:
            for field, errors in self.errors.items():
                return errors[0]
        return None