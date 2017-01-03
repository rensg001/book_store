#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import base64
import json
import ssl
import urllib.request, sys


class OcrVehicleApi(object):
    def __init__(self, host, path, file_path, app_key=None, app_secret=None, app_code=None,
                 ):
        self._app_key = app_key
        self._app_secret = app_secret
        self._app_code = app_code
        self._host = host
        self._path = path
        self._url = self._host + self._path
        self._body = {
            "inputs": [
                {
                    "image": {
                        "dataType": 50, "dataValue": ""
                    }
                }
            ]}
        self._data_value = self._body["inputs"][0]["image"]["dataValue"]
        self._body_json = self.get_body(file_path)
        self._ctx = ssl.create_default_context()
        self._ctx.check_hostname = False
        self._ctx.verify_mode = ssl.CERT_NONE

    def get_header(self):
        headers = {}
        headers.update(Authorization="APPCODE " + self._app_code)
        headers.update({"Content-Type": "application/json; charset=UTF-8"})
        return headers

    def get_body(self, file_path):
        with open(file_path, "rb") as f:
            content = f.read()
            content_b64 = base64.b64encode(content)
            self._data_value = content_b64
        return json.dumps(self._body)

    def make_request(self):
        headers = self.get_header()
        return urllib.request.Request(self._url,
                                      data=self._body_json.encode("utf8"),
                                      headers=headers)

    def do_request(self):
        request = self.make_request()
        resp = urllib.request.urlopen(request, context=self._ctx)
        content = resp.read()
        if content:
            print(content)

ocr_vehicle_api = OcrVehicleApi(
        host="https://dm-53.data.aliyun.com",
        path="/rest/160601/ocr/ocr_vehicle.json",
        file_path="/Users/renshangui/commitizen.json",
        app_code="12641a9e338c467db865c1453c76d8e1"
    )

ocr_vehicle_api.do_request()