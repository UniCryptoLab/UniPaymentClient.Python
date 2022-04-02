# coding: utf-8

import pprint

import six


class InvoicePageListModel(object):
    field_types = {
        'models': 'list[InvoiceModel]',
        'total': 'int',
        'page_no': 'int',
        'page_count': 'int'
    }

    attribute_map = {
        'models': 'models',
        'total': 'total',
        'page_no': 'page_no',
        'page_count': 'page_count'
    }

    def __init__(self, models=None, total=None, page_no=None, page_count=None):  # noqa: E501
        self._models = None
        self._total = None
        self._page_no = None
        self._page_count = None
        self.discriminator = None
        if models is not None:
            self.models = models
        if total is not None:
            self.total = total
        if page_no is not None:
            self.page_no = page_no
        if page_count is not None:
            self.page_count = page_count

    @property
    def models(self):
        return self._models

    @models.setter
    def models(self, models):
        self._models = models

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        self._page_no = page_no

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        self._page_count = page_count

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
        if issubclass(InvoicePageListModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoicePageListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
