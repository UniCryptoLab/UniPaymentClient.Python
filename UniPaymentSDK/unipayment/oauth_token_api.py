from __future__ import absolute_import

import json

from . import UnipaymentSdkException
from .models.token_response import TokenResponse
from .configuration import Configuration
from .api_client import ApiClient


class OauthTokenAPI(object):

    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.api_client = ApiClient(self.configuration)
        self.api_client.set_default_header('Accept', 'application/json')
        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

    def get_access_token(self) -> TokenResponse:
        post_params = {'grant_type': 'client_credentials', 'client_id': self.configuration.client_id,
                       'client_secret': self.configuration.client_secret}

        url = f'{self.configuration.host}/connect/token'
        response_text = self.api_client.request(url, 'POST', post_params=post_params).data.decode('utf-8')
        response_json = json.loads(response_text)
        if 'error' in response_json:
            raise UnipaymentSdkException(message=response_json['error'])
        return TokenResponse.from_json(response_text)
