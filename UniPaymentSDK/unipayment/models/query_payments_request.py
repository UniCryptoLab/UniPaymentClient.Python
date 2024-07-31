from unipayment.models import PaymentStatus
from unipayment.models import TransferMode


class QueryPaymentsRequest(object):
    def __init__(self, page_no=1,
                 page_size=10,
                 is_asc=True,
                 from_account_id=None,
                 to_account_id=None,
                 transfer_method: TransferMode = None,
                 payment_method_id=None,
                 crypto_address=None,
                 bank_account=None,
                 asset_type=None,
                 status: PaymentStatus = None):
        self.page_no = page_no
        self.page_size = page_size
        self.is_asc = is_asc
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
        self.transfer_method = transfer_method
        self.payment_method_id = payment_method_id
        self.crypto_address = crypto_address
        self.bank_account = bank_account
        self.asset_type = asset_type
        self.status = status

    def to_str(self):
        query_params = {
            "page_no": self.page_no,
            "page_size": self.page_size,
            "is_asc": str(self.is_asc).lower()
        }

        if self.from_account_id is not None:
            query_params['from_account_id'] = self.from_account_id
        if self.to_account_id is not None:
            query_params['to_account_id'] = self.to_account_id
        if self.transfer_method is not None:
            query_params['transfer_method'] = self.transfer_method
        if self.payment_method_id is not None:
            query_params['payment_method_id'] = self.payment_method_id
        if self.crypto_address is not None:
            query_params['crypto_address'] = self.crypto_address
        if self.from_account_id is not None:
            query_params['bank_account'] = self.bank_account
        if self.asset_type is not None:
            query_params['asset_type'] = self.asset_type
        if self.status is not None:
            query_params['status'] = self.status

        return query_params
