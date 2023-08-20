# coding: utf-8

import pprint

import six


class BalanceModel(object):
    field_types = {
        'asset_type': 'str',
        'balance': 'float',
        'frozen_balance': 'float',
        'available': 'float'
    }

    attribute_map = {
        'asset_type': 'asset_type',
        'balance': 'balance',
        'frozen_balance': 'frozen_balance',
        'available': 'available'
    }

    def __init__(self, asset_type=None, balance=None, frozen_balance=None, available=None):
        self._asset_type = None
        self._balance = None
        self._frozen_balance = None
        self._available = None
        self.discriminator = None
        if asset_type is not None:
            self.asset_type = asset_type
        if balance is not None:
            self.balance = balance
        if frozen_balance is not None:
            self.frozen_balance = frozen_balance
        if available is not None:
            self.available = available

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        self._asset_type = asset_type

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def frozen_balance(self):
        return self._frozen_balance

    @frozen_balance.setter
    def frozen_balance(self, frozen_balance):
        self._frozen_balance = frozen_balance

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available

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
        if issubclass(BalanceModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, BalanceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
