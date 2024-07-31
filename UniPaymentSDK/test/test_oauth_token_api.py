from __future__ import absolute_import

import logging

from test.test_base_client import TestBaseClient

logger = logging.getLogger(__name__)


class TestOauthTokenAPI(TestBaseClient):

    def test_get_access_token(self):
        """
            Test case for get_access_token. OauthTokenAPI.get_access_token() is called in parent class
        """
        self.assertIsNotNone(self.access_token)

    def tearDown(self):
        pass
