#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
用户数据库操作
"""
from awesome.utils.database import Convert
from db.base import book_store_db
from db.user_model import UserModel, UserInfoModel, UserAddressModel, Admin
from service.user_info import UserAccountInfo, UserProfileInfo, AdminInfo


class UserRepository(object):
    def create(self, user_info):
        with book_store_db.session as session:
            user_model = UserModel(login_id=user_info.login_id,
                                   password=user_info.password,
                                   salt=user_info.salt,
                                   retry=user_info.retry,
                                   first_login=user_info.first_login,
                                   last_login=user_info.last_login,
                                   update_time=user_info.update_time,
                                   create_time=user_info.create_time,
                                   is_valid=user_info.is_valid)
            session.add(user_model)
            session.flush()
            user_info_model = UserInfoModel(user_id=user_model.user_id,
                                            nickname=user_info.nickname,
                                            name=user_info.name,
                                            gender=user_info.gender,
                                            mobile=user_info.mobile,
                                            birthday=user_info.birthday,
                                            update_time=user_info.update_time,
                                            create_time=user_info.create_time,
                                            avatar=user_info.avatar)
            if user_info.address:
                user_address_model = UserAddressModel(user_id=user_model.user_id,
                                                      address=user_info.address,
                                                      update_time=user_info.update_time,
                                                      create_time=user_info.create_time,
                                                      is_valid=True)
                session.add(user_address_model)

            session.add(user_info_model)
            session.commit()
            user_id = user_model.user_id
        return user_id

    def update_account(self, user_account_info):
        with book_store_db.session as session:
            user = session.query(UserModel).get(user_account_info.user_id)
            user.login_id = user_account_info.login_id
            user.password = user_account_info.password
            user.salt = user_account_info.salt
            user.retry = user_account_info.retry
            user.first_login = user_account_info.first_login
            user.last_login = user_account_info.last_login
            user.update_time = user_account_info.update_time
            user.create_time = user_account_info.create_time
            user.is_valid = user_account_info.is_valid
            session.commit()

    def get_profile_by_id(self, user_id):
        with book_store_db.session as session:
            user = session.query(UserInfoModel) \
                .filter(UserInfoModel.user_id == user_id) \
                .first()
            convert = Convert(user, UserProfileInfo)
        return convert.convert()

    def get_by_login_id(self, login_id):
        with book_store_db.session as session:
            user = session.query(UserModel) \
                .filter(UserModel.login_id == login_id) \
                .filter(UserModel.is_valid) \
                .first()
            convert = Convert(user, UserAccountInfo)
        return convert.convert()

    def get_admin_by_id(self, admin_id: int):
        with book_store_db.session as session:
            admin = session.query(Admin) \
                .filter(Admin.admin_id == admin_id) \
                .first()
            if not admin:
                return None
        return AdminInfo(admin_id=admin.admin_id,
                         login_id=admin.login_id,
                         password=admin.password,
                         salt=admin.salt,
                         retry=admin.retry,
                         update_time=admin.update_time,
                         create_time=admin.create_time,
                         is_valid=admin.is_valid)

    def get_admin_by_login_id(self, login_id):
        with book_store_db.session as session:
            admin = session.query(Admin) \
                .filter(Admin.login_id == login_id) \
                .first()
            if not admin:
                return None
            return AdminInfo(admin_id=admin.admin_id,
                             login_id=admin.login_id,
                             password=admin.password,
                             salt=admin.salt,
                             retry=admin.retry,
                             update_time=admin.update_time,
                             create_time=admin.create_time,
                             is_valid=admin.is_valid)
