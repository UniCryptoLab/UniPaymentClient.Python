from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models import Currency


@dataclass_json
@dataclass
class GetCurrenciesResponse:
    code: str
    msg: str
    data: List[Currency]
