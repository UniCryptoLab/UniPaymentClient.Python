from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional


class PaymentReason(Enum):
    INVESTMENTS = "Investments"
    INTERNAL_TRANSFER = "InternalTransfer"
    INVOICE_FOR_SERVICES_OR_GOODS = "InvoiceForServicesOrGoods"
    OPERATING_EXPENSE = "OperatingExpense"
    STAFF_COSTS = "StaffCosts"
    SETTLING_CLIENT_FUNDS = "SettlingClientFunds"
    SETTLING_TRADING_COUNTERPARTY_FUNDS = "SettlingTradingCounterpartyFunds"
    OTHER = "Other"


@dataclass_json
@dataclass
class CreatePaymentRequest:
    from_account_id: str
    asset_type: str
    amount: float
    reason: PaymentReason
    payment_method_id: Optional[str] = None
    to_account_id: Optional[str] = None
    reference: Optional[str] = None
    note: Optional[str] = None
    unique_id: Optional[str] = None
