#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
用户表数据库模型
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, Date, Boolean

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login_id = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    salt = Column(String(64), nullable=False)
    retry = Column(SmallInteger, nullable=False, default=0)
    first_login = Column(DateTime, nullable=True)
    last_login = Column(DateTime, nullable=True)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
    is_valid = Column(Boolean, nullable=False, default=True)


class UserInfoModel(Base):
    __tablename__ = 'user_info'
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(20), nullable=False)
    name = Column(String(20), nullable=True)
    gender = Column(String(1), nullable=False)
    mobile = Column(String(20), nullable=True)
    birthday = Column(Date, nullable=True)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)


class UserAddressModel(Base):
    __tablename__ = 'user_address'
    user_id = Column(Integer, primary_key=True)
    address = Column(String(256), nullable=False)
    update_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
    is_valid = Column(Boolean, nullable=False, default=True)