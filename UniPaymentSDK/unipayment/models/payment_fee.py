from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PaymentFee:
    asset_type: str
    network: str
    fee_type: str
    fee_rate: float
    flat_rate: float
    min_txn_fee: float
    max_txn_fee: float
