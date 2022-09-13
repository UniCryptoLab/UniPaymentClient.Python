# coding: utf-8

import pprint

import six


class GetExchangeRatesResponse(object):
    field_types = {
        'code': 'str',
        'msg': 'str',
        'data': 'list[ExchangeRateModel]'

    }

    attribute_map = {
        'code': 'code',
        'msg': 'msg',
        'data': 'data'
    }

    def __init__(self, code=None, msg=None, data=None):  # noqa: E501
        self._code = None
        self._msg = None
        self._data = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if data is not None:
            self.data = data

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

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
        if issubclass(GetExchangeRatesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, GetExchangeRatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
