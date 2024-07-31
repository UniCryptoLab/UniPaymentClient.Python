from __future__ import absolute_import

import base64
import json
import logging
from datetime import datetime

from .configuration import Configuration
from .api_client import ApiClient
from .api_exception import ApiException
from .unipayment_sdk_exception import UnipaymentSdkException

LOGGER = logging.getLogger(__name__)


def is_valid(token: str) -> bool:
    if not token:
        return False

    parts = token.split(".")
    if len(parts) != 3:
        return False

    try:
        decoded_part2 = base64.b64decode(parts[1]).decode('utf-8')
        data_map = json.loads(decoded_part2)
        exp = int(data_map.get("exp"))
        exp_in_millis = exp * 1000
        LOGGER.info("Access Token expires on: %s", datetime.fromtimestamp(exp_in_millis / 1000))
        current_millis = int(datetime.utcnow().timestamp() * 1000)
        return exp_in_millis > current_millis
    except (json.JSONDecodeError, ValueError) as e:
        LOGGER.warning("Invalid token: %s", token, exc_info=e)
        return False


class BaseClient(object):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.api_client = ApiClient(self.configuration)
        self.api_client.set_default_header('Accept', 'application/json')
        self.api_client.set_default_header('Content-Type', 'application/json')

    def call_api(self, url, method, access_token, query_params=None, post_params=None, body=None):
        if is_valid(access_token) is False:
            raise UnipaymentSdkException('Invalid or expired access token')

        headers = self.api_client.default_headers
        headers['Authorization'] = f'Bearer {access_token}'
        response = self.api_client.request(url, method, headers=headers, query_params=query_params,
                                           post_params=post_params, body=body)

        status_code = response.status
        if 200 <= status_code < 300:
            return response.data.decode('utf-8')
        else:
            raise ApiException(http_resp=response)
