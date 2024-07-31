from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import PaymentMethod


@dataclass_json
@dataclass
class PaymentMethodResponse:
    code: str
    msg: str
    data: Optional[PaymentMethod] = None
