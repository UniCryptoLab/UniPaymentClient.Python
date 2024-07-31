from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from dataclasses_json import dataclass_json, config
from marshmallow import fields


@dataclass_json
@dataclass
class ExchangeOrder:
    id: str
    quote_id: str
    from_currency: str
    to_currency: str
    status: str
    create_time: datetime = field(
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
    valid_until: Optional[datetime] = None
    exchange_amount: Optional[float] = None
