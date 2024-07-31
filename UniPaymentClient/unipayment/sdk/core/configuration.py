from __future__ import absolute_import

import logging
import multiprocessing
import sys


class Configuration(object):

    def __init__(self):
        """Constructor"""
        self.host = ""
        self.client_id = ""
        self.client_secret = ""
        self.app_id = ""
        self.api_version = "1.0"
        self.is_sandbox = True

        if self.is_sandbox:
            self.host = "https://sandbox-api.unipayment.io"
        else:
            self.host = "https://api.unipayment.io"

        self.logger = {
            "package_logger": logging.getLogger("unipayment_sdk"),
            "urllib3_logger": logging.getLogger("urllib3")
        }
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        self.debug = False

        self.verify_ssl = True
        self.ssl_ca_cert = None
        self.cert_file = None
        self.key_file = None
        self.assert_hostname = None

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        self.proxy = None
        self.safe_chars_for_path_param = ''

    def to_debug_report(self):
        return (
            f"Unipayment Python SDK Debug Report:\n"
            f"OS: {sys.platform}\n"
            f"Python Version: {sys.version}\n"
            f"Version of the API: 2.0.0\n"
            f"SDK Package Version: 2.0.0"
        )
