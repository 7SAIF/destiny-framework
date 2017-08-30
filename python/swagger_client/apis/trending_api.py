# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TrendingApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def trending_get_trending_categories(self, **kwargs):
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category.  For pagination within a category, call GetTrendingCategory.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_categories(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20034
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.trending_get_trending_categories_with_http_info(**kwargs)
        else:
            (data) = self.trending_get_trending_categories_with_http_info(**kwargs)
            return data

    def trending_get_trending_categories_with_http_info(self, **kwargs):
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category.  For pagination within a category, call GetTrendingCategory.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_categories_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20034
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trending_get_trending_categories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/Trending/Categories/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20034',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def trending_get_trending_category(self, category_id, page_number, **kwargs):
        """
        Returns paginated lists of trending items for a category.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_category(category_id, page_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str category_id: The ID of the category for whom you want additional results. (required)
        :param int page_number: The page # of results to return. (required)
        :return: InlineResponse20035
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.trending_get_trending_category_with_http_info(category_id, page_number, **kwargs)
        else:
            (data) = self.trending_get_trending_category_with_http_info(category_id, page_number, **kwargs)
            return data

    def trending_get_trending_category_with_http_info(self, category_id, page_number, **kwargs):
        """
        Returns paginated lists of trending items for a category.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_category_with_http_info(category_id, page_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str category_id: The ID of the category for whom you want additional results. (required)
        :param int page_number: The page # of results to return. (required)
        :return: InlineResponse20035
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'page_number']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trending_get_trending_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `trending_get_trending_category`")
        # verify the required parameter 'page_number' is set
        if ('page_number' not in params) or (params['page_number'] is None):
            raise ValueError("Missing the required parameter `page_number` when calling `trending_get_trending_category`")


        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']
        if 'page_number' in params:
            path_params['pageNumber'] = params['page_number']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/Trending/Categories/{categoryId}/{pageNumber}/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20035',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def trending_get_trending_entry_detail(self, identifier, trending_entry_type, **kwargs):
        """
        Returns the detailed results for a specific trending entry.  Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_entry_detail(identifier, trending_entry_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str identifier: The identifier for the entity to be returned. (required)
        :param str trending_entry_type: The type of entity to be returned. (required)
        :return: InlineResponse20036
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.trending_get_trending_entry_detail_with_http_info(identifier, trending_entry_type, **kwargs)
        else:
            (data) = self.trending_get_trending_entry_detail_with_http_info(identifier, trending_entry_type, **kwargs)
            return data

    def trending_get_trending_entry_detail_with_http_info(self, identifier, trending_entry_type, **kwargs):
        """
        Returns the detailed results for a specific trending entry.  Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.trending_get_trending_entry_detail_with_http_info(identifier, trending_entry_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str identifier: The identifier for the entity to be returned. (required)
        :param str trending_entry_type: The type of entity to be returned. (required)
        :return: InlineResponse20036
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'trending_entry_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trending_get_trending_entry_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params) or (params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `trending_get_trending_entry_detail`")
        # verify the required parameter 'trending_entry_type' is set
        if ('trending_entry_type' not in params) or (params['trending_entry_type'] is None):
            raise ValueError("Missing the required parameter `trending_entry_type` when calling `trending_get_trending_entry_detail`")


        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']
        if 'trending_entry_type' in params:
            path_params['trendingEntryType'] = params['trending_entry_type']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/Trending/Details/{trendingEntryType}/{identifier}/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20036',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
