#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class UserSignupInfo(object):
    def __init__(self,
                 user_id,
                 login_id,
                 password,
                 gender,
                 mobile,
                 name,
                 nickname,
                 birthday,
                 address,
                 avatar):
        self.user_id = user_id
        self.login_id = login_id
        self.password = password
        self.gender = gender
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.address = address
        self.avatar = avatar


class UserLoginInfo(object):
    def __init__(self,
                 login_id,
                 password):
        self.login_id = login_id
        self.password = password


class UserCreateInfo(object):
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
                 address,
                 avatar):
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
        self.avatar = avatar


class UserAccountInfo(object):
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
                 is_valid):
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


class UserProfileInfo(object):
    def __init__(self,
                 user_id,
                 gender,
                 mobile,
                 name,
                 nickname,
                 birthday,
                 update_time,
                 create_time,
                 avatar
                 ):
        self.user_id = user_id
        self.gender = gender
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.update_time = update_time
        self.create_time = create_time
        self.avatar = avatar
