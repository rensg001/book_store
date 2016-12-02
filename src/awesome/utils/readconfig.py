#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.escape import native_str
from tornado.util import exec_in
from tornado.options import options, define


def read_config_file(path):
    config = {}
    with open(path, 'rb') as f:
        exec_in(native_str(f.read()), config, config)
    for name in config:
        if name not in options._options and not name.startswith("_"):
            define(name)
            normalized = options._normalize_name(name)
            options._options[normalized]._value = config[name]