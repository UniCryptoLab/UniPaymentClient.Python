from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Transaction:
    hash: str
    network: str
    symbol: str
    from_address: str
    to_address: str
    amount: float
    confirmation_count: int
    is_confirmed: Optional[bool] = None
