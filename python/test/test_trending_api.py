# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.1.1
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.trending_api import TrendingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrendingApi(unittest.TestCase):
    """TrendingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.trending_api.TrendingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_trending_get_trending_categories(self):
        """Test case for trending_get_trending_categories

        """
        pass

    def test_trending_get_trending_category(self):
        """Test case for trending_get_trending_category

        """
        pass

    def test_trending_get_trending_entry_detail(self):
        """Test case for trending_get_trending_entry_detail

        """
        pass


if __name__ == '__main__':
    unittest.main()
