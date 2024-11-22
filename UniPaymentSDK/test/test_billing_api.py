from __future__ import absolute_import

import logging
import uuid

import pytest

from test.test_base_client import TestBaseClient
from unipayment.models import CreateInvoiceRequest, QueryInvoicesRequest, BuyerInfo, InvoiceRefundRequest, \
    CancelInvoiceRefundRequest, QueryInvoiceRefundRequest

logger = logging.getLogger(__name__)


class TestBillingAPI(TestBaseClient):
    pass

    @pytest.mark.order(1)
    def test_create_invoice(self):
        """
            Test case create_invoice
        """
        order_id = uuid.uuid4()
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=20.0,
                                                      price_currency='USD', order_id=order_id, lang='en',
                                                      ext_args='"Merchant Pass Through Data')
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        logger.debug("response body: %s", create_invoice_response)
        self.assertEqual('OK', create_invoice_response.code)

    @pytest.mark.order(2)
    def test_create_invoice_refund(self):
        """
            Test case create_invoice_refund
        """
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=20.0,
                                                      price_currency='USD', order_id=uuid.uuid4(), lang='en',
                                                      ext_args='"Merchant Pass Through Data')
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        self.assertEqual('OK', create_invoice_response.code)

        invoice_refund_request = InvoiceRefundRequest(refund_price_amount=20.0, price_currency='USD',
                                                      fee_payer="MERCHANT", reason="Refund")
        invoice_refund_response = self.BillingAPI.create_invoice_refund(create_invoice_response.data.invoice_id,
                                                                        invoice_refund_request)
        logger.debug("response body: %s", invoice_refund_response)
        self.assertEqual('OK', invoice_refund_response.code)

    @pytest.mark.order(3)
    def test_query_invoice_refunds(self):
        """
            Test case query_invoice_refunds
        """

        query_invoice_refunds_request = QueryInvoiceRefundRequest()
        query_invoice_refunds_response = self.BillingAPI.query_invoice_refunds(query_invoice_refunds_request)
        logger.debug("response body: %s", query_invoice_refunds_response)
        self.assertEqual('OK', query_invoice_refunds_response.code)

    @pytest.mark.order(4)
    def test_cancel_invoice_refund(self):
        """
            Test case cancel_invoice_refund
        """
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=20.0,
                                                      price_currency='USD', order_id=uuid.uuid4(), lang='en',
                                                      ext_args='"Merchant Pass Through Data')
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        self.assertEqual('OK', create_invoice_response.code)

        invoice_refund_request = InvoiceRefundRequest(refund_price_amount=20.0, price_currency='USD',
                                                      fee_payer="MERCHANT", reason="Refund")
        invoice_refund_response = self.BillingAPI.create_invoice_refund(create_invoice_response.data.invoice_id,
                                                                        invoice_refund_request)

        self.assertEqual('OK', invoice_refund_response.code)

        cancel_invoice_refund_request = CancelInvoiceRefundRequest(note="Cancellation")
        cancel_invoice_refund_response = self.BillingAPI.cancel_invoice_refund(invoice_refund_response.data.refund_id,
                                                                               cancel_invoice_refund_request)
        logger.debug("response body: %s", cancel_invoice_refund_response)
        self.assertEqual('OK', cancel_invoice_refund_response.code)

    @pytest.mark.order(5)
    def test_query_invoices(self):
        """
            Test case query_invoices
        """

        query_invoices_request = QueryInvoicesRequest(app_id=self.configuration.app_id)
        query_invoices_response = self.BillingAPI.query_invoices(query_invoices_request)
        logger.debug("response body: %s", query_invoices_response)
        self.assertEqual('OK', query_invoices_response.code)

    @pytest.mark.order(6)
    def test_get_invoice_by_id(self):
        """
            Test case get_invoice_by_id
        """

        query_invoices_request = QueryInvoicesRequest(app_id=self.configuration.app_id)
        query_invoices_response = self.BillingAPI.query_invoices(query_invoices_request)
        invoice_id = query_invoices_response.data.models[0].get("invoice_id")

        get_invoice_by_id_response = self.BillingAPI.get_invoice_by_id(invoice_id)
        logger.debug("response body: %s", get_invoice_by_id_response)
        self.assertEqual('OK', get_invoice_by_id_response.code)

    @pytest.mark.order(7)
    def test_create_invoice_host_to_host(self):
        """
            Test case create_invoice
        """
        order_id = uuid.uuid4()
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=20.0,
                                                      price_currency='USD', order_id=order_id, lang='en',
                                                      ext_args='"Merchant Pass Through Data', host_to_host_mode=True,
                                                      payment_method_type='CRYPTO', pay_currency='UTT',
                                                      network='NETWORK_BSC')
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        logger.debug("response body: %s", create_invoice_response)
        self.assertEqual('OK', create_invoice_response.code)

    @pytest.mark.order(8)
    def test_create_invoice_buyer_info(self):
        """
            Test case create_invoice
        """
        order_id = uuid.uuid4()
        buyer_info = BuyerInfo(name='John Doe', email='john@doe.com', phone='555-555-5555', address1='123 Main Street',
                               address2="", state='NYC', country='US', zip_code='12345', city='San Francisco', )
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=20.0,
                                                      price_currency='USD', order_id=order_id, lang='en',
                                                      ext_args='"Merchant Pass Through Data', buyer_info=buyer_info)
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        logger.debug("response body: %s", create_invoice_response)
        self.assertEqual('OK', create_invoice_response.code)
