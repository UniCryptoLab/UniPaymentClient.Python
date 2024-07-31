from dataclasses import dataclass
from typing import Optional, List

from dataclasses_json import dataclass_json

from unipayment.models import DepositAddress


@dataclass_json
@dataclass
class GetDepositAddressResponse:
    code: str
    msg: str
    data: Optional[List[DepositAddress]] = None
