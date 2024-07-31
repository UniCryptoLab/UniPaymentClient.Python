from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import Invoice
from unipayment.models import QueryResult


@dataclass_json
@dataclass
class QueryInvoicesResponse:
    code: str
    msg: str
    data: QueryResult[Invoice]
