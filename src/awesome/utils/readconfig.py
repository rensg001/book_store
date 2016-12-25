#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import logging.config
import json

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


def read_log_config(path="logconfig.json", level=logging.INFO):
    """读取logging配置"""
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=level)
