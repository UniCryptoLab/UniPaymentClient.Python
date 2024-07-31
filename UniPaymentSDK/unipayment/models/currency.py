from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Currency:
    code: str
    name: str
    is_fiat: bool
    divisibility: int
