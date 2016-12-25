#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


broker_url = "amqp://guest@localhost//"
result_backend = "redis://localhost"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = False

task_routes = {
    "app_test.add": {"queue": "add"},
    "app_test.feed_task": {"queue": "feed_tasks", "routing_key": "feed.tasks"},
}
