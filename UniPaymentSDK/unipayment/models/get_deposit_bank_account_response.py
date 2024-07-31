from dataclasses import dataclass
from typing import Optional, List

from dataclasses_json import dataclass_json

from unipayment.models import DepositBankAccount


@dataclass_json
@dataclass
class GetDepositBankAccountResponse:
    code: str
    msg: str
    data: Optional[List[DepositBankAccount]]
