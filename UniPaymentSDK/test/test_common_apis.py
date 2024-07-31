from __future__ import absolute_import

import logging

import pytest

from test.test_base_client import TestBaseClient

logger = logging.getLogger(__name__)


class TestOauthTokenAPI(TestBaseClient):
    pass

    @pytest.mark.order(1)
    def test_ping(self):
        """
            Test case for ping
        """
        """
            Use POST HTTP Method
        """
        ping_response = self.CommonAPI.ping(self.access_token, use_post=True)
        logger.debug("response body: %s", ping_response.to_json())
        self.assertEqual('OK', ping_response.code)
        self.assertEqual('pong', ping_response.msg)

        """
            Use GET HTTP Method
        """
        ping_response = self.CommonAPI.ping(self.access_token)
        logger.debug("response body: %s", ping_response.to_json())
        self.assertEqual('OK', ping_response.code)
        self.assertEqual('pong', ping_response.msg)

    @pytest.mark.order(2)
    def test_query_ips(self):
        """
            Test case for query_ips
        """
        query_ips_response = self.CommonAPI.query_ips(self.access_token)
        logger.debug("response body: %s", query_ips_response.to_json())
        self.assertEqual('OK', query_ips_response.code)
        self.assertEqual(['2.2.2.2'], query_ips_response.data)

    @pytest.mark.order(3)
    def test_get_currencies(self):
        """
            Test case for get_currencies
        """
        get_currencies_response = self.CommonAPI.get_currencies(self.access_token)
        logger.debug("response body: %s", get_currencies_response.to_json())
        self.assertEqual('OK', get_currencies_response.code)

    @pytest.mark.order(4)
    def test_get_exchange_rate_by_currency_pair(self):
        """
            Test case for get_exchange_rate_by_currency_pair
        """
        get_exchange_rate_response = self.CommonAPI.get_exchange_rate_by_currency_pair(self.access_token, 'USD', 'BTC')
        logger.debug("response body: %s", get_exchange_rate_response.to_json())
        self.assertEqual('OK', get_exchange_rate_response.code)

    @pytest.mark.order(5)
    def test_get_exchange_rate_by_fiat_currency(self):
        """
            Test case for get_exchange_rate_by_fiat_currency
        """
        get_exchange_rates_response = self.CommonAPI.get_exchange_rate_by_fiat_currency(self.access_token, 'USD')
        logger.debug("response body: %s", get_exchange_rates_response.to_json())
        self.assertEqual('OK', get_exchange_rates_response.code)

    @pytest.mark.order(6)
    def test_check_ipn(self):
        """
            Test case for check_ipn
        """
        check_ipn_response = self.CommonAPI.check_ipn(self.access_token,
                                                      {'ipn_type': 'invoice', 'event': 'invoice_created',
                                                       'app_id': 'cee1b9e2-d90c-4b63-9824-d621edb38012',
                                                       'invoice_id': '12wQquUmeCPUx3qmp3aHnd',
                                                       'order_id': 'ORDER_123456', 'price_amount': 2.0,
                                                       'price_currency': 'USD', 'network': None, 'address': None,
                                                       'pay_currency': None, 'pay_amount': 0.0, 'exchange_rate': 0.0,
                                                       'paid_amount': 0.0, 'confirmed_amount': 0.0,
                                                       'refunded_price_amount': 0.0,
                                                       'create_time': '2022-09-14T04:57:54.5599307Z',
                                                       'expiration_time': '2022-09-14T05:02:54.559933Z',
                                                       'status': 'New', 'error_status': 'None',
                                                       'ext_args': 'Merchant Pass Through Data', 'transactions': None,
                                                       'notify_id': 'fd58cedd-67c6-4053-ae65-2f6fb09a7d2c',
                                                       'notify_time': '0001-01-01T00:00:00'})
        logger.debug("response body: %s", check_ipn_response.to_json())
        self.assertEqual('OK', check_ipn_response.code)
        self.assertEqual('IPN is verified.', check_ipn_response.msg)
