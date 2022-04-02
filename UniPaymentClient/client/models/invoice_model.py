# coding: utf-8

import pprint

import six


class InvoiceModel(object):
    field_types = {
        'network': 'str',
        'address': 'str',
        'app_id': 'str',
        'invoice_id': 'str',
        'order_id': 'str',
        'price_amount': 'float',
        'price_currency': 'str',
        'pay_amount': 'float',
        'pay_currency': 'str',
        'exchange_rate': 'float',
        'paid_amount': 'float',
        'create_time': 'datetime',
        'expiration_time': 'datetime',
        'confirm_speed': 'str',
        'status': 'str',
        'error_status': 'str',
        'invoice_url': 'str'
    }

    attribute_map = {
        'network': 'network',
        'address': 'address',
        'app_id': 'app_id',
        'invoice_id': 'invoice_id',
        'order_id': 'order_id',
        'price_amount': 'price_amount',
        'price_currency': 'price_currency',
        'pay_amount': 'pay_amount',
        'pay_currency': 'pay_currency',
        'exchange_rate': 'exchange_rate',
        'paid_amount': 'paid_amount',
        'create_time': 'create_time',
        'expiration_time': 'expiration_time',
        'confirm_speed': 'confirm_speed',
        'status': 'status',
        'error_status': 'error_status',
        'invoice_url': 'invoice_url'
    }

    def __init__(self, network=None, address=None, app_id=None, invoice_id=None, order_id=None, price_amount=None,
                 price_currency=None, pay_amount=None, pay_currency=None, exchange_rate=None, paid_amount=None,
                 create_time=None, expiration_time=None, confirm_speed=None, status=None, error_status=None,
                 invoice_url=None):  # noqa: E501
        self._network = None
        self._address = None
        self._app_id = None
        self._invoice_id = None
        self._order_id = None
        self._price_amount = None
        self._price_currency = None
        self._pay_amount = None
        self._pay_currency = None
        self._exchange_rate = None
        self._paid_amount = None
        self._create_time = None
        self._expiration_time = None
        self._confirm_speed = None
        self._status = None
        self._error_status = None
        self._invoice_url = None
        self.discriminator = None
        if network is not None:
            self.network = network
        if address is not None:
            self.address = address
        if app_id is not None:
            self.app_id = app_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if order_id is not None:
            self.order_id = order_id
        if price_amount is not None:
            self.price_amount = price_amount
        if price_currency is not None:
            self.price_currency = price_currency
        if pay_amount is not None:
            self.pay_amount = pay_amount
        if pay_currency is not None:
            self.pay_currency = pay_currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if paid_amount is not None:
            self.paid_amount = paid_amount
        if create_time is not None:
            self.create_time = create_time
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if confirm_speed is not None:
            self.confirm_speed = confirm_speed
        if status is not None:
            self.status = status
        if error_status is not None:
            self.error_status = error_status
        if invoice_url is not None:
            self.invoice_url = invoice_url

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, network):
        self._network = network

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        self._app_id = app_id

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self._order_id = order_id

    @property
    def price_amount(self):
        return self._price_amount

    @price_amount.setter
    def price_amount(self, price_amount):
        self._price_amount = price_amount

    @property
    def price_currency(self):
        return self._price_currency

    @price_currency.setter
    def price_currency(self, price_currency):
        self._price_currency = price_currency

    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, pay_amount):
        self._pay_amount = pay_amount

    @property
    def pay_currency(self):
        return self._pay_currency

    @pay_currency.setter
    def pay_currency(self, pay_currency):
        self._pay_currency = pay_currency

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        self._paid_amount = paid_amount

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        self._create_time = create_time

    @property
    def expiration_time(self):
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        self._expiration_time = expiration_time

    @property
    def confirm_speed(self):
        return self._confirm_speed

    @confirm_speed.setter
    def confirm_speed(self, confirm_speed):
        self._confirm_speed = confirm_speed

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def error_status(self):
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        self._error_status = error_status

    @property
    def invoice_url(self):
        return self._invoice_url

    @invoice_url.setter
    def invoice_url(self, invoice_url):
        self._invoice_url = invoice_url

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.field_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InvoiceModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
