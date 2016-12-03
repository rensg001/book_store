#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import uuid

from Crypto.Hash import SHA256


class PasswordHash(object):
    def __init__(self):
        self._password = None
        self._password_hash = None
        self._salt = str(uuid.uuid4())
        self._sha256 = SHA256.new()

    def update(self, password):
        if isinstance(password, str):
            password = password.encode("utf8")
        self._password = password
        self._sha256.update(self._password)
        self._sha256.update(self._salt.encode("utf8"))

    def _hex(self):
        self._password_hash = self._sha256.hexdigest()

    @property
    def salt(self):
        return self._salt

    @property
    def password(self):
        return self._password

    @property
    def password_hash(self):
        self._hex()
        return self._password_hash

    @staticmethod
    def compare(password, salt, password_hash):
        if isinstance(password, str):
            password = password.encode("utf8")
        if isinstance(salt, str):
            salt = salt.encode("utf8")
        sha256 = SHA256.new()
        sha256.update(password)
        sha256.update(salt)
        return sha256.hexdigest() == password_hash