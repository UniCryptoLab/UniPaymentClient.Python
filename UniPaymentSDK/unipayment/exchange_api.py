from .base_client import BaseClient
from .models.accept_quote_response import AcceptQuoteResponse
from .models.query_exchange_order_response import QueryExchangeOrderResponse
from .models.query_exchange_orders_request import QueryExchangeOrdersRequest
from .models.query_exchange_orders_response import QueryExchangeOrdersResponse
from .models.quote_request import QuoteRequest
from .models.quote_response import QuoteResponse


class ExchangeAPI(BaseClient):
    pass

    def get_quote(self, quote_request: QuoteRequest) -> QuoteResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/exchange/quote'
        response_text = self.call_api(url, 'GET', query_params=quote_request.to_str())
        return QuoteResponse.from_json(response_text)

    def accept_quote(self, quote_id) -> AcceptQuoteResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/exchange/quote/{quote_id}'
        response_text = self.call_api(url, 'PUT')
        return AcceptQuoteResponse.from_json(response_text)

    def query_exchange_orders(self,
                              query_exchange_orders_request: QueryExchangeOrdersRequest = None) -> QueryExchangeOrdersResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/exchange/orders'

        if query_exchange_orders_request is None:
            query_exchange_orders_request = QueryExchangeOrdersRequest()

        response_text = self.call_api(url, 'GET', query_params=query_exchange_orders_request.to_str())
        return QueryExchangeOrdersResponse.from_json(response_text)

    def query_exchange_order_by_order_id(self, exchange_order_id) -> QueryExchangeOrderResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/exchange/orders/{exchange_order_id}'

        response_text = self.call_api(url, 'GET')
        return QueryExchangeOrderResponse.from_json(response_text)
