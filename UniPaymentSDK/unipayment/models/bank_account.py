from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BankAccount:
    bank_name: str
    account_number: str
