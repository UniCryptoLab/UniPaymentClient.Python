# coding: utf-8

import pprint

import six


class QueryInvoiceRequest(object):
    field_types = {
        'app_id': 'str',
        'invoice_id': 'str',
        'order_id': 'str',
        'status': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'is_asc': 'bool',
        'start': 'str',
        'end': 'str'
    }

    attribute_map = {
        'app_id': 'appId',
        'invoice_id': 'invoiceId',
        'order_id': 'orderId',
        'status': 'status',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'is_asc': 'isAsc',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, app_id=None, invoice_id=None, order_id=None, status=None,
                 page_no=None, page_size=None, is_asc=None, start=None, end=None):  # noqa: E501
        self._app_id = None
        self._invoice_id = None
        self._order_id = None
        self._status = None
        self._page_no = None
        self._page_size = None
        self._is_asc = None
        self._start = None
        self._end = None
        self.discriminator = None
        if app_id is not None:
            self._app_id = app_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if is_asc is not None:
            self.is_asc = is_asc
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        self._app_id = app_id

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self._order_id = order_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        self._page_no = page_no

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        self._page_size = page_size

    @property
    def is_asc(self):
        return self._is_asc

    @is_asc.setter
    def is_asc(self, is_asc):
        self._is_asc = is_asc

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

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
        if issubclass(QueryInvoiceRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, QueryInvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
