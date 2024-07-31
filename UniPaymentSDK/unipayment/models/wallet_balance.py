from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WalletBalance:
    asset_type: str
    balance: float
    frozen_balance: float
    reversed_balance: float
    available: float
    id: Optional[str] = None
