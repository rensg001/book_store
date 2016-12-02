#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class UserInfoV(object):
    def __init__(self,
                 user_id,
                 login_id,
                 password,
                 gender,
                 mobile,
                 name,
                 nickname,
                 birthday,
                 address):
        self.user_id = user_id
        self.login_id = login_id
        self.password = password
        self.gender = gender
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.address = address


class UserInfoM(object):
    def __init__(self,
                 user_id,
                 login_id,
                 password,
                 salt,
                 retry,
                 first_login,
                 last_login,
                 update_time,
                 create_time,
                 is_valid,
                 gender,
                 mobile,
                 name,
                 nickname,
                 birthday,
                 address):
        self.user_id = user_id
        self.login_id = login_id
        self.password = password
        self.salt = salt
        self.retry = retry
        self.first_login = first_login
        self.last_login = last_login
        self.update_time = update_time
        self.create_time = create_time
        self.is_valid = is_valid
        self.gender = gender
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.address = address