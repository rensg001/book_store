#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime
from awesome.utils.password import PasswordHash
from service.user_info import UserInfoM, UserInfoV
from sites.www.db.user import UserRepository


class UserService(object):
    def __init__(self):
        self.user_repository = UserRepository()

    def create(self, user_info_v: UserInfoV):
        password_hash = PasswordHash()
        password_hash.update(user_info_v.password)
        now = datetime.now()
        user_info_m = UserInfoM(user_id=0,
                                login_id=user_info_v.login_id,
                                password=password_hash.password_hash,
                                salt=password_hash.salt,
                                retry=0,
                                first_login=None,
                                last_login=None,
                                update_time=now,
                                create_time=now,
                                is_valid=True,
                                gender=user_info_v.gender,
                                mobile=user_info_v.mobile,
                                name=user_info_v.name,
                                nickname=user_info_v.nickname,
                                birthday=user_info_v.birthday,
                                address=user_info_v.address)
        return self.user_repository.create(user_info_m)

    def get_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)