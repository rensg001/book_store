#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import redis
import time


class RedisClient(object):
    def __init__(self, host, port, db=0):
        self._redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def __getattr__(self, name):
        return getattr(self._redis_client, name)


class Session(object):
    def __init__(self, session_id):
        self._session_id = session_id
        self._redis_client = redis_client
        if self._redis_client.exists("login:") and not self._redis_client.type("login:") == b"set":
            self._redis_client.delete("login:")
        self._redis_client.sadd("login:", session_id)

    def __getitem__(self, key):
        return self._redis_client.hget(self._session_id, key)

    def __setitem__(self, key, value):
        self._redis_client.hset(self._session_id, key, value)


redis_client = RedisClient(host="localhost", port=6379)


def check_token(token):
    return redis_client.hget("login:", token)


def update_token(token, user):
    timestamp = time.time()
    redis_client.hset("login:", token, user)
    redis_client.zadd("recent:", timestamp, token)


if __name__ == "__main__":
    session = Session("mysessionid")
    # session["login_id"] = "aaoonn"
    # session["name"] = "test"
    print((session["login_id"], session["name"]))
    # print(redis_client.type("login:"))
