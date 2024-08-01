from __future__ import absolute_import

import logging
import uuid

import pytest

from test.test_base_client import TestBaseClient
from unipayment.models import PaymentNote, CreatePaymentRequest, PaymentReason, QueryPaymentsRequest

logger = logging.getLogger(__name__)


class TestPaymentAPI(TestBaseClient):
    pass

    @pytest.mark.order(1)
    def test_create_payment(self):
        """
            Test case create_payment
        """
        """ Set Correct Account IDs & Payment Method ID """
        create_payment_request = CreatePaymentRequest(
            from_account_id='d7c5db2e-8572-4a2f-9300-84dc4b3fd052',
            to_account_id='f0b4083b-8b43-4267-a321-f96bdba8c9e4',
            asset_type='USDT',
            amount=10,
            reason=PaymentReason.INTERNAL_TRANSFER,
            payment_method_id='5c0bce95-7d10-47f3-8e11-250ab900da07',
            unique_id=uuid.uuid4()
        )
        create_payment_response = self.PaymentAPI.create_payment(self.access_token, create_payment_request)
        logger.debug("response body: %s", create_payment_response.to_json())
        self.assertEqual('OK', create_payment_response.code)

    @pytest.mark.order(2)
    def test_get_payment_by_id(self):
        """
            Test case get_payment_by_id
        """

        """ Set Payment ID """
        payment_id = self.create_payment()

        get_payment_response = self.PaymentAPI.get_payment_by_id(self.access_token, payment_id)
        logger.debug("response body: %s", get_payment_response.to_json())
        self.assertEqual('OK', get_payment_response.code)
        self.assertIsNotNone(get_payment_response.data)

    @pytest.mark.order(3)
    def test_confirm_payment(self):
        """
            Test case confirm_payment
        """

        """ Set Payment ID """
        payment_id = self.create_payment()
        payment_note = PaymentNote(note="Payment Confirmed")
        confirm_payment_response = self.PaymentAPI.confirm_payment(self.access_token, payment_id, payment_note)
        logger.debug("response body: %s", confirm_payment_response.to_json())
        self.assertEqual('OK', confirm_payment_response.code)

    @pytest.mark.order(4)
    def test_cancel_payment(self):
        """
            Test case cancel_payment
        """

        """ Set Payment ID """
        payment_id = self.create_payment()
        payment_note = PaymentNote(note="Payment Cancelled")
        cancel_payment_response = self.PaymentAPI.cancel_payment(self.access_token, payment_id, payment_note)
        logger.debug("response body: %s", cancel_payment_response.to_json())
        self.assertEqual('OK', cancel_payment_response.code)

    @pytest.mark.order(5)
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

    def create_payment(self):
        create_payment_request = CreatePaymentRequest(
            from_account_id='d7c5db2e-8572-4a2f-9300-84dc4b3fd052',
            to_account_id='f0b4083b-8b43-4267-a321-f96bdba8c9e4',
            asset_type='USDT',
            amount=10,
            reason=PaymentReason.INTERNAL_TRANSFER,
            payment_method_id='5c0bce95-7d10-47f3-8e11-250ab900da07',
            unique_id=uuid.uuid4()
        )
        create_payment_response = self.PaymentAPI.create_payment(self.access_token, create_payment_request)
        return create_payment_response.data.id
