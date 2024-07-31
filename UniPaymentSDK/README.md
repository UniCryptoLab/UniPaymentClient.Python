# UniPayment Python SDK

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/UniCryptoLab/UniPaymentClient.Python/blob/main/UniPaymentClient/LICENSE.txt)
[![PyPI](https://img.shields.io/pypi/v/unipayment.svg?style=flat-square)](https://pypi.org/project/unipayment)

A Python SDK client for the [UniPayment API](https://unipayment.readme.io/reference/overview).

This SDK provides a convenient abstraction of UniPayment's Gateway API and allows developers to focus on payment
flow/e-commerce integration rather than on the specific details of client-server interaction using the raw API.

## Getting Started

[Integrate Tutorial](https://help.unipayment.io/en/articles/7851188-integrate-with-payment-gateway)

Before using the UniPayment API, sign up for your [API key](https://console.unipayment.io/).

You can also use our test tokens for testing and
integration. [Documentation](https://help.unipayment.io/en/articles/8263248-how-to-use-testcoin).

## Installation

### Manual

1. Download the package and extract it into a local directory or clone the repo.
2. cd into the root directory where setup.py is located.
3. Enter：[README.md](..%2FREADME.md)

```bash
python setup.py install
```

### Using pip

```bash
pip install unipayment
```[README.md](..%2FREADME.md)

## Initializing UniPayment SDK Configuration

You can load the configurations using the following:

```python
from unipayment.sdk import BillingAPI, BeneficiaryAPI, CommonAPI, OauthTokenAPI, ExchangeAPI, PaymentAPI, WalletAPI
from unipayment.sdk.core import Configuration

self.configuration = Configuration()
self.configuration.client_id = '071a5fad-9f7e-4785-9fe1-5a5e8d45c518'
self.configuration.client_secret = 'CzWUHMvWy7Dw7NAc8ZnKaDkqnXzSMV18d'
self.configuration.app_id = "a22a62d1-3b64-4cb5-9336-9c45afd91e6e"
self.configuration.debug = True
self.CommonAPI = CommonAPI(self.configuration)
self.OauthTokenAPI = OauthTokenAPI(self.configuration)
self.BeneficiaryAPI = BeneficiaryAPI(self.configuration)
self.ExchangeAPI = ExchangeAPI(self.configuration)
self.WalletAPI = WalletAPI(self.configuration)
self.PaymentAPI = PaymentAPI(self.configuration)
self.BillingAPI = BillingAPI(self.configuration)

if self.configuration.debug:
    logger.setLevel(logging.DEBUG)

```

## Authentication

> Reference：https://unipayment.readme.io/reference/authentication

### Obtaining An Access Token

To authenticate your application, you need to obtain an access token by making a request to our OAuth 2.0 token
endpoint. This request must include your client_id, client_secret, and the grant_type.

> How to obtain an access token: https://unipayment.readme.io/reference/access-token

```python
token_response = self.OauthTokenAPI.get_access_token()
access_token = token_response.access_token
```

Note: If access token is expired, an exception will be thrown by the SDK.

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

create_invoice_response = self.BillingAPI.create_invoice(self.access_token, create_invoice_request)
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

## Handle Invoice IPN

> Reference：https://unipayment.readme.io/reference/ipn-check
>
> IPN: https://unipayment.readme.io/reference/ipn-payment-notification
>
> Invoice Status: https://unipayment.readme.io/reference/invoice-status


IPNs (Instant Payment Notifications) are sent to the notify_url when order status is changed to paid, confirmed and
complete.

```python

@app.route("/handle-notify", methods=['POST'])
def check_notify():
    notify = request.get_json()
    try:
        check_ipn_response = self.CommonAPI.check_ipn(self.access_token, notify)
        if check_ipn_response.code == 'OK':
            # ipn is valid, we can handel status
            if notify['status'] == 'Confirmed':
                # payment is confirmed, we can process order here
                print('invoice is confirmed')
        else:
            # ipn is not valid
            pass
    except ApiException as e:
        print(e)

```

IPN notify

``` json
{
	"ipn_type": "invoice",
	"event": "invoice_expired",
	"app_id": "cee1b9e2-d90c-4b63-9824-d621edb38012",
	"invoice_id": "3Q7fyLnB2YNhUDW1fFNyEz",
	"order_id": "20",
	"price_amount": 6.0,
	"price_currency": "SGD",
	"network": null,
	"address": null,
	"pay_currency": null,
	"pay_amount": 0.0,
	"exchange_rate": 0.0,
	"paid_amount": 0.0,
	"confirmed_amount": 0.0,
	"refunded_price_amount": 0.0,
	"create_time": "2022-09-12T03:36:03",
	"expiration_time": "2022-09-12T03:41:03",
	"status": "Expired",
	"error_status": "None",
	"ext_args": null,
	"transactions": null,
	"notify_id": "8ccd2b61-226b-48e5-99b8-acb1f350313e",
	"notify_time": "2022-09-12T03:56:10.5852752Z"
}
```

## Handle Withdrawal IPN

> Reference：https://unipayment.readme.io/reference/ipn-check

> IPN: https://unipayment.readme.io/reference/ipn-withdrawal-notification

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