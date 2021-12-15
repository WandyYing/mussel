#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/15 21:29
"""

from mussel.core.make_requests import MakeRequest
from tests.api.service.httpbin import HttpBin


class TestHttpBin:
    def setUp(self):
        ...

    # todo: support dataProvider
    def test_status(self):
        send_request = MakeRequest(host="http://www.httpbin.org/")
        # todo: send_request.send(HttpBin.status, testdata)
        send_request.send(HttpBin.status)
        response = send_request.responses[-1]
        assert response.status_code == 200
