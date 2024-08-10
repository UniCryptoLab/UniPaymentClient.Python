from __future__ import absolute_import

import json

from .base_client import BaseClient
from .models import Beneficiary, PaymentMethod, PaymentMethodResponse, QueryPaymentMethodsResponse, \
    BeneficiaryResponse, QueryBeneficiariesRequest, QueryBeneficiariesResponse


class BeneficiaryAPI(BaseClient):
    pass

    def create_beneficiary(self, beneficiary: Beneficiary) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries'
        response_text = self.call_api(url, 'POST', body=json.loads(beneficiary.to_json()))
        return BeneficiaryResponse.from_json(response_text)

    def get_beneficiary_by_id(self, beneficiary_id) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'GET')
        return BeneficiaryResponse.from_json(response_text)

    def update_beneficiary_by_id(self, beneficiary_id, beneficiary: Beneficiary) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'PUT', body=json.loads(beneficiary.to_json()))
        return BeneficiaryResponse.from_json(response_text)

    def delete_beneficiary_by_id(self, beneficiary_id) -> BeneficiaryResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}'
        response_text = self.call_api(url, 'DELETE')
        return BeneficiaryResponse.from_json(response_text)

    def query_beneficiaries(self,
                            query_beneficiaries_request: QueryBeneficiariesRequest = None) -> QueryBeneficiariesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries'

        if query_beneficiaries_request is None:
            query_beneficiaries_request = QueryBeneficiariesRequest()

        response_text = self.call_api(url, 'GET', query_params=query_beneficiaries_request.to_str())
        return QueryBeneficiariesResponse.from_json(response_text)

    def create_payment_method(self, beneficiary_id,
                              payment_method: PaymentMethod) -> PaymentMethodResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment-methods'
        response_text = self.call_api(url, 'POST', body=json.loads(payment_method.to_json()))
        return PaymentMethodResponse.from_json(response_text)

    def update_payment_method(self, beneficiary_id, payment_method_id,
                              payment_method: PaymentMethod) -> PaymentMethodResponse:
        url = (f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment'
               f'-methods/{payment_method_id}')
        response_text = self.call_api(url, 'PUT', body=json.loads(payment_method.to_json()))
        return PaymentMethodResponse.from_json(response_text)

    def get_payment_method_by_id(self, beneficiary_id, payment_method_id) -> PaymentMethodResponse:
        url = (f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment'
               f'-methods/{payment_method_id}')
        response_text = self.call_api(url, 'GET')
        return PaymentMethodResponse.from_json(response_text)

    def query_payment_methods(self, beneficiary_id) -> QueryPaymentMethodsResponse:
        url = (f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment'
               f'-methods')
        response_text = self.call_api(url, 'GET')
        return QueryPaymentMethodsResponse.from_json(response_text)

    def delete_payment_method_by_id(self, beneficiary_id, payment_method_id) -> PaymentMethodResponse:
        url = (f'{self.configuration.host}/v{self.configuration.api_version}/beneficiaries/{beneficiary_id}/payment'
               f'-methods/{payment_method_id}')
        response_text = self.call_api(url, 'DELETE')
        return PaymentMethodResponse.from_json(response_text)
