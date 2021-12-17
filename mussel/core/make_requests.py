#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ying jun
@email: wandy1208@live.com
@time: 2021/12/12 22:30
"""
from typing import Any, Callable, Dict, List, Optional
from urllib import parse

from requests import Response, Session

from mussel.scheme.api import Interface


class MakeRequest(object):
    def __init__(self, session: Optional[Session] = None, host: str = None) -> None:

        if session is None:
            session = Session()
        self.session = session
        self.responses: List[Response] = []
        self.host = host

    def to_send(self, interface: Interface, **kwargs: Any) -> None:

        """
        Args:
            interface: Interface object.
            kwargs: additional keyword arguments to pass through to |request|.
        """
        http_requests: Dict[str, Callable] = {
            "DELETE": self.session.delete,
            "GET": self.session.get,
            "HEAD": self.session.head,
            "OPTIONS": self.session.options,
            "PATCH": self.session.patch,
            "POST": self.session.post,
            "PUT": self.session.put,
        }

        method = interface.method.upper()
        if method not in http_requests:
            # todo: RequestError
            raise Exception(f'"{method}" is not a valid HTTP method.')
        self.responses.append(
            # todo: details log
            http_requests[method](parse.urljoin(self.host, interface.url), **kwargs)
        )

    send = to_send
