from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import Invoice


@dataclass_json
@dataclass
class CreateInvoiceResponse:
    code: str
    msg: str
    data: Invoice
