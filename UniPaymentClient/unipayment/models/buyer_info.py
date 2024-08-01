# coding: utf-8

import pprint
import six

class BuyerInfo(object):
    field_types = {
        'name': 'str',
        'email': 'str',
        'phone': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'zip_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone': 'phone',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'zip_code': 'zip_code'
    }

    def __init__(self, name=None, email=None, phone=None, address1=None, address2=None, city=None, state=None, country=None, zip_code=None):
        self._name = name
        self._email = email
        self._phone = phone
        self._address1 = address1
        self._address2 = address2
        self._city = city
        self._state = state
        self._country = country
        self.zip_code = zip_code
        self.discriminator = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address1(self):
        return self._address1

    @address1.setter
    def address1(self, address1):
        self._address1 = address1

    @property
    def address2(self):
        return self._address2

    @address2.setter
    def address2(self, address2):
        self._address2 = address2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

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
        if issubclass(BuyerInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, BuyerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
