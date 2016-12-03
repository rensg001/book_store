#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import random
import string


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(length))
