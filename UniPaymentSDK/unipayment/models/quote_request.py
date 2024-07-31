from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class QuoteRequest:
    from_currency: str
    to_currency: str
    exchange_amount: float
