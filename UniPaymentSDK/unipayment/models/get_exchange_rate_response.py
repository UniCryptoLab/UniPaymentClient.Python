from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import ExchangeRate


@dataclass_json
@dataclass
class GetExchangeRateResponse:
    code: str
    msg: str
    data: ExchangeRate
