#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import random
import string


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(length))

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info(random_word(20))