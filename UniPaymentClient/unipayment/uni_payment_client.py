# coding: utf-8

from __future__ import absolute_import

import json
from datetime import datetime

import six

from .api_client import ApiClient
from .configuration import Configuration

# python 2 and python 3 compatibility library


class UniPaymentClient(object):
    def __init__(self, client_id, client_secret, is_sandbox=False, debug=False):
        self.configuration = Configuration()
        self.configuration.client_id = client_id
        self.configuration.client_secret = client_secret
        self.configuration.debug = debug
        if is_sandbox:
            self.configuration.host = "https://sandbox-api.unipayment.io"
        else:
            self.configuration.host = "https://api.unipayment.io"
        self.api_client = ApiClient(self.configuration)

    def create_invoice(self, create_invoice_request, **kwargs):
        """create_invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invoice(create_invoice_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvoiceRequest create_invoice_request: (required)
        :return: ResponseInvoiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_invoice_with_http_info(create_invoice_request, **kwargs)
        else:
            (data) = self.create_invoice_with_http_info(create_invoice_request, **kwargs)
            return data

    def create_invoice_with_http_info(self, create_invoice_request, **kwargs):
        """create_invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invoice_with_http_info(create_invoice_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvoiceRequest create_invoice_request: (required)
        :return: ResponseInvoiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_invoice_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_invoice_request' is set
        if ('create_invoice_request' not in params or
                params['create_invoice_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_invoice_request` when calling `create_invoice`")

        collection_formats = {}

        path_params = {}

        query_params = None

        body_params = None
        if 'create_invoice_request' in params:
            body_params = params['create_invoice_request'].to_dict()

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/invoices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateInvoiceResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_invoice(self, query_invoice_request, **kwargs):
        """query_invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_invoice(query_invoice_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QueryInvoiceRequest query_invoice_request: (required)
        :return: QueryInvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_invoice_with_http_info(query_invoice_request, **kwargs)
        else:
            (data) = self.query_invoice_with_http_info(query_invoice_request, **kwargs)
            return data

    def query_invoice_with_http_info(self, query_invoice_request, **kwargs):
        """query_invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_invoice_with_http_info(query_invoice_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QueryInvoiceRequest query_invoice_request: (required)
        :return: QueryInvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_invoice_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_invoice_request' is set
        if ('query_invoice_request' not in params or
                params['query_invoice_request'] is None):
            raise ValueError(
                "Missing the required parameter `query_invoice_request` when calling `query_invoice`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_invoice_request' in params:
            query_invoice_request = params['query_invoice_request'].to_dict()
            for key, value in query_invoice_request.items():
                if value is not None:
                    query_params.append((key, value))

        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetExchangeRatesResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invoice_by_id(self, invoice_id, **kwargs):
        """get_invoice_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoice_by_id(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: (required)
        :return: GetInvoiceByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invoice_by_id_with_http_info(invoice_id, **kwargs)
        else:
            (data) = self.get_invoice_by_id_with_http_info(invoice_id, **kwargs)
            return data

    def get_invoice_by_id_with_http_info(self, invoice_id, **kwargs):
        """get_invoice_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoice_by_id_with_http_info(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: (required)
        :return: GetInvoiceByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if invoice_id is None:
            raise ValueError(
                "Missing the required parameter `invoice_id` when calling `get_invoice_by_id`")

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/invoices/' + invoice_id, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetInvoiceByIdResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_exchange_rates_by_fiat_currency(self, fiat_currency, **kwargs):
        """get_exchange_rates_by_fiat_currency

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rates_by_fiat_currency(fiat_currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fiat_currency: (required)
        :return: GetExchangeRatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_exchange_rates_by_fiat_currency_with_http_info(fiat_currency, **kwargs)
        else:
            (data) = self.get_exchange_rates_by_fiat_currency_with_http_info(fiat_currency, **kwargs)
            return data

    def get_exchange_rates_by_fiat_currency_with_http_info(self, fiat_currency, **kwargs):
        """get_exchange_rates_by_fiat_currency

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rates_by_fiat_currency_with_http_info(fiat_currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fiat_currency: (required)
        :return: GetExchangeRatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fiat_currency' is set
        if fiat_currency is None:
            raise ValueError(
                "Missing the required parameter `fiat_currency` when calling `get_exchange_rate_by_fiat_currency`")

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/rates/' + fiat_currency, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetExchangeRatesResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_exchange_rates_by_currency_pair(self, fiat_currency, crypto_currency, **kwargs):
        """get_exchange_rates_by_currency_pair

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rates_by_currency_pair(fiat_currency, crypto_currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fiat_currency: (required)
        :param str crypto_currency: (required)
        :return: GetExchangeRatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_exchange_rates_by_currency_pair_with_http_info(fiat_currency, crypto_currency, **kwargs)
        else:
            (data) = self.get_exchange_rates_by_currency_pair_with_http_info(fiat_currency, crypto_currency, **kwargs)
            return data

    def get_exchange_rates_by_currency_pair_with_http_info(self, fiat_currency, crypto_currency, **kwargs):
        """get_exchange_rates_by_currency_pair

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rates_by_currency_pair_with_http_info(fiat_currency, crypto_currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
         :param str fiat_currency: (required)
        :param str crypto_currency: (required)
        :return: GetExchangeRatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fiat_currency' is set
        if fiat_currency is None:
            raise ValueError(
                "Missing the required parameter `fiat_currency` when calling `get_exchange_rates_by_currency_pair`")

        if crypto_currency is None:
            raise ValueError(
                "Missing the required parameter `crypto_currency` when calling `get_exchange_rates_by_currency_pair`")

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/rates/' + fiat_currency + '/' + crypto_currency, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetExchangeRateResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_ips(self, **kwargs):
        """query_ips

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ips(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryIpsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_ips_with_http_info(**kwargs)
        else:
            (data) = self.query_ips_with_http_info(**kwargs)
            return data

    def query_ips_with_http_info(self, **kwargs):
        """query_ips

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ips_with_http_info( async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryIpsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/ips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueryIpsResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_currencies(self, **kwargs):
        """get_currencies

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_currencies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetCurrenciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_currencies_with_http_info(**kwargs)
        else:
            (data) = self.get_currencies_with_http_info(**kwargs)
            return data

    def get_currencies_with_http_info(self, **kwargs):
        """get_currencies

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_currencies_with_http_info( async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetCurrenciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_invoice" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('rd', datetime.utcnow().strftime('%Y%m%d%H%M%S%f')))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCurrenciesResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def check_ipn(self, ipn_notify, **kwargs):
        """check_ipn

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_ipn(ipn_notify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param json or string ipn_notify: (required)
        :return: CheckIpnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_ipn_with_http_info(ipn_notify, **kwargs)
        else:
            (data) = self.check_ipn_with_http_info(ipn_notify, **kwargs)
            return data

    def check_ipn_with_http_info(self, ipn_notify, **kwargs):
        """check_ipn

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_ipn_with_http_info(ipn_notify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param json or string ipn_notify: (required)
        :return: CheckIpnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ipn_notify']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_ipn" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_invoice_request' is set
        if ('ipn_notify' not in params or
                params['ipn_notify'] is None):
            raise ValueError(
                "Missing the required parameter `ipn_notify` when calling `check_ipn`")

        collection_formats = {}

        path_params = {}

        query_params = None

        body_params = None
        if 'ipn_notify' in params:
            # ipn_notify is json or json string, it is not request object
            body_params = params['ipn_notify']

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/ipn', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckIpnResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
