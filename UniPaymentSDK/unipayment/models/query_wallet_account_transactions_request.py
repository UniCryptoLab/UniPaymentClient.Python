from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json


class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    DEPOSITPAYMENT = "DEPOSITPAYMENT"
    PAYMENTFEE = "PAYMENTFEE"
    FEEADJUSTMENT = "FEEADJUSTMENT"
    ADJUSTMENTSWAP = "ADJUSTMENTSWAP"
    SWAPINVOICE = "SWAPINVOICE"
    INVOICEREFUND = "INVOICEREFUND"
    REFUND = "REFUND"


@dataclass_json
@dataclass
class QueryWalletAccountTransactionsRequest:
    def __init__(self, page_no=1, page_size=20, is_asc=True, txn_type: TransactionType = None):
        self.page_no = page_no
        self.page_size = page_size
        self.is_asc = is_asc
        self.txn_type = txn_type

    def to_str(self):
        query_params = {
            "page_no": self.page_no,
            "page_size": self.page_size,
            "is_asc": str(self.is_asc).lower()
        }
        if self.txn_type:
            query_params["txn_type"] = self.txn_type.value
        return query_params
