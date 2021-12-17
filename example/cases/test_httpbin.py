#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/15 21:29
"""

import copy

from example.api.service.httpbin import HttpBin
from mussel.core.make_requests import MakeRequest
from mussel.utils import data_provider


class TestHttpBin:
    def setUp(self):
        ...

    # todo: support dataProvider
    @data_provider([{"path_var": {"codes": 200}}, {"path_var": {"codes": 300}}])
    def test_status(self, data):
        send_request = MakeRequest(host="http://www.httpbin.org/")
        # todo: copy.deepcopy implement
        HttpBin_status_copy = copy.deepcopy(HttpBin.status)
        HttpBin_status_copy.url = HttpBin_status_copy.url.format(**data["path_var"])
        send_request.send(HttpBin_status_copy)
        response = send_request.responses[-1]
        assert response.status_code == data["path_var"]["codes"]
