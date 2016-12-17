#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import json
import os
import datetime

from awesome.errors import ERROR_MAP, ErrorEnum
from awesome.exceptions import UndefinedError
from awesome.utils.random_str import random_word
from tornado.options import options
from tornado.web import RequestHandler


class ResultBase(dict):
    def __init__(self, code, success, *args, **kwargs):
        if not isinstance(code, int):
            raise ValueError("argument code must be type of int.")
        if not isinstance(success, bool):
            raise ValueError("argument success must be type of bool.")
        kwargs.update(code=code)
        kwargs.update(success=success)
        super(ResultBase, self).__init__(*args, **kwargs)


class MessageResult(ResultBase):
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


class ErrorMSGResult(MessageResult):
    def __init__(self, *args, **kwargs):
        kwargs.update(success=False)
        super(MessageResult, self).__init__(*args, **kwargs)


class DataResult(dict):
    def __init__(self, data, code=0, success=True, *args, **kwargs):
        if not isinstance(data, dict):
            raise ValueError("argument data must be type of dict.")

        kwargs.update(data=data)
        kwargs.update(code=code)
        kwargs.update(success=success)
        super(DataResult, self).__init__(*args, **kwargs)


class BaseRequestHandler(RequestHandler):
    def write_error_msg(self, code: int, msg=None):
        if not msg:
            error_msg = ERROR_MAP.get(code)
            if not error_msg:
                raise UndefinedError(code)
        else:
            error_msg = msg
        return self.write(ErrorMSGResult(message=error_msg, code=code))

    def write_success(self):
        self.write(SuccessMSGResult())

    def write_data(self, data):
        json_string = json.dumps(DataResult(data), cls=MyJSONEncoder)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json_string)


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime(format="%Y-%m-%d %H:%M:%S")
        elif isinstance(o, datetime.date):
            return o.strftime(format="%Y-%m-%d")
        elif hasattr(o, "__dict__"):
            return o.__dict__
        super(MyJSONEncoder, self).default(o)


class FileUploadHandler(BaseRequestHandler):
    def post(self):
        if not self.request.files:
            return self.write_error_msg(code=ErrorEnum.argument_error.value,
                                        msg="缺少文件参数")

        file = self.request.files["fileupload"][0]
        filename, file_extension = os.path.splitext(file["filename"])
        today = datetime.datetime.today()
        filename = random_word(20)
        relative_path = today.strftime("%Y/%m/%d")
        fullname = filename+file_extension
        path = os.path.join(options.FILE_UPLOAD_ROOT, relative_path)
        if not os.path.exists(path):
            os.makedirs(path)
        relative_path = os.path.join(relative_path, fullname)
        filepath = os.path.join(path, fullname)
        with open(filepath, mode="wb") as f:
            try:
                f.write(file["body"])
            except IOError:
                raise
        return self.write_data({"filepath": relative_path})
