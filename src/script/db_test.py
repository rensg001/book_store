#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
# import MySQLdb
#
# def connection(host, user, password, db):
#     conn = MySQLdb.connect(host=host,
#                     user=user,
#                     passwd=password,
#                     db=db)
#     return conn
#
# def main():
#     conn = connection("localhost", "root", "123456", "test")
#     cur = conn.cursor()
#     cur.execute("""
#         UPDATE `user` SET `is_valid`=1, `counter_id`=173632123 WHERE `user_id`=1
#     """)
#     cur.execute("""
#         UPDATE `book` SET `name`='hdhd' WHERE `book_id`=1
#     """)
#
#     conn.commit()
#     cur.close()
#
# if __name__ == "__main__":
#     main()