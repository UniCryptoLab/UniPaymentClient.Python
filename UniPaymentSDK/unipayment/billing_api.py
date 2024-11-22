import json

from .base_client import BaseClient
from .models import CancelInvoiceRefundRequest
from .models.create_invoice_request import CreateInvoiceRequest
from .models.create_invoice_response import CreateInvoiceResponse
from .models.get_invoice_by_id_response import GetInvoiceByIdResponse
from .models.invoice_refund_request import InvoiceRefundRequest
from .models.invoice_refund_response import InvoiceRefundResponse
from .models.query_invoice_refunds_request import QueryInvoiceRefundRequest
from .models.query_invoice_refunds_response import QueryInvoiceRefundsResponse
from .models.query_invoices_request import QueryInvoicesRequest
from .models.query_invoices_response import QueryInvoicesResponse


class BillingAPI(BaseClient):
    pass

    def create_invoice(self, create_invoice_request: CreateInvoiceRequest) -> CreateInvoiceResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices'
        response_text = self.call_api(url, 'POST', body=json.loads(create_invoice_request.to_json()))
        return CreateInvoiceResponse.from_json(response_text)

    def get_invoice_by_id(self, invoice_id) -> GetInvoiceByIdResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/{invoice_id}'
        response_text = self.call_api(url, 'GET')
        return GetInvoiceByIdResponse.from_json(response_text)

    def query_invoices(self, query_invoices_request: QueryInvoicesRequest) -> QueryInvoicesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices'
        response_text = self.call_api(url, 'GET', query_params=query_invoices_request.to_str())
        return QueryInvoicesResponse.from_json(response_text)

    def create_invoice_refund(self, invoice_id, invoice_refund_request: InvoiceRefundRequest) -> InvoiceRefundResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/{invoice_id}/refunds'
        response_text = self.call_api(url, 'POST', body=json.loads(invoice_refund_request.to_json()))
        return InvoiceRefundResponse.from_json(response_text)

    def get_invoice_refund_by_id(self, refund_id) -> InvoiceRefundResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/refunds/{refund_id}'
        response_text = self.call_api(url, 'GET')
        return InvoiceRefundResponse.from_json(response_text)

    def query_invoice_refunds(self,
                              query_invoice_refund_request: QueryInvoiceRefundRequest) -> QueryInvoiceRefundsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/refunds'
        response_text = self.call_api(url, 'GET', query_params=query_invoice_refund_request.to_str())
        return QueryInvoiceRefundsResponse.from_json(response_text)

    def cancel_invoice_refund(self, refund_id,
                              cancel_invoice_refund_request: CancelInvoiceRefundRequest) -> InvoiceRefundResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/invoices/refunds/{refund_id}/cancel'
        response_text = self.call_api(url, 'PUT', body=json.loads(cancel_invoice_refund_request.to_json()))
        return InvoiceRefundResponse.from_json(response_text)
