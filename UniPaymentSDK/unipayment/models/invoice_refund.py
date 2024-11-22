from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json, config
from marshmallow import fields


@dataclass_json
@dataclass
class InvoiceRefund:
    refund_id: str
    invoice_id: str
    price_currency: str
    refund_price_amount: float
    fee_payer: str
    fee: float
    reason: str
    status: str
    create_time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
