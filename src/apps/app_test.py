#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from kombu import Queue, Exchange
from kombu.common import Broadcast
from celery import Celery

app = Celery(name="app_test",
             backend="redis://localhost",
             broker="amqp://guest@localhost//")

app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default',    routing_key='task.#', exchenge=Exchange('default', type='topic')),
    Queue('feed_tasks', routing_key='feed.#', exchange=Exchange('feed', type='topic')),
    Broadcast('broadcast_tasks'),
)
# task_default_exchange = 'tasks'
# task_default_exchange_type = 'topic'
# task_default_routing_key = 'task.default'
app.conf.task_routes = {
    "app_test.feed_task": {"queue": "feed_tasks", "exchange": "feed", "routing_key": "feed.task"},
    "app_test.broadcast_task": {"queue": "broadcast_tasks"}
}

# app.config_from_object("celeryconfig")


@app.task(celery_ignore_result=False)
def add(x, y):
    return x + y


@app.task(celery_ignore_result=False)
def other_task():
    return "other task has done."


@app.task(celery_ignore_result=False)
def feed_task():
    return "feed task has done."


@app.task(celery_ignore_result=True)
def broadcast_task():
    return "broadcast task has done."

add_sig = app.signature("app_test.add", args=(2,2))
