#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from setuptools import setup, find_packages

setup(
    name="book_store",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"":"src"},
    package_data={}
      )