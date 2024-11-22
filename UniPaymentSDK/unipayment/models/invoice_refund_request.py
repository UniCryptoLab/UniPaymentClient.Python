from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class InvoiceRefundRequest:
    refund_price_amount: float
    price_currency: str
    fee_payer: str
    reason: str
