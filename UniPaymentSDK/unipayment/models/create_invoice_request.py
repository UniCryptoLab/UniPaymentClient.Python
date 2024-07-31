from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from unipayment.models import ConfirmSpeed


@dataclass_json
@dataclass
class CreateInvoiceRequest:
    app_id: str
    price_amount: float
    price_currency: str
    order_id: str
    pay_currency: Optional[str] = None
    lang: Optional[str] = None
    ext_args: Optional[str] = None
    payment_method_type: Optional[str] = None
    pay_network: Optional[str] = None
    notify_url: Optional[str] = None
    redirect_url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    confirm_speed: Optional[ConfirmSpeed] = None
