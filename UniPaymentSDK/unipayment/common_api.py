from __future__ import absolute_import

from .base_client import BaseClient
from .models.check_ipn_response import CheckIpnResponse
from .models.get_currencies_response import GetCurrenciesResponse
from .models.get_exchange_rate_response import GetExchangeRateResponse
from .models.get_exchange_rates_response import GetExchangeRatesResponse
from .models.ping_response import PingResponse
from .models.query_ips_response import QueryIpsResponse


class CommonAPI(BaseClient):
    pass

    def ping(self, use_post=False) -> PingResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ping'
        method = 'GET'
        if use_post:
            method = 'POST'

        response_text = self.call_api(url, method)
        return PingResponse.from_json(response_text)

    def query_ips(self) -> QueryIpsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ips'
        response_text = self.call_api(url, 'GET')
        return QueryIpsResponse.from_json(response_text)

    def get_currencies(self) -> GetCurrenciesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/currencies'
        response_text = self.call_api(url, 'GET')
        return QueryIpsResponse.from_json(response_text)

    def get_exchange_rate_by_currency_pair(self, fiat_currency,
                                           crypto_currency) -> GetExchangeRateResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/rates/{fiat_currency}/{crypto_currency}'
        response_text = self.call_api(url, 'GET')
        # Adjust the JSON string to match dataclass field names as 'from' is a reserved keyword
        adjusted_json_string = response_text.replace('"from":', '"from_currency":').replace('"to":', '"to_currency":')
        return GetExchangeRateResponse.from_json(adjusted_json_string)

    def get_exchange_rate_by_fiat_currency(self, fiat_currency, ) -> GetExchangeRatesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/rates/{fiat_currency}'
        response_text = self.call_api(url, 'GET')
        # Adjust the JSON string to match dataclass field names as from is a reserved keyword
        adjusted_json_string = response_text.replace('"from":', '"from_currency":').replace('"to":', '"to_currency":')
        return GetExchangeRatesResponse.from_json(adjusted_json_string)

    def check_ipn(self, notify) -> CheckIpnResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/ipn'
        response_text = self.call_api(url, 'POST', body=notify)
        return CheckIpnResponse.from_json(response_text)
