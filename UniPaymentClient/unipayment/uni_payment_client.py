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

    def get_wallet_balances(self, **kwargs):
        """get_wallet_balances  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallet_balances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetWalletBalanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wallet_balances_with_http_info(**kwargs)
        else:
            (data) = self.get_wallet_balances_with_http_info(**kwargs)
            return data

    def get_wallet_balances_with_http_info(self, **kwargs):
        """get_wallet_balances  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallet_balances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResponseListBalanceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['async_req']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wallet_balances" % key
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
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/wallet/balances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetWalletBalanceResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_withdrawal(self, create_withdraw_request, **kwargs):
        """create_withdrawal

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_withdrawal(create_withdraw_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWithdrawalRequest create_withdraw_request: (required)
        :return: CreateWithdrawalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_withdrawal_with_http_info(create_withdraw_request, **kwargs)
        else:
            (data) = self.create_withdrawal_with_http_info(create_withdraw_request, **kwargs)
            return data

    def create_withdrawal_with_http_info(self, create_withdraw_request, **kwargs):
        """create_withdrawal

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_withdrawal_with_http_info(create_withdraw_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWithdrawalRequest create_withdraw_request: (required)
        :return: CreateWithdrawalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_withdraw_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_withdrawal" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'request' is set
        if ('create_withdraw_request' not in params or
                params['create_withdraw_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_withdraw_request` when calling `create_withdrawal`")

        collection_formats = {}

        path_params = {}

        query_params = None

        body_params = None
        if 'create_withdraw_request' in params:
            body_params = params['create_withdraw_request'].to_dict()

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/wallet/withdrawals', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateWithdrawalResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_withdrawal_by_id(self, withdrawal_id, **kwargs):
        """get_withdrawal_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_withdrawal_by_id(withdrawal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str withdrawal_id: (required)
        :return: GetWithdrawalByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_withdrawal_by_id_with_http_info(withdrawal_id, **kwargs)
        else:
            (data) = self.get_withdrawal_by_id_with_http_info(withdrawal_id, **kwargs)
            return data

    def get_withdrawal_by_id_with_http_info(self, withdrawal_id, **kwargs):
        """get_withdrawal_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_withdrawal_by_id_with_http_info(withdrawal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str withdrawal_id: (required)
        :return: GetWithdrawalByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['withdrawal_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_withdrawal_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'withdrawal_id' is set
        if ('withdrawal_id' not in params or
                params['withdrawal_id'] is None):
            raise ValueError(
                "Missing the required parameter `withdrawal_id` when calling `get_withdrawal_by_id`")

        collection_formats = {}

        path_params = {}
        if 'withdrawal_id' in params:
            path_params['withdrawalId'] = params['withdrawal_id']

        query_params = None

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/wallet/withdrawals/{withdrawalId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetWithdrawalByIdResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_withdrawal(self, cancel_withdrawal_request, **kwargs):
        """cancel_withdrawal

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_withdrawal(cancel_withdrawal_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CancelWithdrawalRequest cancel_withdrawal_request: (required)
        :return: CancelWithdrawalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_withdrawal_with_http_info(cancel_withdrawal_request, **kwargs)
        else:
            (data) = self.cancel_withdrawal_with_http_info(cancel_withdrawal_request, **kwargs)
            return data

    def cancel_withdrawal_with_http_info(self, cancel_withdrawal_request, **kwargs):
        """cancel_withdrawal

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_withdrawal_with_http_info(cancel_withdrawal_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CancelWithdrawalRequest cancel_withdrawal_request: (required)
        :return: CancelWithdrawalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_withdrawal_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_withdrawal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cancel_withdrawal_request' is set
        if ('cancel_withdrawal_request' not in params or
                params['cancel_withdrawal_request'] is None):
            raise ValueError(
                "Missing the required parameter `cancel_withdrawal_request` when calling `cancel_withdrawal`")

        collection_formats = {}

        path_params = None

        query_params = None

        body_params = None
        if 'cancel_withdrawal_request' in params:
            body_params = params['cancel_withdrawal_request'].to_dict()

        header_params = {}

        form_params = []
        local_var_files = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/wallet/withdrawals/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelWithdrawalResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_withdrawals(self, **kwargs):
        """query_withdrawals

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_withdrawals(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryWithdrawalsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_withdrawals_with_http_info(**kwargs)
        else:
            (data) = self.query_withdrawals_with_http_info(**kwargs)
            return data

    def query_withdrawals_with_http_info(self, **kwargs):
        """query_withdrawals

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_withdrawals_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryWithdrawalsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_withdrawals" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = None

        query_params = None

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/wallet/withdrawals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueryWithdrawalsResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_payout(self, create_payout_request, **kwargs):
        """create_payout

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payout(create_payout_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePayoutRequest create_payout_request: (required)
        :return: CreatePayoutResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_payout_with_http_info(create_payout_request, **kwargs)
        else:
            (data) = self.create_payout_with_http_info(create_payout_request, **kwargs)
            return data

    def create_payout_with_http_info(self, create_payout_request, **kwargs):
        """create_payout

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payout_with_http_info(create_payout_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePayoutRequest create_payout_request: (required)
        :return: CreatePayoutResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_payout_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_payout_request' is set
        if ('create_payout_request' not in params or
                params['create_payout_request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_payout`")

        collection_formats = {}

        path_params = {}

        query_params = None

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_payout_request' in params:
            body_params = params['create_payout_request'].to_dict()

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/payouts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePayoutResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payout_by_id(self, payout_id, **kwargs):
        """get_payout_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_by_id(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payout_id: (required)
        :return: GetPayoutByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payout_by_id_with_http_info(payout_id, **kwargs)
        else:
            (data) = self.get_payout_by_id_with_http_info(payout_id, **kwargs)
            return data

    def get_payout_by_id_with_http_info(self, payout_id, **kwargs):
        """get_payout_by_id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_by_id_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payout_id: (required)
        :return: GetPayoutByIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payout_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payout_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in params or
                params['payout_id'] is None):
            raise ValueError("Missing the required parameter `payout_id` when calling `get_payout_by_id`")

        collection_formats = {}

        path_params = {}
        if 'payout_id' in params:
            path_params['payoutId'] = params['payout_id']

        query_params = None

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/payouts/{payoutId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPayoutByIdResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_payouts(self, **kwargs):
        """query_payouts

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_payouts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryPayoutsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_payouts_with_http_info(**kwargs)
        else:
            (data) = self.query_payouts_with_http_info(**kwargs)
            return data

    def query_payouts_with_http_info(self, **kwargs):
        """query_payouts

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_payouts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: QueryPayoutsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_payouts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = None

        query_params = None

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/v' + self.configuration.api_version + '/payouts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueryPayoutsResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
