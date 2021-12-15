#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/12 23:12
"""
from dataclasses import dataclass


@dataclass
class Interface:
    method: str
    url: str
    title: str = ""
