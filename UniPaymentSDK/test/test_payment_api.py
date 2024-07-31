from __future__ import absolute_import

import logging
import uuid

from test.test_base_client import TestBaseClient
from unipayment.models import PaymentNote, CreatePaymentRequest, PaymentReason, QueryPaymentsRequest

logger = logging.getLogger(__name__)


class TestPaymentAPI(TestBaseClient):
    pass

    def test_create_payment(self):
        """
            Test case create_payment
        """
        """ Set Correct Account IDs & Payment Method ID """
        create_payment_request = CreatePaymentRequest(
            from_account_id='4fc5f376-ca8a-479f-bf9a-4e6155ca1f9f',
            to_account_id='952af86c-21cf-4666-8de4-8fea61d4a31c',
            asset_type='UTT',
            amount=10,
            reason=PaymentReason.InternalTransfer,
            payment_method_id='cff91813-b4f0-4c6d-8f16-4094ad9f920e',
            unique_id=uuid.uuid4()
        )
        create_payment_response = self.PaymentAPI.create_payment(self.access_token, create_payment_request)
        logger.debug("response body: %s", create_payment_response.to_json())
        self.assertEqual('OK', create_payment_response.code)

    def test_get_payment_by_id(self):
        """
            Test case get_payment_by_id
        """

        """ Set Payment ID """
        payment_id = uuid.uuid4()

        get_payment_response = self.PaymentAPI.get_payment_by_id(self.access_token, payment_id)
        logger.debug("response body: %s", get_payment_response.to_json())
        self.assertEqual('OK', get_payment_response.code)
        self.assertIsNotNone(get_payment_response.data)

    def test_confirm_payment(self):
        """
            Test case confirm_payment
        """

        """ Set Payment ID """
        payment_id = uuid.uuid4()
        payment_note = PaymentNote(note="Payment Confirmed")
        confirm_payment_response = self.PaymentAPI.confirm_payment(self.access_token, payment_id, payment_note)
        logger.debug("response body: %s", confirm_payment_response.to_json())
        self.assertEqual('OK', confirm_payment_response.code)

    def test_cancel_payment(self):
        """
            Test case cancel_payment
        """

        """ Set Payment ID """
        payment_id = uuid.uuid4()
        payment_note = PaymentNote(note="Payment Cancelled")
        cancel_payment_response = self.PaymentAPI.cancel_payment(self.access_token, payment_id, payment_note)
        logger.debug("response body: %s", cancel_payment_response.to_json())
        self.assertEqual('OK', cancel_payment_response.code)

    def test_query_payments(self):
        """
            Test case query_payments
        """
        query_payments_request = QueryPaymentsRequest()
        query_payments_response = self.PaymentAPI.query_payments(self.access_token, query_payments_request)
        logger.debug("response body: %s", query_payments_response.to_json())
        self.assertEqual('OK', query_payments_response.code)
        self.assertIsNotNone(query_payments_response.data)

    def test_get_payment_fee(self):
        """
            Test case get_payment_fee
        """

        get_payment_fee_response = self.PaymentAPI.get_payment_fee(self.access_token, 'USDT')
        logger.debug("response body: %s", get_payment_fee_response.to_json())
        self.assertEqual('OK', get_payment_fee_response.code)
        self.assertIsNotNone(get_payment_fee_response.data)
