# coding: utf-8


import pprint

import six


class CreatePayoutRequest(object):
    field_types = {
        'items': 'list[PayoutRequestItem]',
        'network': 'str',
        'asset_type': 'str'
    }

    attribute_map = {
        'items': 'items',
        'network': 'network',
        'asset_type': 'asset_type'
    }

    def __init__(self, items=None, network=None, asset_type=None):
        self._items = None
        self._network = None
        self._asset_type = None
        self.discriminator = None
        if items is not None:
            self.items = items
        if network is not None:
            self.network = network
        if asset_type is not None:
            self.asset_type = asset_type

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, network):
        self._network = network

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        self._asset_type = asset_type

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
        if issubclass(CreatePayoutRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreatePayoutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
