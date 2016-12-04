#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import options
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WrapSession(object):
    def __init__(self, real_session):
        self._session = real_session

    def __getattr__(self, attr):
        if not attr.startswith("_"):
            try:
                return getattr(self._session, attr)
            except Exception:
                raise
        else:
            raise AttributeError("cannot access private attribute {}.".format(attr))

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):

        self._session.close()
        if type is not None:
            return False


class DataBase(object, metaclass=Singleton):
    def __init__(self, db_conn):
        self._engine = create_engine(db_conn, echo=True if options.DEBUG else False)
        self._Session = sessionmaker(bind=self._engine)
        self.session = WrapSession(self._Session())


class BookStoreDB(object):

    @property
    def book_store_db(self):
        if not hasattr(self, "_book_store"):
            setattr(self, "_book_store", DataBase(options.MYSQL_CONN))
        return getattr(self, "_book_store")

book_store_db = BookStoreDB().book_store_db

Base = declarative_base()