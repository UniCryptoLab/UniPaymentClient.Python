from dataclasses import dataclass, field
from enum import Enum

from dataclasses_json import dataclass_json, config
from typing import Optional
from datetime import datetime

from marshmallow import fields


@dataclass_json
@dataclass
class PaymentDestination:
    network: str
    address: str


class PaymentStatus(Enum):
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


@dataclass_json
@dataclass
class Payment:
    id: str
    customer_id: str
    transfer_method: str
    network: str
    asset_type: str
    from_account_id: str
    destination: PaymentDestination
    amount: float
    create_time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    update_time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    fee: Optional[float] = None
    total_amount: Optional[float] = None
    reference: Optional[str] = None
    reason: Optional[str] = None
    note: Optional[str] = None
    status: Optional[PaymentStatus] = None
