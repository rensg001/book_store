#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from datetime import datetime

from awesome.errors import ErrorEnum
from awesome.utils.password import PasswordHash
from service.user_info import UserCreateInfo, UserSignupInfo, UserLoginInfo, AdminLoginInfo
from db.user import UserRepository


class UserService(object):
    def __init__(self):
        self.user_repository = UserRepository()

    def create(self, user_info_v: UserSignupInfo):
        password_hash = PasswordHash()
        password_hash.update(user_info_v.password)
        now = datetime.now()
        user_info_m = UserCreateInfo(user_id=0,
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
                                     address=user_info_v.address,
                                     avatar=user_info_v.avatar)
        return self.user_repository.create(user_info_m)

    def get_profile_by_id(self, user_id):
        return self.user_repository.get_profile_by_id(user_id)

    def login(self, user_login_info: UserLoginInfo):
        user = self.user_repository.get_by_login_id(user_login_info.login_id)
        if not user:
            return ErrorEnum.login_failure.value
        equal = PasswordHash.compare(user_login_info.password,
                                     user.salt,
                                     user.password)
        if not equal:
            user.retry += 1
            self.user_repository.update_account(user)
            return ErrorEnum.login_failure.value

        now = datetime.now()
        user.retry = 0
        if not user.first_login:
            user.first_login = now
        user.last_login = now
        self.user_repository.update_account(user)
        return user.user_id

    def get_admin_by_id(self, admin_id: int):
        admin = self.user_repository.get_admin_by_id(admin_id)
        if not admin:
            return admin
        del admin.retry
        del admin.password
        del admin.is_valid
        return admin

    def admin_login(self, admin_login_info: AdminLoginInfo):
        admin = self.user_repository.get_admin_by_login_id(admin_login_info.login_id)
        if not admin:
            return ErrorEnum.login_failure.value
        equal = PasswordHash.compare(admin_login_info.password,
                                     admin.salt,
                                     admin.password)
        if not equal:
            return ErrorEnum.login_failure.value
        return admin.admin_id
