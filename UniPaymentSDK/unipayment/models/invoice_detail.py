from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import dataclass_json, config
from marshmallow import fields

from unipayment.models import PaymentMethodType, ConfirmSpeed, InvoiceStatus, Transaction


@dataclass_json
@dataclass
class InvoiceDetail:
    app_id: str
    invoice_id: str
    payment_method_type: PaymentMethodType
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
    invoice_url: str
    transactions: List[Transaction]
    network: Optional[str] = None
    address: Optional[str] = None
    pay_currency: Optional[str] = None
    error_status: Optional[str] = None
