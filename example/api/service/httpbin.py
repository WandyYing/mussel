#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/12 22:57
"""

from mussel.scheme.api import Interface


class HttpBin:

    # todo: support params in url path
    status = Interface("GET", "/status/{codes}", "Return status code")
