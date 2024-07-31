from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models import PaymentMethod


@dataclass_json
@dataclass
class QueryPaymentMethodsResponse:
    code: str
    msg: str
    data: List[PaymentMethod]
