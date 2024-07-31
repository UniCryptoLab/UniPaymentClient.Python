from __future__ import absolute_import

import logging
from typing import Optional

import pytest

from test.test_base_client import TestBaseClient
from unipayment.models import Beneficiary, BeneficiaryType, Relationship, PaymentMethod, TransferMode, \
    InternalPaymentMethodDetail, QueryBeneficiariesResponse, QueryPaymentMethodsResponse

logger = logging.getLogger(__name__)


def get_beneficiary_id(response: QueryBeneficiariesResponse, email) -> Optional[str]:
    for beneficiary in response.data.models:
        if beneficiary.get('email') == email:
            return beneficiary.get('id')
    return None


def get_payment_method_id(response: QueryPaymentMethodsResponse, transfer_method: TransferMode) -> Optional[str]:
    for payment_method in response.data:
        if transfer_method != payment_method.transfer_method:
            continue
        return payment_method.id
    return None


class TestOauthTokenAPI(TestBaseClient):
    pass

    @pytest.mark.order(1)
    def test_create_beneficiary(self):
        """
            Test case create_beneficiary
        """

        beneficiary = Beneficiary(
            name="John Doe",
            email="john.doe@example.com",
            type=BeneficiaryType.INDIVIDUAL,
            relationship=Relationship.CUSTOMER,
            address="123 Main St",
            city="Springfield",
            state="IL",
            country="US",
            zip_code="62704"
        )
        create_beneficiary_response = self.BeneficiaryAPI.create_beneficiary(self.access_token, beneficiary)
        logger.debug("response body: %s", create_beneficiary_response.to_json())
        self.assertEqual('OK', create_beneficiary_response.code)
        self.assertIsNotNone(create_beneficiary_response.data.id)

    @pytest.mark.order(2)
    def test_query_beneficiaries(self):
        """
            Test case query_beneficiaries
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        logger.debug("response body: %s", query_beneficiaries_response.to_json())
        self.assertEqual('OK', query_beneficiaries_response.code)
        self.assertIsNotNone(query_beneficiaries_response.data)

    @pytest.mark.order(3)
    def test_get_beneficiary_by_id(self):
        """
            Test case get_beneficiary_by_id
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')

        beneficiary_response = self.BeneficiaryAPI.get_beneficiary_by_id(self.access_token, beneficiary_id)
        logger.debug("response body: %s", beneficiary_response.to_json())
        self.assertEqual('OK', beneficiary_response.code)
        self.assertIsNotNone(beneficiary_response.data.id)

    @pytest.mark.order(4)
    def test_create_payment_method(self):
        """
            Test case create_payment_method
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')

        payment_method_detail = InternalPaymentMethodDetail(asset_type='USDT', uid='1000000')
        internal_payment_method = PaymentMethod(title='internal', transfer_method=TransferMode.INTERNAL,
                                                detail=payment_method_detail)
        payment_method_response = self.BeneficiaryAPI.create_payment_method(self.access_token, beneficiary_id,
                                                                            internal_payment_method)
        logger.debug("response body: %s", payment_method_response.to_json())
        self.assertEqual('OK', payment_method_response.code)

    @pytest.mark.order(5)
    def test_query_payment_methods(self):
        """
            Test case query_payment_methods
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')

        query_payment_methods_response = self.BeneficiaryAPI.query_payment_methods(self.access_token, beneficiary_id)
        logger.debug("response body: %s", query_payment_methods_response.to_json())
        self.assertEqual('OK', query_payment_methods_response.code)

    @pytest.mark.order(6)
    def test_get_payment_method_by_id(self):
        """
            Test case query_payment_methods
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')

        query_payment_methods_response = self.BeneficiaryAPI.query_payment_methods(self.access_token, beneficiary_id)
        payment_method_id = get_payment_method_id(query_payment_methods_response, TransferMode.INTERNAL)

        get_payment_method_response = self.BeneficiaryAPI.get_payment_method_by_id(self.access_token, beneficiary_id,
                                                                                   payment_method_id)
        logger.debug("response body: %s", get_payment_method_response.to_json())
        self.assertEqual('OK', get_payment_method_response.code)

    @pytest.mark.order(7)
    def delete_payment_method_by_id(self):
        """
            Test case query_payment_methods
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')

        query_payment_methods_response = self.BeneficiaryAPI.query_payment_methods(self.access_token, beneficiary_id)
        payment_method_id = get_payment_method_id(query_payment_methods_response, TransferMode.INTERNAL)

        delete_payment_method_response = self.BeneficiaryAPI.delete_payment_method_by_id(self.access_token,
                                                                                         beneficiary_id,
                                                                                         payment_method_id)
        logger.debug("response body: %s", delete_payment_method_response.to_json())
        self.assertEqual('OK', delete_payment_method_response.code)

    @pytest.mark.order(8)
    def test_delete_beneficiary_by_id(self):
        """
            Test case delete_beneficiary_by_id
        """
        query_beneficiaries_response = self.BeneficiaryAPI.query_beneficiaries(self.access_token)
        beneficiary_id = get_beneficiary_id(query_beneficiaries_response, 'john.doe@example.com')
        beneficiary_response = self.BeneficiaryAPI.delete_beneficiary_by_id(self.access_token, beneficiary_id)
        logger.debug("response body: %s", beneficiary_response.to_json())
        self.assertEqual('OK', beneficiary_response.code)
        self.assertIsNone(beneficiary_response.data)
