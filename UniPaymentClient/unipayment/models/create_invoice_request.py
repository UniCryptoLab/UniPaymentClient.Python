# coding: utf-8

import pprint

import six


class CreateInvoiceRequest(object):
    field_types = {
        'app_id': 'str',
        'title': 'str',
        'description': 'str',
        'lang': 'str',
        'price_amount': 'float',
        'price_currency': 'str',
        'pay_currency': 'str',
        'network': 'str',
        'notify_url': 'str',
        'redirect_url': 'str',
        'order_id': 'str',
        'ext_args': 'str',
        'confirm_speed': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'title': 'title',
        'description': 'description',
        'lang': 'lang',
        'price_amount': 'price_amount',
        'price_currency': 'price_currency',
        'pay_currency': 'pay_currency',
        'network': 'network',
        'notify_url': 'notify_url',
        'redirect_url': 'redirect_url',
        'order_id': 'order_id',
        'ext_args': 'ext_args',
        'confirm_speed': 'confirm_speed'
    }

    def __init__(self, app_id=None, title=None, description=None, lang=None, price_amount=None, price_currency=None,
                 pay_currency=None, network=None, notify_url=None, redirect_url=None, order_id=None, ext_args=None,
                 confirm_speed=None):  # noqa: E501
        self._app_id = None
        self._title = None
        self._description = None
        self._lang = None
        self._price_amount = None
        self._price_currency = None
        self._pay_currency = None
        self._network = None
        self._notify_url = None
        self._redirect_url = None
        self._order_id = None
        self._ext_args = None
        self._confirm_speed = None
        self.discriminator = None
        if app_id is not None:
            self._app_id = app_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if lang is not None:
            self.lang = lang
        if price_amount is not None:
            self.price_amount = price_amount
        if price_currency is not None:
            self.price_currency = price_currency
        if pay_currency is not None:
            self.pay_currency = pay_currency
        if network is not None:
            self.network = network
        if notify_url is not None:
            self.notify_url = notify_url
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if order_id is not None:
            self.order_id = order_id
        if ext_args is not None:
            self.ext_args = ext_args
        if confirm_speed is not None:
            self.confirm_speed = confirm_speed

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        self._app_id = app_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        self._lang = lang

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
    def pay_currency(self):
        return self._pay_currency

    @pay_currency.setter
    def pay_currency(self, pay_currency):
        self._pay_currency = pay_currency

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, network):
        self._network = network

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        self._notify_url = notify_url

    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        self._redirect_url = redirect_url

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self._order_id = order_id

    @property
    def ext_args(self):
        return self._ext_args

    @ext_args.setter
    def ext_args(self, ext_args):
        self._ext_args = ext_args

    @property
    def confirm_speed(self):
        return self._confirm_speed

    @confirm_speed.setter
    def confirm_speed(self, confirm_speed):
        allowed_values = ["low", "medium", "high"]  # noqa: E501
        if confirm_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `confirm_speed` ({0}), must be one of {1}"  # noqa: E501
                    .format(confirm_speed, allowed_values)
            )

        self._confirm_speed = confirm_speed

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
                if value is not None:
                    result[attr] = value
        if issubclass(CreateInvoiceRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreateInvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
