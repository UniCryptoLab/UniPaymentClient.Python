from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ExchangeRateModel:
    to_currency: str
    from_currency: str
    rate: float
    ask: float
    bid: float
