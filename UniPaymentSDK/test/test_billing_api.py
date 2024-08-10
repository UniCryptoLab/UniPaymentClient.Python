from __future__ import absolute_import

import logging
import uuid

import pytest

from test.test_base_client import TestBaseClient
from unipayment.models import CreateInvoiceRequest, QueryInvoicesRequest

logger = logging.getLogger(__name__)


class TestBillingAPI(TestBaseClient):
    pass

    @pytest.mark.order(1)
    def test_create_invoice(self):
        """
            Test case create_invoice
        """
        order_id = uuid.uuid4()
        create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=2.0,
                                                      price_currency='USD', order_id=order_id, lang='en',
                                                      ext_args='"Merchant Pass Through Data')
        create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
        logger.debug("response body: %s", create_invoice_response)
        self.assertEqual('OK', create_invoice_response.code)

    @pytest.mark.order(2)
    def test_query_invoices(self):
        """
            Test case query_invoices
        """

        query_invoices_request = QueryInvoicesRequest(app_id=self.configuration.app_id)
        query_invoices_response = self.BillingAPI.query_invoices(query_invoices_request)
        logger.debug("response body: %s", query_invoices_response)
        self.assertEqual('OK', query_invoices_response.code)

    @pytest.mark.order(3)
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
