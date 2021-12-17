#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/18 19:37
"""

import pytest


def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test"""

    def decorator(fn):
        @pytest.mark.parametrize("data", fn_data_provider)
        def repl(self, data):
            fn(self, data)

        return repl

    return decorator
