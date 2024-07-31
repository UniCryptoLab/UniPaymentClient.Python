from __future__ import absolute_import
import unittest
import logging

from unipayment import BillingAPI, BeneficiaryAPI, CommonAPI, OauthTokenAPI, ExchangeAPI, PaymentAPI, WalletAPI
from unipayment import Configuration

logger = logging.getLogger(__name__)


class TestBaseClient(unittest.TestCase):

    def setUp(self):
        self.configuration = Configuration()
        self.configuration.client_id = '74feb539-ba5a-4ae9-b901-4da4fb539574'
        self.configuration.client_secret = 'BsoRhgqzhR1TYMtwTRYdPxBTvR5rxkW9K'
        self.configuration.app_id = "2a9bd90b-fe95-4659-83cb-04de662fbbac"
        self.configuration.debug = True
        self.CommonAPI = CommonAPI(self.configuration)
        self.OauthTokenAPI = OauthTokenAPI(self.configuration)
        self.BeneficiaryAPI = BeneficiaryAPI(self.configuration)
        self.ExchangeAPI = ExchangeAPI(self.configuration)
        self.WalletAPI = WalletAPI(self.configuration)
        self.PaymentAPI = PaymentAPI(self.configuration)
        self.BillingAPI = BillingAPI(self.configuration)

        if self.configuration.debug:
            logger.setLevel(logging.DEBUG)

        token_response = self.OauthTokenAPI.get_access_token()
        self.assertIsNotNone(token_response)
        self.assertIsNotNone(token_response.access_token)
        self.access_token = token_response.access_token

    def tearDown(self):
        pass
