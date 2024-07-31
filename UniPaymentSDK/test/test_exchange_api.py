from __future__ import absolute_import

import logging
import uuid

from test.test_base_client import TestBaseClient
from unipayment.models import QueryExchangeOrdersRequest, QuoteRequest

logger = logging.getLogger(__name__)


class TestExchangeAPI(TestBaseClient):
    pass

    def test_get_quote(self):
        """
            Test case get_quote
        """

        quote_request = QuoteRequest(
            from_currency='USDT',
            to_currency='BNB',
            exchange_amount='100')

        quote_response = self.ExchangeAPI.get_quote(self.access_token, quote_request)
        logger.debug("response body: %s", quote_response.to_json())
        self.assertEqual('OK', quote_response.code)
        self.assertIsNotNone(quote_response.data.quote_id)

    def test_accept_quote(self):
        """
            Test case accept_quote
        """

        """ Set Quote ID """
        quote_id = uuid.uuid4()
        accept_quote_response = self.ExchangeAPI.accept_quote(self.access_token, quote_id)
        logger.debug("response body: %s", accept_quote_response.to_json())
        self.assertEqual('OK', accept_quote_response.code)

    def test_query_exchange_orders(self):
        """
            Test case query_exchange_orders
        """

        query_exchange_orders_request = QueryExchangeOrdersRequest()
        query_exchange_orders_response = self.ExchangeAPI.query_exchange_orders(self.access_token,
                                                                                query_exchange_orders_request)
        logger.debug("response body: %s", query_exchange_orders_response.to_json())
        self.assertEqual('OK', query_exchange_orders_response.code)

    def test_query_exchange_order_by_order_id(self):
        """
            Test case query_exchange_order_by_order_id
        """

        """ Set Order ID """
        order_id = uuid.uuid4()
        query_exchange_order_response = self.ExchangeAPI.query_exchange_order_by_order_id(self.access_token, order_id)
        logger.debug("response body: %s", query_exchange_order_response.to_json())
        self.assertEqual('OK', query_exchange_order_response.code)
