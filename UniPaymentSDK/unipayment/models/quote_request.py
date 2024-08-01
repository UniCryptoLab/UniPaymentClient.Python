class QuoteRequest(object):
    def __init__(self, from_currency: str, to_currency: str, exchange_amount: float):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange_amount = exchange_amount

    def to_str(self):
        query_params = {
            "from_currency": self.from_currency,
            "to_currency": self.to_currency,
            "exchange_amount": self.exchange_amount
        }
        return query_params
