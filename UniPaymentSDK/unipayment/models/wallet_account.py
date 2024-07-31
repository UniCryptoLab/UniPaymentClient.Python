from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import BankAccount


class AccountType(Enum):
    DEFAULT = "Default"
    SETTLEMENT = "Settlement"
    BANK = "Bank"


@dataclass_json
@dataclass
class WalletAccount:
    asset_type: str
    balance: float
    frozen_balance: float
    reversed_balance: float
    available: float
    type: AccountType
    id: Optional[str] = None
    friendly_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_account: Optional[BankAccount] = None
    status: Optional[str] = None
