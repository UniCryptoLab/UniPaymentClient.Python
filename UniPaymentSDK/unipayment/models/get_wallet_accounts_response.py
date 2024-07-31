from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models import WalletBalance


@dataclass_json
@dataclass
class GetWalletAccountsResponse:
    code: str
    msg: str
    data: List[WalletBalance]
