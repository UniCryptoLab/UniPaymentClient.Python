from __future__ import absolute_import

import logging
from typing import Optional

from test.test_base_client import TestBaseClient
from unipayment.models import GetWalletAccountsResponse

logger = logging.getLogger(__name__)


def get_account_id(response: GetWalletAccountsResponse, asset_type) -> Optional[str]:
    for balance in response.data:
        if balance.asset_type == asset_type:
            return balance.id
    return None


class TestWalletAPI(TestBaseClient):

    def test_get_balances(self):
        """
            Test case get_balances
        """
        get_wallet_balances_response = self.WalletAPI.get_balances(self.access_token)
        logger.debug("response body: %s", get_wallet_balances_response.to_json())
        self.assertEqual('OK', get_wallet_balances_response.code)

    def test_get_accounts(self):
        """
            Test case get_balances
        """
        get_wallet_accounts_response = self.WalletAPI.get_accounts(self.access_token)
        logger.debug("response body: %s", get_wallet_accounts_response.to_json())
        self.assertEqual('OK', get_wallet_accounts_response.code)

    def test_get_deposit_bank_account(self):
        """
            Test case get_deposit_bank_account
        """
        get_wallet_accounts_response = self.WalletAPI.get_accounts(self.access_token)
        fiat_account_id = get_account_id(get_wallet_accounts_response, 'USD')
        get_deposit_bank_account_response = self.WalletAPI.get_deposit_bank_account(self.access_token,
                                                                                    fiat_account_id)
        logger.debug("response body: %s", get_deposit_bank_account_response.to_json())
        self.assertEqual('OK', get_deposit_bank_account_response.code)
        self.assertIsNotNone(get_deposit_bank_account_response.data)

    def test_get_deposit_address(self):
        """
            Test case get_deposit_address
        """
        get_wallet_accounts_response = self.WalletAPI.get_accounts(self.access_token)
        crypto_account_id = get_account_id(get_wallet_accounts_response, 'BNB')
        get_deposit_address_response = self.WalletAPI.get_deposit_address(self.access_token,
                                                                          crypto_account_id)
        logger.debug("response body: %s", get_deposit_address_response.to_json())
        self.assertEqual('OK', get_deposit_address_response.code)
        self.assertIsNotNone(get_deposit_address_response.data)

    def test_query_transactions(self):
        """
            Test case query_transactions
        """
        get_wallet_accounts_response = self.WalletAPI.get_accounts(self.access_token)
        fiat_account_id = get_account_id(get_wallet_accounts_response, 'USD')
        query_wallet_account_transactions_response = self.WalletAPI.query_transactions(self.access_token,
                                                                                       fiat_account_id)
        logger.debug("response body: %s", query_wallet_account_transactions_response.to_json())
        self.assertEqual('OK', query_wallet_account_transactions_response.code)
