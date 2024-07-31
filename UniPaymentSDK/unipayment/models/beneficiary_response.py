from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import Beneficiary


@dataclass_json
@dataclass
class BeneficiaryResponse:
    code: str
    msg: str
    data: Optional[Beneficiary] = None
