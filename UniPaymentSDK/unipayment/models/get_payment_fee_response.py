from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models import PaymentFee


@dataclass_json
@dataclass
class GetPaymentFeeResponse:
    code: str
    msg: str
    data: List[PaymentFee]
