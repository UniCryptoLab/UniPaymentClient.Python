# coding: utf-8

from __future__ import absolute_import

import unittest
import uuid

import unipayment
from unipayment import Configuration, ApiClient, UniPaymentClient
from unipayment import CreateInvoiceRequest, QueryInvoiceRequest


class TestUniPaymentClient(unittest.TestCase):

    def setUp(self):
        self.client_id = '74feb539-ba5a-4ae9-b901-4da4fb539574'
        self.client_secret = 'BsoRhgqzhR1TYMtwTRYdPxBTvR5rxkW9K'
        self.app_id = '2a9bd90b-fe95-4659-83cb-04de662fbbac'
        self.invoice_id = 'SrAARgNrPgvveiBQtNc4gk'
        self.notify = ''
        self.client = UniPaymentClient(self.client_id, self.client_secret, True, True)

    def tearDown(self):
        pass

    def test_create_invoice(self):
        """Test case for create_invoice

        """
        app_id = self.app_id
        price_amount = 100
        price_currency = 'USD'
        pay_currency = 'USDT'
        notify_url = 'https://google.com'
        redirect_url = 'https://google.com'
        order_id = uuid.uuid4().hex
        title = 'Test Invoice'
        description = 'Test Desc'
        lang = 'en-US'
        ext_args = None
        confirm_speed = 'low'

        create_invoice_request = CreateInvoiceRequest(app_id=app_id, price_amount=price_amount, price_currency=price_currency,
                                                      pay_currency=pay_currency, notify_url=notify_url,
                                                      redirect_url=redirect_url,
                                                      order_id=order_id, title=title, description=description,
                                                      lang=lang, ext_args=ext_args, confirm_speed=confirm_speed)
        create_invoice_response = self.client.create_invoice(create_invoice_request)
        self.assertEqual('OK', create_invoice_response.code)

    def test_query_invoice(self):
        """Test case for query_invoice

        """
        query_invoice_request = QueryInvoiceRequest(order_id="ORDER_123456", page_no=1, page_size=10)
        query_invoice_response = self.client.query_invoice(query_invoice_request)
        self.assertEqual('OK', query_invoice_response.code)

    def test_get_invoice_by_id(self):
        """Test case for get_invoice_by_id

        """
        get_invoice_by_id_response = self.client.get_invoice_by_id(self.invoice_id)
        self.assertEqual('OK', get_invoice_by_id_response.code)

    def test_get_exchange_rates_by_fiat_currency(self):
        """Test case for get_exchange_rate_by_fiat_currency

        """
        get_exchange_rates_response = self.client.get_exchange_rates_by_fiat_currency('USD')
        self.assertEqual('OK', get_exchange_rates_response.code)

    def test_get_exchange_rates_by_currency_pair(self):
        """Test case for get_exchange_rates_by_currency_pair

        """
        get_exchange_rate_response = self.client.get_exchange_rates_by_currency_pair('USD', 'BTC')
        self.assertEqual('OK', get_exchange_rate_response.code)

    def test_query_ips(self):
        """Test case for query_ips

        """
        query_ips_response = self.client.query_ips()
        self.assertEqual('OK', query_ips_response.code)

    def test_get_currencies(self):
        """Test case for get_currencies

        """
        get_currencies_response = self.client.get_currencies()
        self.assertEqual('OK', get_currencies_response.code)


if __name__ == '__main__':
    unittest.main()
