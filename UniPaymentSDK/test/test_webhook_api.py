from __future__ import absolute_import

import logging

from test.test_base_client import TestBaseClient
from unipayment.models import UpdateNotifyURLRequest, UpdateSecretKeyRequest

logger = logging.getLogger(__name__)


class TestWebhookAPI(TestBaseClient):
    pass

    def test_update_notify_url(self):
        """
            Test case update_notify_url
        """

        update_notify_url_request = UpdateNotifyURLRequest(notify_url='https://en7exsmaa68jo.x.pipedream.net')
        update_notify_url_response = self.WebhookAPI.update_notify_url(update_notify_url_request)
        logger.debug("response body: %s", update_notify_url_response.to_json())
        self.assertEqual('OK', update_notify_url_response.code)

    def test_update_secret_key(self):
        """
            Test case update_secret_key
        """

        update_secret_key_request = UpdateSecretKeyRequest(secret_key='s3cretKey@2024%')
        update_secret_key_response = self.WebhookAPI.update_secret_key(update_secret_key_request)
        logger.debug("response body: %s", update_secret_key_response.to_json())
        self.assertEqual('OK', update_secret_key_response.code)
