from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import ExchangeOrder
from unipayment.models import QueryResult


@dataclass_json
@dataclass
class QueryExchangeOrdersResponse:
    code: str
    msg: str
    data: QueryResult[ExchangeOrder]
