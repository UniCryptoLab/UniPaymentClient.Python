from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional
from datetime import datetime

from marshmallow import fields


@dataclass_json
@dataclass
class Quote:
    quote_id: str
    from_currency: str
    to_currency: str
    valid_until: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    requested_amount: Optional[float] = None
    exchange_rate: Optional[float] = None
    gross_amount: Optional[float] = None
    net_amount: Optional[float] = None
    fee_currency: Optional[str] = None
    fee: Optional[float] = None
