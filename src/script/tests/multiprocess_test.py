#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import ctypes
import multiprocessing

text = b"a b c d e f g h"
text_list = text.split()
text_list.append(b"\n")

# buffer = ["", "", "", "", ""]
buffer_size = 5
buffer = multiprocessing.Array(ctypes.c_char, buffer_size)

s = multiprocessing.Semaphore(value=1)
n = multiprocessing.Semaphore(value=0)
e = multiprocessing.Semaphore(value=buffer_size)


def produce(t, buffer, buffer_size, index):
    buffer[index % buffer_size] = t
    # buffer.append(t)
    n.release()


def producer(buffer, buffer_size):
    index = 0
    for t in text_list:
        e.acquire()
        s.acquire()
        produce(t, buffer, buffer_size, index)
        s.release()
        index += 1


def consume(buffer, buffer_size, index):

    # print(index)
    product = buffer[index % buffer_size]
    e.release()
    return product


def consumer(buffer, buffer_size):
    index = 0

    while True:
        n.acquire()
        s.acquire()
        product = consume(buffer, buffer_size, index)
        s.release()
        index += 1
        print(product)
        if product == b"\n":
            break


producer_pool = []

for i in range(1):
    p = multiprocessing.Process(target=producer, args=(buffer, buffer_size))
    p.start()
    producer_pool.append(p)

c = multiprocessing.Process(target=consumer, args=(buffer, buffer_size))
c.start()

for p in producer_pool:
    p.join()

c.join()
