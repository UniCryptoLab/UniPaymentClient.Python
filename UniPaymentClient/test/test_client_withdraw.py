# coding: utf-8

from __future__ import absolute_import

import logging
import os
from dotenv import load_dotenv
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
import uuid

from unipayment import CreateInvoiceRequest, QueryInvoiceRequest, CreateWithdrawalRequest, CancelWithdrawalRequest
from unipayment import UniPaymentClient
from test_state import JSONifiedState


class TestUniPaymentClient(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.client_id = os.getenv('client_id', 'test client id')
        self.client_secret = os.getenv('client_secret', 'test client id')
        self.app_id = os.getenv('app_id', 'test client id')
        self.withdraw_id = ''
        self.notify = ''
        self.client = UniPaymentClient(self.client_id, self.client_secret, False, False)
        self.state = JSONifiedState()
        self.state.restore()

    def tearDown(self):
        pass

    def test_1_get_wallet_balances(self):
        """Test case for get_wallet_balances

        """

        wallet_balances_response = self.client.get_wallet_balances()
        self.assertEqual('OK', wallet_balances_response.code)

    def test_2_create_withdrawal(self):
        """Test case for create_withdrawal

        """
        create_withdrawal_request = CreateWithdrawalRequest(amount=1.01, asset_type="USDT", include_fee=True,
                                                            auto_confirm=False, network="NETWORK_BSC")
        create_withdrawal_response = self.client.create_withdrawal(create_withdrawal_request)
        self.assertEqual('OK', create_withdrawal_response.code)
        self.assertEqual('NETWORK_BSC', create_withdrawal_response.data.network)
        self.assertEqual('USDT', create_withdrawal_response.data.asset_type)
        self.assertEqual(1.01, create_withdrawal_response.data.amount)
        self.withdraw_id = create_withdrawal_response.data.id

        self.state.on_create_withdraw(create_withdrawal_response.data)



    def test_3_get_withdrawal_by_id(self):
        """Test case for get_withdrawal_by_id

        """
        self.assertNotIn(self.state.data['withdrawal_id'], ['', None])

        get_withdrawal_by_id_response = self.client.get_withdrawal_by_id(
            withdrawal_id=self.state.data['withdrawal_id'])
        self.assertEqual('OK', get_withdrawal_by_id_response.code)

    def test_4_cancel_withdrawal_by_id(self):
        """Test case for cancel_withdrawal

        """
        self.assertNotIn(self.state.data['withdrawal_id'], ['', None])

        cancel_withdrawal_request = CancelWithdrawalRequest(id=self.state.data['withdrawal_id'])
        cancel_withdrawal_response = self.client.cancel_withdrawal(cancel_withdrawal_request)
        self.assertEqual('OK', cancel_withdrawal_response.code)

    def test_5_query_withdrawals(self):
        """Test case for query_withdrawals

        """
        query_withdrawals_response = self.client.query_withdrawals()
        print(query_withdrawals_response)
        self.assertEqual('OK', query_withdrawals_response.code)


if __name__ == '__main__':
    unittest.main()
