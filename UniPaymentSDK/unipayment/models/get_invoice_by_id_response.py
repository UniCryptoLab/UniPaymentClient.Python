from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import InvoiceDetail


@dataclass_json
@dataclass
class GetInvoiceByIdResponse:
    code: str
    msg: str
    data: InvoiceDetail
