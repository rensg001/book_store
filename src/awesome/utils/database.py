#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class Convert(object):
    """
    转换数据行到目标类型
    """

    def __init__(self, row, target):
        """
        :param row: 模型对象
        :param target: 目标类
        """
        self.row = row
        self.target = target
        self._data = {}

    def _get_dict(self):
        row_dict = dict(self.row.__dict__)
        removed_key = []
        for key in row_dict:
            if key.startswith("_"):
                removed_key.append(key)
        for rmv_key in removed_key:
            row_dict.pop(rmv_key, None)
        self._data = row_dict

    def convert(self):
        if not self.row:
            return self.row

        self._get_dict()
        return self.target(**self._data)


class ConvertList(object):
    """
    转换多行数据到目标类型
    """

    def __init__(self, rows, target):
        self.rows = rows
        self.target = target
        self._dict_list = []
        self._data = []

    def _get_dict(self):
        for row in self.rows:
            row_dict = dict(row.__dict__)
            removed_key = []
            for key in row_dict:
                if key.startswith("_"):
                    removed_key.append(key)
            for rmv_key in removed_key:
                row_dict.pop(rmv_key, None)
            self._dict_list.append(row_dict)

    def convert(self):
        if not self.rows:
            return self.rows

        for item in self._dict_list:
            self._data.append(self.target(**item))
        return self._data
