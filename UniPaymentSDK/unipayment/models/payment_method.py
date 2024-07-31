from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json


class TransferMode(Enum):
    BANK = "BANK"
    CRYPTO = "CRYPTO"
    INTERNAL = "INTERNAL"


@dataclass_json
@dataclass
class PaymentMethodDetail:
    asset_type: str


@dataclass_json
@dataclass
class PaymentMethod:
    title: str
    transfer_method: TransferMode
    detail: PaymentMethodDetail
    id: Optional[str] = None
    beneficiary_id: Optional[str] = None


@dataclass_json
@dataclass
class BankPaymentMethodDetail(PaymentMethodDetail):
    network: str
    account_number: str
    iban: Optional[str] = None
    bic: Optional[str] = None
    routing_number: Optional[str] = None
    bank_identifier: Optional[str] = None
    reference: Optional[str] = None
    bank_name: Optional[str] = None
    bank_address: Optional[str] = None
    bank_country: Optional[str] = None
    intermediary_bank_name: Optional[str] = None
    intermediary_account_number: Optional[str] = None
    intermediary_bic: Optional[str] = None


@dataclass_json
@dataclass
class CryptoPaymentMethodDetail(PaymentMethodDetail):
    network: str
    address: str


@dataclass_json
@dataclass
class InternalPaymentMethodDetail(PaymentMethodDetail):
    uid: str
