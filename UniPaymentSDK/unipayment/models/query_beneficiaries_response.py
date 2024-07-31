from dataclasses import dataclass

from dataclasses_json import dataclass_json

from unipayment.models import Beneficiary
from unipayment.models import QueryResult


@dataclass_json
@dataclass
class QueryBeneficiariesResponse:
    code: str
    msg: str
    data: QueryResult[Beneficiary]
