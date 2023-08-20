# coding: utf-8


import pprint

import six


class PayoutDetailModel(object):
    field_types = {
        'payout_id': 'str',
        'network': 'str',
        'asset_type': 'str',
        'status': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'items': 'list[PayoutItem]'
    }

    attribute_map = {
        'payout_id': 'payout_id',
        'network': 'network',
        'asset_type': 'asset_type',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'items': 'items'
    }

    def __init__(self, payout_id=None, network=None, asset_type=None, status=None, create_time=None, update_time=None,
                 items=None):
        self._payout_id = None
        self._network = None
        self._asset_type = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._items = None
        self.discriminator = None
        if payout_id is not None:
            self.payout_id = payout_id
        if network is not None:
            self.network = network
        if asset_type is not None:
            self.asset_type = asset_type
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if items is not None:
            self.items = items

    @property
    def payout_id(self):
        return self._payout_id

    @payout_id.setter
    def payout_id(self, payout_id):
        self._payout_id = payout_id

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["Pending", "Processing", "Complete"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                    .format(status, allowed_values)
            )

        self._status = status

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        self._create_time = create_time

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        self._update_time = update_time

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

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
        if issubclass(PayoutDetailModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PayoutDetailModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
