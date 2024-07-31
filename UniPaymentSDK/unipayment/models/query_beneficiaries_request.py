class QueryBeneficiariesRequest(object):
    def __init__(self, page_no=1, page_size=10, is_asc=True):
        self.page_no = page_no
        self.page_size = page_size
        self.is_asc = is_asc

    def to_str(self):
        query_params = {
            "page_no": self.page_no,
            "page_size": self.page_size,
            "is_asc": str(self.is_asc).lower()
        }
        return query_params
