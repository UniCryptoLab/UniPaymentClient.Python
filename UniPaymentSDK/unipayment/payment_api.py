import json

from .base_client import BaseClient
from .models.create_payment_request import CreatePaymentRequest
from .models.get_payment_fee_response import GetPaymentFeeResponse
from .models.payment_note import PaymentNote
from .models.payment_response import PaymentResponse
from .models.query_payments_request import QueryPaymentsRequest
from .models.query_payments_response import QueryPaymentsResponse


class PaymentAPI(BaseClient):
    pass

    def create_payment(self, create_payment_request: CreatePaymentRequest) -> PaymentResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments'
        response_text = self.call_api(url, 'POST', body=json.loads(create_payment_request.to_json()))
        return PaymentResponse.from_json(response_text)

    def get_payment_by_id(self, payment_id) -> PaymentResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments/{payment_id}'
        response_text = self.call_api(url, 'GET')
        return PaymentResponse.from_json(response_text)

    def query_payments(self,
                       query_payments_request: QueryPaymentsRequest = None) -> QueryPaymentsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments'
        if query_payments_request is None:
            query_payments_request = QueryPaymentsRequest()
        response_text = self.call_api(url, 'GET', query_params=query_payments_request.to_str())
        return QueryPaymentsResponse.from_json(response_text)

    def confirm_payment(self, payment_id, payment_note: PaymentNote) -> PaymentResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments/{payment_id}/confirm'
        response_text = self.call_api(url, 'PUT', body=json.loads(payment_note.to_json()))
        return PaymentResponse.from_json(response_text)

    def cancel_payment(self, payment_id, payment_note: PaymentNote) -> PaymentResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments/{payment_id}/cancel'
        response_text = self.call_api(url, 'PUT', body=json.loads(payment_note.to_json()))
        return PaymentResponse.from_json(response_text)

    def get_payment_fee(self, asset_type) -> GetPaymentFeeResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/payments/fee'
        response_text = self.call_api(url, 'GET', query_params={"asset_type": asset_type})
        return GetPaymentFeeResponse.from_json(response_text)
