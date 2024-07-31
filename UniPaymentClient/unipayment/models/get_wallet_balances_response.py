from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from unipayment.models.wallet_balance import WalletBalance


@dataclass_json
@dataclass
class GetWalletBalanceResponse:
    code: str
    msg: str
    data: List[WalletBalance]
