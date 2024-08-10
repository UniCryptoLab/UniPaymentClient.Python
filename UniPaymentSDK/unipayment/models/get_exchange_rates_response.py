from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models import ExchangeRate


@dataclass_json
@dataclass
class GetExchangeRatesResponse:
    code: str
    msg: str
    data: List[ExchangeRate]
