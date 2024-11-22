class QueryInvoiceRefundRequest(object):
    def __init__(self, page_no=1, page_size=10, is_asc=True, invoice_id=None, status=None,
                 start=None, end=None):
        self.page_no = page_no
        self.page_size = page_size
        self.is_asc = is_asc
        self.invoice_id = invoice_id
        self.status = status
        self.start = start
        self.end = end

    def to_str(self):
        query_params = {
            "page_no": self.page_no,
            "page_size": self.page_size,
            "is_asc": str(self.is_asc).lower()
        }
        if self.invoice_id:
            query_params["invoice_id"] = self.invoice_id
        if self.status:
            query_params["status"] = self.status
        if self.start:
            query_params["start"] = self.start
        if self.end:
            query_params["end"] = self.end
        return query_params
