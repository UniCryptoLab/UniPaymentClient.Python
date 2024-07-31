from __future__ import absolute_import

from .models.check_ipn_response import CheckIpnResponse
from .models.get_currencies_response import GetCurrenciesResponse
from .models.get_exchange_rate_response import GetExchangeRateResponse
from .models.get_exchange_rates_response import GetExchangeRatesResponse
from .models.query_ips_response import QueryIpsResponse
from .base_client import BaseClient
from .models.ping_response import PingResponse


class CommonAPI(BaseClient):
    pass

    def ping(self, access_token, use_post=False) -> PingResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ping'
        method = 'GET'
        if use_post:
            method = 'POST'

        response_text = self.call_api(url, method, access_token)
        return PingResponse.from_json(response_text)

    def query_ips(self, access_token) -> QueryIpsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ips'
        response_text = self.call_api(url, 'GET', access_token)
        return QueryIpsResponse.from_json(response_text)

    def get_currencies(self, access_token) -> GetCurrenciesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/currencies'
        response_text = self.call_api(url, 'GET', access_token)
        return QueryIpsResponse.from_json(response_text)

    def get_exchange_rate_by_currency_pair(self, access_token, fiat_currency,
                                           crypto_currency) -> GetExchangeRateResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/rates/{fiat_currency}/{crypto_currency}'
        response_text = self.call_api(url, 'GET', access_token)
        # Adjust the JSON string to match dataclass field names as 'from' is a reserved keyword
        adjusted_json_string = response_text.replace('"from":', '"from_currency":').replace('"to":', '"to_currency":')
        return GetExchangeRateResponse.from_json(adjusted_json_string)

    def get_exchange_rate_by_fiat_currency(self, access_token, fiat_currency, ) -> GetExchangeRatesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/rates/{fiat_currency}'
        response_text = self.call_api(url, 'GET', access_token)
        # Adjust the JSON string to match dataclass field names as from is a reserved keyword
        adjusted_json_string = response_text.replace('"from":', '"from_currency":').replace('"to":', '"to_currency":')
        return GetExchangeRatesResponse.from_json(adjusted_json_string)

    def check_ipn(self, access_token, notify) -> CheckIpnResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ipn'
        response_text = self.call_api(url, 'POST', access_token, body=notify)
        return CheckIpnResponse.from_json(response_text)
