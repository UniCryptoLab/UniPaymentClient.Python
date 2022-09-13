# coding: utf-8

import pprint

import six


class InvoiceTransactionModel(object):
    field_types = {
        'hash': 'str',
        'network': 'str',
        'symbol': 'str',
        'from': 'str',
        'to': 'str',
        'amount': 'float',
        'confirmation_count': 'int',
        'is_confirmed': 'bool'
    }

    attribute_map = {
        'hash': 'hash',
        'network': 'network',
        'symbol': 'symbol',
        'from_str': 'from',
        'to': 'to',
        'amount': 'amount',
        'confirmation_count': 'confirmation_count',
        'is_confirmed': 'is_confirmed'
    }

    def __init__(self, hash=None, network=None, symbol=None, from_str=None, to=None, amount=None,
                 confirmation_count=None, is_confirmed=None):  # noqa: E501
        self._hash = None
        self._network = None
        self._symbol = None
        self._from_str = None
        self._to = None
        self._amount = None
        self._confirmation_count = None
        self._is_confirmed = None
        self.discriminator = None
        if hash is not None:
            self._hash = hash
        if network is not None:
            self.network = network
        if symbol is not None:
            self.symbol = symbol
        if from_str is not None:
            self.from_str = from_str
        if to is not None:
            self.to = to
        if amount is not None:
            self.amount = amount
        if confirmation_count is not None:
            self.confirmation_count = confirmation_count
        if is_confirmed is not None:
            self.is_confirmed = is_confirmed

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, hash):
        self._hash = hash

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, network):
        self._network = network

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

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
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def confirmation_count(self):
        return self._confirmation_count

    @confirmation_count.setter
    def confirmation_count(self, confirmation_count):
        self._confirmation_count = confirmation_count

    @property
    def is_confirmed(self):
        return self._is_confirmed

    @is_confirmed.setter
    def is_confirmed(self, is_confirmed):
        self._is_confirmed = is_confirmed

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
        if issubclass(InvoiceTransactionModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceTransactionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
