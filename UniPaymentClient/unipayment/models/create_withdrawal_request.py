# coding: utf-8

import pprint

import six


class CreateWithdrawalRequest(object):
    field_types = {
        'network': 'str',
        'address': 'str',
        'asset_type': 'str',
        'amount': 'float',
        'dest_tag': 'str',
        'notify_url': 'str',
        'note': 'str',
        'auto_confirm': 'bool',
        'include_fee': 'bool'
    }

    attribute_map = {
        'network': 'network',
        'address': 'address',
        'asset_type': 'asset_type',
        'amount': 'amount',
        'dest_tag': 'dest_tag',
        'notify_url': 'notify_url',
        'note': 'note',
        'auto_confirm': 'auto_confirm',
        'include_fee': 'include_fee'
    }

    def __init__(self, network=None, address=None, asset_type=None, amount=None, dest_tag=None, notify_url=None,
                 note=None, auto_confirm=None, include_fee=None):  # noqa: E501
        self._network = None
        self._address = None
        self._asset_type = None
        self._amount = None
        self._dest_tag = None
        self._notify_url = None
        self._note = None
        self._auto_confirm = None
        self._include_fee = None
        self.discriminator = None
        if network is not None:
            self.network = network
        if address is not None:
            self.address = address
        if asset_type is not None:
            self.asset_type = asset_type
        if amount is not None:
            self.amount = amount
        if dest_tag is not None:
            self.dest_tag = dest_tag
        if notify_url is not None:
            self.notify_url = notify_url
        if note is not None:
            self.note = note
        if auto_confirm is not None:
            self.auto_confirm = auto_confirm
        if include_fee is not None:
            self.include_fee = include_fee

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, network):
        self._network = network

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

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
    def dest_tag(self):
        return self._dest_tag

    @dest_tag.setter
    def dest_tag(self, dest_tag):
        self._dest_tag = dest_tag

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        self._notify_url = notify_url

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    @property
    def auto_confirm(self):
        return self._auto_confirm

    @auto_confirm.setter
    def auto_confirm(self, auto_confirm):
        self._auto_confirm = auto_confirm

    @property
    def include_fee(self):
        return self._include_fee

    @include_fee.setter
    def include_fee(self, include_fee):
        self._include_fee = include_fee

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
        if issubclass(CreateWithdrawalRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreateWithdrawalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
