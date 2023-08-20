# coding: utf-8


import pprint

import six


class WithdrawalModel(object):
    field_types = {
        'id': 'str',
        'network': 'str',
        'asset_type': 'str',
        'amount': 'float',
        'address': 'str',
        'fee': 'float',
        'status': 'str',
        'txn_hash': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'network': 'network',
        'asset_type': 'asset_type',
        'amount': 'amount',
        'address': 'address',
        'fee': 'fee',
        'status': 'status',
        'txn_hash': 'txn_hash',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, network=None, asset_type=None, amount=None, address=None, fee=None, status=None,
                 txn_hash=None, create_time=None):
        self._id = None
        self._network = None
        self._asset_type = None
        self._amount = None
        self._address = None
        self._fee = None
        self._status = None
        self._txn_hash = None
        self._create_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if network is not None:
            self.network = network
        if asset_type is not None:
            self.asset_type = asset_type
        if amount is not None:
            self.amount = amount
        if address is not None:
            self.address = address
        if fee is not None:
            self.fee = fee
        if status is not None:
            self.status = status
        if txn_hash is not None:
            self.txn_hash = txn_hash
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, fee):
        self._fee = fee

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["Pending", "Cancel", "Confirm", "Reject", "Approve", "Success", "Fail"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                    .format(status, allowed_values)
            )

        self._status = status

    @property
    def txn_hash(self):
        return self._txn_hash

    @txn_hash.setter
    def txn_hash(self, txn_hash):
        self._txn_hash = txn_hash

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        self._create_time = create_time

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
        if issubclass(WithdrawalModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WithdrawalModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
