from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import ExchangeOrder


@dataclass_json
@dataclass
class AcceptQuoteResponse:
    code: str
    msg: str
    data: ExchangeOrder
