# coding: utf-8


import pprint

import six


class PayoutRequestItem(object):
    field_types = {
        'address': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'address': 'address',
        'amount': 'amount'
    }

    def __init__(self, address=None, amount=None):
        self._address = None
        self._amount = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if amount is not None:
            self.amount = amount

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

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
        if issubclass(PayoutRequestItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PayoutRequestItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
