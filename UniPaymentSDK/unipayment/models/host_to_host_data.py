from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class HostToHostData:
    network: str
    address: str
    pay_amount: float
    pay_currency: str
    type: str
