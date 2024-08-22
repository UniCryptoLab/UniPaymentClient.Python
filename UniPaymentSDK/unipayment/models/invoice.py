from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json, config
from marshmallow import fields

from unipayment.models.host_to_host_data import HostToHostData


class PaymentMethodType(Enum):
    CRYPTO = "CRYPTO"
    CARD = "CARD"
    SKRILL = "SKRILL"
    UNKNOWN = "UNKNOWN"


class InvoiceStatus(Enum):
    NEW = "New"
    PAID = "Paid"
    CONFIRMED = "Confirmed"
    COMPLETE = "Complete"
    EXPIRED = "Expired"
    INVALID = "Invalid"


class InvoiceErrorStatus(Enum):
    NONE = "None"
    PAID_LATE = "PaidLate"
    PAID_PARTIAL = "PaidPartial"
    PAID_OVER = "PaidOver"
    MARKED = "Marked"


class ConfirmSpeed(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass_json
@dataclass
class Invoice:
    app_id: str
    invoice_id: str
    payment_method_type: PaymentMethodType
    host_to_host_mode: bool
    order_id: str
    price_amount: float
    price_currency: str
    pay_amount: float
    exchange_rate: float
    paid_amount: float
    refunded_price_amount: float
    create_time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    expiration_time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    confirm_speed: ConfirmSpeed
    status: InvoiceStatus
    error_status: InvoiceErrorStatus
    invoice_url: str
    network: Optional[str] = None
    address: Optional[str] = None
    pay_currency: Optional[str] = None
    host_to_host_data: Optional[HostToHostData] = None
