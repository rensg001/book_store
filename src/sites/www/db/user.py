#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
用户数据库操作
"""
from awesome.db.base import book_store_db
from awesome.db.user import UserModel, UserInfoModel, UserAddressModel


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
                                            create_time=user_info.create_time)
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

    def get_by_id(self, user_id):
        with book_store_db.session as session:
            user = session.query(UserModel).get(UserModel.user_id == user_id)
        return user