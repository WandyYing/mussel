#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/15 21:29
"""

import copy

import pytest

from mussel.core.make_requests import MakeRequest
from tests.api.service.httpbin import HttpBin


def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test"""

    def test_decorator(fn):
        @pytest.mark.parametrize("data", fn_data_provider)
        def repl(self, data):
            fn(self, data)

        return repl

    return test_decorator


class TestHttpBin:
    def setUp(self):
        ...

    # todo: support dataProvider
    @data_provider([{"path_var": {"codes": 200}}, {"path_var": {"codes": 300}}])
    def test_status(self, data):
        send_request = MakeRequest(host="http://www.httpbin.org/")
        # todo: send_request.send(HttpBin.status, testdata)
        print(data)
        HttpBin_status_copy = copy.deepcopy(HttpBin.status)
        HttpBin_status_copy.url = HttpBin_status_copy.url.format(**data["path_var"])
        send_request.send(HttpBin_status_copy)
        response = send_request.responses[-1]
        assert response.status_code == 200
