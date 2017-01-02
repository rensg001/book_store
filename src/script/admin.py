#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""
添加管理员
"""

import logging
import argparse
import os

from datetime import datetime

from awesome.utils.password import PasswordHash
from awesome.utils.readconfig import read_config_file
from sqlalchemy.exc import IntegrityError


logging.basicConfig(level=logging.INFO)


class AdminManager(object):
    def __init__(self, login_id, password):
        self.login_id = login_id
        self.password = password
        self.hash_tool = PasswordHash()
        self.hash_tool.update(self.password)

    def _add(self):
        from db.base import book_store_db
        from db.user_model import Admin

        now = datetime.now()
        try:
            with book_store_db.session as session:
                admin = Admin(login_id=self.login_id,
                              password=self.hash_tool.password_hash,
                              salt=self.hash_tool.salt,
                              retry=0,
                              update_time=now,
                              create_time=now,
                              is_valid=True)
                session.add(admin)
                session.commit()
        except IntegrityError:
            logging.info("登陆ID重复请更换后重试")

    def go(self):
        self._add()

if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(cur_dir, "app.conf")
    read_config_file(config_path)

    parser = argparse.ArgumentParser()
    parser.add_argument("login_id", help="admin user login_id.")
    parser.add_argument("password", help="admin user password.")
    args = parser.parse_args()

    admin_manager = AdminManager(login_id=args.login_id, password=args.password)
    admin_manager.go()
