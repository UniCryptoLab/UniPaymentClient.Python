class ApiException(Exception):
    def __init__(self, status=None, reason=None, http_resp=None):
        self.status = http_resp.status if http_resp else status
        self.reason = http_resp.reason if http_resp else reason
        self.body = http_resp.data if http_resp else None
        self.headers = http_resp.headers if http_resp else None

    def __str__(self):
        error_message = f"({self.status})\nReason: {self.reason}\n"
        if self.headers:
            error_message += f"HTTP response headers: {self.headers}\n"
        if self.body:
            error_message += f"HTTP response body: {self.body}\n"
        return error_message
