# coding: utf-8

import pprint

import six


class ExchangeRateModel(object):
    field_types = {
        'from': 'str',
        'to': 'str',
        'rate': 'float'
    }

    attribute_map = {
        'from_str': 'from',
        'to': 'to',
        'rate': 'rate'
    }

    def __init__(self, from_str=None, to=None, rate=None):  # noqa: E501
        self._from_str = None
        self._to = None
        self._rate = None
        self.discriminator = None
        if from_str is not None:
            self.from_str = from_str
        if to is not None:
            self.to = to
        if rate is not None:
            self.rate = rate

    @property
    def from_str(self):
        return self._from_str

    @from_str.setter
    def from_str(self, from_str):
        self._from_str = from_str

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, to):
        self._to = to

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.field_types):
            if attr == 'from':
                value = getattr(self, 'from_str')
            else:
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
        if issubclass(ExchangeRateModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ExchangeRateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
