from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import Payment


@dataclass_json
@dataclass
class PaymentResponse:
    code: str
    msg: str
    data: Optional[Payment]
