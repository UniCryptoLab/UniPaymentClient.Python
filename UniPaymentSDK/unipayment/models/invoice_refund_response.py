from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import InvoiceRefund


@dataclass_json
@dataclass
class InvoiceRefundResponse:
    code: str
    msg: str
    data: Optional[InvoiceRefund] = None
