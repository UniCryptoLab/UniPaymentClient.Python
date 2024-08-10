from __future__ import absolute_import

import io
import json
import logging
import re
import ssl
from urllib.parse import urlencode

import certifi
import urllib3

from .api_exception import ApiException

logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):
    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject:
    def __init__(self, configuration, pools_size=4, maxsize=None):
        self._setup_ssl_configuration(configuration)
        self._setup_pool_manager(configuration, pools_size, maxsize)

    def _setup_ssl_configuration(self, configuration):
        self.cert_reqs = ssl.CERT_REQUIRED if configuration.verify_ssl else ssl.CERT_NONE
        self.ca_certs = configuration.ssl_ca_cert or certifi.where()

    def _setup_pool_manager(self, configuration, pools_size, maxsize):
        additional_pool_args = {
            'assert_hostname': configuration.assert_hostname} if configuration.assert_hostname is not None else {}
        maxsize = maxsize or configuration.connection_pool_maxsize or 4

        if configuration.debug:
            logging.basicConfig(level=logging.DEBUG)

        self.pool_manager = self._create_pool_manager(configuration, pools_size, maxsize, additional_pool_args)

    def _create_pool_manager(self, configuration, pools_size, maxsize, additional_pool_args):
        if configuration.proxy:
            return urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=self.cert_reqs,
                ca_certs=self.ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **additional_pool_args
            )
        else:
            return urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=self.cert_reqs,
                ca_certs=self.ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **additional_pool_args
            )

    def request(self, method, url, query_params=None, headers=None, body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        method = method.upper()
        self._validate_request_method(method)

        if post_params and body:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        headers = headers or {'Content-Type': 'application/json'}
        timeout = self._get_timeout(_request_timeout)

        try:
            return self._handle_request(method, url, query_params, headers, body, post_params, _preload_content,
                                        timeout)
        except urllib3.exceptions.SSLError as e:
            raise ApiException(status=0, reason=f"{type(e).__name__}\n{str(e)}")

    def _validate_request_method(self, method):
        valid_methods = ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']
        if method not in valid_methods:
            raise ValueError(f"Invalid HTTP request method: {method}")

    def _get_timeout(self, _request_timeout):
        if not _request_timeout:
            return None
        if isinstance(_request_timeout, (int, float)):
            return urllib3.Timeout(total=_request_timeout)
        if isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
            return urllib3.Timeout(connect=_request_timeout[0], read=_request_timeout[1])
        raise ValueError("Invalid timeout format")

    def _handle_request(self, method, url, query_params, headers, body, post_params, _preload_content, timeout):
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            return self._handle_body_methods(method, url, query_params, headers, body, post_params, _preload_content,
                                             timeout)
        else:
            return self._handle_query_methods(method, url, query_params, headers, _preload_content, timeout)

    def _handle_body_methods(self, method, url, query_params, headers, body, post_params, _preload_content, timeout):
        if query_params:
            url += '?' + urlencode(query_params)
        if re.search('json', headers['Content-Type'], re.IGNORECASE):
            request_body = json.dumps(body) if body is not None else '{}'
            return self.pool_manager.request(method, url, body=request_body, preload_content=_preload_content,
                                             timeout=timeout, headers=headers)
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            return self.pool_manager.request(method, url, fields=post_params, encode_multipart=False,
                                             preload_content=_preload_content, timeout=timeout, headers=headers)
        if headers['Content-Type'] == 'multipart/form-data':
            del headers['Content-Type']
            return self.pool_manager.request(method, url, fields=post_params, encode_multipart=True,
                                             preload_content=_preload_content, timeout=timeout, headers=headers)
        if isinstance(body, str):
            return self.pool_manager.request(method, url, body=body, preload_content=_preload_content, timeout=timeout,
                                             headers=headers)
        raise ApiException(status=0,
                           reason="Cannot prepare a request message for provided arguments. Please check that your arguments match declared content type.")

    def _handle_query_methods(self, method, url, query_params, headers, _preload_content, timeout):
        response = self.pool_manager.request(method, url, fields=query_params, preload_content=_preload_content,
                                             timeout=timeout, headers=headers)
        if _preload_content:
            response = RESTResponse(response)
            logger.debug("response body: %s", response.data)
        if not 200 <= response.status <= 299:
            raise ApiException(http_resp=response)
        return response

    def GET(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("GET", url, headers=headers, query_params=query_params, _preload_content=_preload_content,
                            _request_timeout=_request_timeout)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("HEAD", url, headers=headers, query_params=query_params, _preload_content=_preload_content,
                            _request_timeout=_request_timeout)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        return self.request("OPTIONS", url, headers=headers, query_params=query_params, post_params=post_params,
                            _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None, _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url, headers=headers, query_params=query_params,
                            _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
             _request_timeout=None):
        return self.request("POST", url, headers=headers, query_params=query_params, post_params=post_params,
                            _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
            _request_timeout=None):
        return self.request("PUT", url, headers=headers, query_params=query_params, post_params=post_params,
                            _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
              _request_timeout=None):
        return self.request("PATCH", url, headers=headers, query_params=query_params, post_params=post_params,
                            _preload_content=_preload_content, _request_timeout=_request_timeout, body=body)
