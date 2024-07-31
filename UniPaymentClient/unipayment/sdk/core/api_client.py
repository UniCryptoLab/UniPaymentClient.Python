# coding: utf-8
from __future__ import absolute_import

import platform
from multiprocessing.pool import ThreadPool

from .configuration import Configuration
from .rest import RESTClientObject

SDK_VERSION = '2.0.0'


class ApiClient(object):

    def __init__(self, configuration: Configuration):
        self.pool = ThreadPool()
        self.rest_client = RESTClientObject(configuration)
        self.default_headers = {}
        self.user_agent = ('unipayment_sdk_python/' + SDK_VERSION + ' (' + platform.system() + ' ' + platform.release()
                           + ')')

    def __del__(self):
        self.pool.close()
        self.pool.join()

    @property
    def user_agent(self):
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def request(self, url, method, query_params=None, headers=None, post_params=None, body=None, _preload_content=False,
                _request_timeout=None):
        if headers is None:
            headers = self.default_headers

        if method == "GET":
            return self.rest_client.GET(url, query_params=query_params, headers=headers,
                                        _preload_content=_preload_content, _request_timeout=_request_timeout)
        elif method == "HEAD":
            return self.rest_client.HEAD(url, query_params=query_params, headers=headers,
                                         _preload_content=_preload_content, _request_timeout=_request_timeout)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url, query_params=query_params, headers=headers,
                                            _preload_content=_preload_content, _request_timeout=_request_timeout)
        elif method == "POST":
            return self.rest_client.POST(url, headers=headers, post_params=post_params,
                                         _preload_content=_preload_content, _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url, headers=headers, post_params=post_params,
                                        _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url, headers=headers, post_params=post_params,
                                          _preload_content=_preload_content, _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url, query_params=query_params, headers=headers,
                                           _preload_content=_preload_content, _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError("HTTP method must be `GET`, `HEAD`, `OPTIONS`, `POST`, `PATCH`, `PUT` or `DELETE`.")
