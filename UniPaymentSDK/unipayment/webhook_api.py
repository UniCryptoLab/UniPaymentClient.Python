import json

from .base_client import BaseClient
from .models.api_response import ApiResponse
from .models.update_notify_url_request import UpdateNotifyURLRequest
from .models.update_secret_key_request import UpdateSecretKeyRequest


class WebhookAPI(BaseClient):
    pass

    def update_notify_url(self, update_notify_url_request: UpdateNotifyURLRequest) -> ApiResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/webhook/notify-url'
        response_text = self.call_api(url, 'POST', body=json.loads(update_notify_url_request.to_json()))
        return ApiResponse.from_json(response_text)

    def update_secret_key(self, update_secret_key_request: UpdateSecretKeyRequest) -> ApiResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/webhook/secret-key'
        response_text = self.call_api(url, 'POST', body=json.loads(update_secret_key_request.to_json()))
        return ApiResponse.from_json(response_text)
