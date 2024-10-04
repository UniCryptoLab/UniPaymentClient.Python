# UniPayment Python SDK

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/UniCryptoLab/UniPaymentClient.Python/blob/main/UniPaymentClient/LICENSE.txt)
[![PyPI](https://img.shields.io/pypi/v/unipayment.svg?style=flat-square)](https://pypi.org/project/unipayment)

A Python SDK client for the [UniPayment API](https://unipayment.readme.io/reference/overview).

This SDK provides a convenient abstraction of UniPayment's Gateway API and allows developers to focus on payment
flow/e-commerce integration rather than on the specific details of client-server interaction using the raw API.

## Getting Started

[Integration Tutorial](https://bit.ly/up-help-integration)

Before using the UniPayment API, sign up for your [API key](https://console.unipayment.io/).

You can also use our test tokens for testing and
integration. [Documentation](https://help.unipayment.io/en/articles/8263248-how-to-use-testcoin).

## Installation

### Manual

1. Download the package and extract it into a local directory or clone the repo.
2. cd into the root directory where setup.py is located.
3. Enter：

```bash
python setup.py install
```

### Using pip

```bash
pip install unipayment
```

## Initializing UniPayment SDK Configuration

You can load the configurations using the following:

```python
from unipayment import Configuration, BillingAPI, BeneficiaryAPI, CommonAPI, ExchangeAPI, PaymentAPI, WalletAPI


self.configuration = Configuration()
self.configuration.client_id = '071a5fad-9f7e-4785-9fe1-5a5e8d45c518'
self.configuration.client_secret = 'CzWUHMvWy7Dw7NAc8ZnKaDkqnXzSMV18d'
self.configuration.app_id = "a22a62d1-3b64-4cb5-9336-9c45afd91e6e"
self.configuration.is_sandbox = True
self.configuration.debug = True

self.CommonAPI = CommonAPI(self.configuration)
self.BeneficiaryAPI = BeneficiaryAPI(self.configuration)
self.ExchangeAPI = ExchangeAPI(self.configuration)
self.WalletAPI = WalletAPI(self.configuration)
self.PaymentAPI = PaymentAPI(self.configuration)
self.BillingAPI = BillingAPI(self.configuration)

if self.configuration.debug:
    logger.setLevel(logging.DEBUG)

```


## Create an invoice

> Reference：https://unipayment.readme.io/reference/create_invoice

```python
import logging
import uuid

from unipayment.models import CreateInvoiceRequest

logger = logging.getLogger(__name__)

order_id = uuid.uuid4()
create_invoice_request = CreateInvoiceRequest(app_id=self.configuration.app_id, price_amount=2.0,
                                              price_currency='USD', order_id=order_id, lang='en',
                                              ext_args='"Merchant Pass Through Data')

create_invoice_response = self.BillingAPI.create_invoice(create_invoice_request)
logger.debug("response body: %s", create_invoice_response)

```

### CreateInvoiceResponse

```json
{
  "msg": "",
  "code": "OK",
  "data": {
    "app_id": "a22a62d1-3b64-4cb5-9336-9c45afd91e6e",
    "payment_method_type": "UNKNOWN",
    "invoice_id": "V2s88VEcyK4o9c8r999qWR",
    "order_id": "62986426-d37c-452b-98cf-039c785f3d86",
    "price_amount": 2.0,
    "price_currency": "USD",
    "network": null,
    "address": null,
    "pay_amount": 0.0,
    "pay_currency": null,
    "exchange_rate": 0.0,
    "paid_amount": 0.0,
    "refunded_price_amount": 0.0,
    "create_time": "2024-07-31T07:53:08",
    "expiration_time": "2024-07-31T08:13:08",
    "confirm_speed": "Medium",
    "status": "New",
    "error_status": "None",
    "invoice_url": "https://sandbox-app.unipayment.io/i/V2s88VEcyK4o9c8r999qWR"
  }
}

```

## Webhook Notification
[Webhook Tutorial](https://bit.ly/up-help-webhook)

## Webhook Signature Verification

See https://unipayment.readme.io/reference/webhook

Use the below code to verify of the 'hmac_signature' which can extract from the request header

```python

from unipayment import WebhookSignatureUtil

"""
//Use raw json payload (no formatting or pretty print)
"""
payload = 'json payload'
secret_key = 'your secret key'
signature = 'signature to verify'
valid = WebhookSignatureUtil.is_valid(payload, secret_key, signature)

```

## Run Example

1.Get source code form GitHub

``` bash
git clone https://github.com/UniCryptoLab/UniPaymentClient.Python.git
```

2.Prepare the environment

``` bash
virtualenv venv
source venv/bin/active
cd UniPaymentClient.Python/UniPaymentClientExample/ pip
pip install -r requirement.txt
```

3.Run example

``` bash
python main.py
```

## License

MIT License

Copyright (c) 2024 UniPayment

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.