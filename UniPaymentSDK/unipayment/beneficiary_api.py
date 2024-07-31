from __future__ import absolute_import

import json

from .models import Beneficiary, PaymentMethod, PaymentMethodResponse, QueryPaymentMethodsResponse, \
    BeneficiaryResponse, QueryBeneficiariesRequest, QueryBeneficiariesResponse
from .base_client import BaseClient


class BeneficiaryAPI(BaseClient):
    pass

    def create_beneficiary(self, access_token, beneficiary: Beneficiary) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries'
        response_text = self.call_api(url, 'POST', access_token, body=json.loads(beneficiary.to_json()))
        return BeneficiaryResponse.from_json(response_text)

    def get_beneficiary_by_id(self, access_token, beneficiary_id) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'GET', access_token)
        return BeneficiaryResponse.from_json(response_text)

    def update_beneficiary_by_id(self, access_token, beneficiary_id, beneficiary: Beneficiary) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'PUT', access_token, body=json.loads(beneficiary.to_json()))
        return BeneficiaryResponse.from_json(response_text)

    def delete_beneficiary_by_id(self, access_token, beneficiary_id) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'DELETE', access_token)
        return BeneficiaryResponse.from_json(response_text)

    def query_beneficiaries(self, access_token,
                            query_beneficiaries_request: QueryBeneficiariesRequest = None) -> QueryBeneficiariesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries'

        if query_beneficiaries_request is None:
            query_beneficiaries_request = QueryBeneficiariesRequest()

        response_text = self.call_api(url, 'GET', access_token, query_params=query_beneficiaries_request.to_str())
        return QueryBeneficiariesResponse.from_json(response_text)

    def create_payment_method(self, access_token, beneficiary_id,
                              payment_method: PaymentMethod) -> PaymentMethodResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods'
        response_text = self.call_api(url, 'POST', access_token, body=json.loads(payment_method.to_json()))
        return PaymentMethodResponse.from_json(response_text)

    def update_payment_method(self, access_token, beneficiary_id, payment_method_id,
                              payment_method: PaymentMethod) -> PaymentMethodResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods/{payment_method_id}'
        response_text = self.call_api(url, 'PUT', access_token, body=json.loads(payment_method.to_json()))
        return PaymentMethodResponse.from_json(response_text)

    def get_payment_method_by_id(self, access_token, beneficiary_id, payment_method_id) -> PaymentMethodResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods/{payment_method_id}'
        response_text = self.call_api(url, 'GET', access_token)
        return PaymentMethodResponse.from_json(response_text)

    def query_payment_methods(self, access_token, beneficiary_id) -> QueryPaymentMethodsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods'
        response_text = self.call_api(url, 'GET', access_token)
        return QueryPaymentMethodsResponse.from_json(response_text)

    def delete_payment_method_by_id(self, access_token, beneficiary_id, payment_method_id) -> PaymentMethodResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods/{payment_method_id}'
        response_text = self.call_api(url, 'DELETE', access_token)
        return PaymentMethodResponse.from_json(response_text)
