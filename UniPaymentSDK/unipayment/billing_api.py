import json

from .models.create_invoice_request import CreateInvoiceRequest
from .models.create_invoice_response import CreateInvoiceResponse
from .models.get_invoice_by_id_response import GetInvoiceByIdResponse
from .models.query_invoices_request import QueryInvoicesRequest
from .models.query_invoices_response import QueryInvoicesResponse
from .base_client import BaseClient


class BillingAPI(BaseClient):
    pass

    def create_invoice(self, access_token, create_invoice_request: CreateInvoiceRequest) -> CreateInvoiceResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices'
        response_text = self.call_api(url, 'POST', access_token, body=json.loads(create_invoice_request.to_json()))
        return CreateInvoiceResponse.from_json(response_text)

    def get_invoice_by_id(self, access_token, invoice_id) -> GetInvoiceByIdResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/{invoice_id}'
        response_text = self.call_api(url, 'GET', access_token)
        print(response_text)
        return GetInvoiceByIdResponse.from_json(response_text)

    def query_invoices(self, access_token, query_invoices_request: QueryInvoicesRequest) -> QueryInvoicesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices'
        response_text = self.call_api(url, 'GET', access_token, query_params=query_invoices_request.to_str())
        return QueryInvoicesResponse.from_json(response_text)
