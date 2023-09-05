# coding: utf-8

from __future__ import absolute_import

import unittest
import uuid

from unipayment import CreateInvoiceRequest, QueryInvoiceRequest, CreateWithdrawalRequest, CancelWithdrawalRequest
from unipayment import UniPaymentClient
from test_state import JSONifiedState

class TestUniPaymentClient(unittest.TestCase):

    def setUp(self):
        self.client_id = '74feb539-ba5a-4ae9-b901-4da4fb539574'
        self.client_secret = 'BsoRhgqzhR1TYMtwTRYdPxBTvR5rxkW9K'
        self.app_id = '2a9bd90b-fe95-4659-83cb-04de662fbbac'
        self.invoice_id = 'SrAARgNrPgvveiBQtNc4gk'
        self.notify = ''
        self.client = UniPaymentClient(self.client_id, self.client_secret, True, True)
        self.state = JSONifiedState()
        self.state.restore()


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
        lang = 'en'
        ext_args = None
        confirm_speed = 'low'

        create_invoice_request = CreateInvoiceRequest(app_id=app_id, price_amount=price_amount,
                                                      price_currency=price_currency,
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

    def test_get_wallet_balances(self):
        """Test case for get_wallet_balances

        """
        wallet_balances_response = self.client.get_wallet_balances()
        self.assertEqual('OK', wallet_balances_response.code)

    def test_create_withdrawal(self):
        """Test case for create_withdrawal

        """
        create_withdrawal_request = CreateWithdrawalRequest(amount=1.01, asset_type="USDT", include_fee=True,
                                                            auto_confirm=True, network="NETWORK_BSC")
        create_withdrawal_response = self.client.create_withdrawal(create_withdrawal_request)
        self.assertEqual('OK', create_withdrawal_response.code)

    def test_get_withdrawal_by_id(self):
        """Test case for get_withdrawal_by_id

        """
        get_withdrawal_by_id_response = self.client.get_withdrawal_by_id(
            withdrawal_id='12e0c40f-9df1-40a0-a336-029081b3a638')
        self.assertEqual('OK', get_withdrawal_by_id_response.code)

    def test_get_withdrawal_by_id(self):
        """Test case for cancel_withdrawal

        """
        cancel_withdrawal_request = CancelWithdrawalRequest(id="a6389658-ac47-42f7-b71e-4bd1dc51ee2d")
        cancel_withdrawal_response = self.client.cancel_withdrawal(cancel_withdrawal_request)
        self.assertEqual('OK', cancel_withdrawal_response.code)

    def test_query_withdrawals(self):
        """Test case for query_withdrawals

        """
        query_withdrawals_response = self.client.query_withdrawals()
        print(query_withdrawals_response)
        self.assertEqual('OK', query_withdrawals_response.code)

    def test_query_payouts(self):
        """Test case for query_payouts

        """
        query_payouts_response = self.client.query_payouts()
        print(query_payouts_response)
        self.assertEqual('OK', query_payouts_response.code)


if __name__ == '__main__':
    unittest.main()
