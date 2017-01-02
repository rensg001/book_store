#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from enum import Enum


class ErrorEnum(Enum):
    argument_error = -1
    success = 0
    login_failure = -100001


ERROR_MAP = {
    ErrorEnum.login_failure.value: "用户名或密码错误",
    ErrorEnum.argument_error.value: "参数错误"
}
