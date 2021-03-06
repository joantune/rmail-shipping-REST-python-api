# coding: utf-8

"""
    Royal Mail API Shipping V3 (REST)

    This API specification details the requirements for integrating with **Royal Mail API Shipping V3**.<br><br>It specifically covers how the Royal Mail API Shipping V3 can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.<br><br>Royal Mail API Shipping V3 exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail.<br><br>Built on industry standards, Royal Mail API Shipping V3 provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels. There are no costs to customers for using the Royal Mail API Shipping V3 services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.<br><br>This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating/ cancelling a shipment and Manifesting please refer to http://www.royalmail.com/pro-shipping-help.  # noqa: E501

    OpenAPI spec version: 3.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rmail_apiv3.api_client import ApiClient


class AddressesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def addresses_create(self, body, x_rmg_auth_token, **kwargs):  # noqa: E501
        """Create Address  # noqa: E501

        Add a new address to your address book that you can then use in your shipment requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_create(body, x_rmg_auth_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: The address. (required)
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.addresses_create_with_http_info(body, x_rmg_auth_token, **kwargs)  # noqa: E501
        else:
            (data) = self.addresses_create_with_http_info(body, x_rmg_auth_token, **kwargs)  # noqa: E501
            return data

    def addresses_create_with_http_info(self, body, x_rmg_auth_token, **kwargs):  # noqa: E501
        """Create Address  # noqa: E501

        Add a new address to your address book that you can then use in your shipment requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_create_with_http_info(body, x_rmg_auth_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: The address. (required)
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_rmg_auth_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method addresses_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `addresses_create`")  # noqa: E501
        # verify the required parameter 'x_rmg_auth_token' is set
        if ('x_rmg_auth_token' not in params or
                params['x_rmg_auth_token'] is None):
            raise ValueError("Missing the required parameter `x_rmg_auth_token` when calling `addresses_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_rmg_auth_token' in params:
            header_params['X-RMG-Auth-Token'] = params['x_rmg_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['clientID']  # noqa: E501

        return self.api_client.call_api(
            '/addresses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def addresses_delete(self, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Delete Address  # noqa: E501

        Deletes the specified address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_delete(x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID of the address to delete. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.addresses_delete_with_http_info(x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.addresses_delete_with_http_info(x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
            return data

    def addresses_delete_with_http_info(self, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Delete Address  # noqa: E501

        Deletes the specified address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_delete_with_http_info(x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID of the address to delete. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_rmg_auth_token', 'address_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method addresses_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_rmg_auth_token' is set
        if ('x_rmg_auth_token' not in params or
                params['x_rmg_auth_token'] is None):
            raise ValueError("Missing the required parameter `x_rmg_auth_token` when calling `addresses_delete`")  # noqa: E501
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `addresses_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_rmg_auth_token' in params:
            header_params['X-RMG-Auth-Token'] = params['x_rmg_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['clientID']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{addressId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def addresses_get(self, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Get Address  # noqa: E501

        Get the address specified by your unique Address ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_get(x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID. (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.addresses_get_with_http_info(x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.addresses_get_with_http_info(x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
            return data

    def addresses_get_with_http_info(self, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Get Address  # noqa: E501

        Get the address specified by your unique Address ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_get_with_http_info(x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID. (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_rmg_auth_token', 'address_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method addresses_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_rmg_auth_token' is set
        if ('x_rmg_auth_token' not in params or
                params['x_rmg_auth_token'] is None):
            raise ValueError("Missing the required parameter `x_rmg_auth_token` when calling `addresses_get`")  # noqa: E501
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `addresses_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_rmg_auth_token' in params:
            header_params['X-RMG-Auth-Token'] = params['x_rmg_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['clientID']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{addressId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def addresses_get_all(self, x_rmg_auth_token, **kwargs):  # noqa: E501
        """Get Addresses  # noqa: E501

        Get all of your stored addresses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_get_all(x_rmg_auth_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :return: list[Address]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.addresses_get_all_with_http_info(x_rmg_auth_token, **kwargs)  # noqa: E501
        else:
            (data) = self.addresses_get_all_with_http_info(x_rmg_auth_token, **kwargs)  # noqa: E501
            return data

    def addresses_get_all_with_http_info(self, x_rmg_auth_token, **kwargs):  # noqa: E501
        """Get Addresses  # noqa: E501

        Get all of your stored addresses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_get_all_with_http_info(x_rmg_auth_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :return: list[Address]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_rmg_auth_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method addresses_get_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_rmg_auth_token' is set
        if ('x_rmg_auth_token' not in params or
                params['x_rmg_auth_token'] is None):
            raise ValueError("Missing the required parameter `x_rmg_auth_token` when calling `addresses_get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_rmg_auth_token' in params:
            header_params['X-RMG-Auth-Token'] = params['x_rmg_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['clientID']  # noqa: E501

        return self.api_client.call_api(
            '/addresses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Address]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def addresses_update(self, body, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Update address  # noqa: E501

        Update an address that is already in your address book with new details. The whole address will be replaced with<br />new details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_update(body, x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: The address with the updated details. (required)
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID of the address to update. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.addresses_update_with_http_info(body, x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.addresses_update_with_http_info(body, x_rmg_auth_token, address_id, **kwargs)  # noqa: E501
            return data

    def addresses_update_with_http_info(self, body, x_rmg_auth_token, address_id, **kwargs):  # noqa: E501
        """Update address  # noqa: E501

        Update an address that is already in your address book with new details. The whole address will be replaced with<br />new details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.addresses_update_with_http_info(body, x_rmg_auth_token, address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: The address with the updated details. (required)
        :param str x_rmg_auth_token: Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. (required)
        :param str address_id: Your unique Address ID of the address to update. (required)
        :return: AddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_rmg_auth_token', 'address_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method addresses_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `addresses_update`")  # noqa: E501
        # verify the required parameter 'x_rmg_auth_token' is set
        if ('x_rmg_auth_token' not in params or
                params['x_rmg_auth_token'] is None):
            raise ValueError("Missing the required parameter `x_rmg_auth_token` when calling `addresses_update`")  # noqa: E501
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `addresses_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_rmg_auth_token' in params:
            header_params['X-RMG-Auth-Token'] = params['x_rmg_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['clientID']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{addressId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
