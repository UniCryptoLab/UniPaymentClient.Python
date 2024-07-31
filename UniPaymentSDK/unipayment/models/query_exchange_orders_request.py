class QueryExchangeOrdersRequest(object):
    def __init__(self, page_no=1, page_size=10, is_asc=True, from_currency=None, to_currency=None):
        self.page_no = page_no
        self.page_size = page_size
        self.is_asc = is_asc
        self.from_currency = from_currency
        self.to_currency = to_currency

    def to_str(self):
        query_params = {
            "page_no": self.page_no,
            "page_size": self.page_size,
            "is_asc": str(self.is_asc).lower()
        }
        if self.from_currency is not None:
            query_params["from_currency"] = self.from_currency
        if self.to_currency is not None:
            query_params["to_currency"] = self.to_currency
        return query_params
