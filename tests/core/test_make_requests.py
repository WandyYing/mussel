#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/17 20:25
"""

from unittest import mock

import pytest

from mussel.core.make_requests import MakeRequest
from mussel.scheme.api import Interface


class TestMakeAPIRequests:
    def test_can_be_instantiated(self):
        mr = MakeRequest()

        assert isinstance(mr, MakeRequest)

    @pytest.mark.parametrize(
        "interface",
        [
            Interface("delete", "url"),
            Interface("get", "url"),
            Interface("head", "url"),
            Interface("options", "url"),
            Interface("patch", "url"),
            Interface("post", "url"),
            Interface("put", "url"),
        ],
    )
    @mock.patch("mussel.core.make_requests.Session")
    def test_http_method_calls_correct_session_method(self, mocked_session, interface):
        mar = MakeRequest()

        mar.send(interface)

        getattr(mar.session, interface.method).assert_called_once()
