from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import BankInfo
from unipayment.models import Beneficiary


@dataclass_json
@dataclass
class DepositBankAccount:
    network: str
    account_number: str
    iban: Optional[str] = None
    bic: Optional[str] = None
    routing_number: Optional[str] = None
    beneficiary: Optional[Beneficiary] = None
    bank_info: Optional[BankInfo] = None
    reference: Optional[str] = None
