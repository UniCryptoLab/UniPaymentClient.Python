from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import Invoice, InvoiceRefund
from unipayment.models import QueryResult


@dataclass_json
@dataclass
class QueryInvoiceRefundsResponse:
    code: str
    msg: str
    data: QueryResult[InvoiceRefund]
