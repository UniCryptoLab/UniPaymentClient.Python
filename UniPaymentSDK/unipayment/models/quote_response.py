from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import Quote


@dataclass_json
@dataclass
class QuoteResponse:
    code: str
    msg: str
    data: Quote
