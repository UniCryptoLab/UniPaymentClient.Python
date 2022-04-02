# coding: utf-8

import pprint

import six


class CurrencyModel(object):
    field_types = {
        'code': 'str',
        'symbol': 'str',
        'name': 'str',
        'is_fiat': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'symbol': 'symbol',
        'name': 'name',
        'is_fiat': 'is_fiat'
    }

    def __init__(self, code=None, symbol=None, name=None, is_fiat=None):  # noqa: E501
        self._code = None
        self._symbol = None
        self._name = None
        self._is_fiat = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name
        if is_fiat is not None:
            self.is_fiat = is_fiat

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def is_fiat(self):
        return self._is_fiat

    @is_fiat.setter
    def is_fiat(self, is_fiat):
        self._is_fiat = is_fiat

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
        if issubclass(CurrencyModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CurrencyModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
