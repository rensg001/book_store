#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class ResultBase(dict):
    def __init__(self, code, success, *args, **kwargs):
        if not isinstance(code, int):
            raise ValueError("argument code must be type of int.")
        if not isinstance(success, bool):
            raise ValueError("argument success must be type of bool.")
        kwargs.update(code=code)
        kwargs.update(success=success)
        super(ResultBase, self).__init__(*args, **kwargs)


class MessageResult(dict):
    def __init__(self, message="", *args, **kwargs):
        if not isinstance(message, str):
            raise ValueError("argument data must be type of str.")

        kwargs.update(message=message)

        super(MessageResult, self).__init__(*args, **kwargs)


class SuccessMSGResult(MessageResult):
    def __init__(self, *args, **kwargs):
        kwargs.update(code=0)
        kwargs.update(success=True)
        super(SuccessMSGResult, self).__init__(*args, **kwargs)


class DataResult(dict):
    def __init__(self, data, *args, **kwargs):
        if not isinstance(data, dict):
            raise ValueError("argument data must be type of dict.")

        kwargs.update(data=data)
        super(DataResult, self).__init__(*args, **kwargs)