from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import QueryResult
from unipayment.models import Transaction


@dataclass_json
@dataclass
class QueryWalletAccountTransactionsResponse:
    code: str
    msg: str
    data: QueryResult[Transaction]
