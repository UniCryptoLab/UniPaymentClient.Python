from dataclasses import dataclass
from dataclasses_json import dataclass_json

from unipayment.models import Payment
from unipayment.models import QueryResult


@dataclass_json
@dataclass
class QueryPaymentsResponse:
    code: str
    msg: str
    data: QueryResult[Payment]
