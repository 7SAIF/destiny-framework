# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.1.1
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.content_content_item_public_contract import ContentContentItemPublicContract  # noqa: F401,E501


class TrendingTrendingEntryNews(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'article': 'ContentContentItemPublicContract'
    }

    attribute_map = {
        'article': 'article'
    }

    def __init__(self, article=None):  # noqa: E501
        """TrendingTrendingEntryNews - a model defined in Swagger"""  # noqa: E501

        self._article = None
        self.discriminator = None

        if article is not None:
            self.article = article

    @property
    def article(self):
        """Gets the article of this TrendingTrendingEntryNews.  # noqa: E501


        :return: The article of this TrendingTrendingEntryNews.  # noqa: E501
        :rtype: ContentContentItemPublicContract
        """
        return self._article

    @article.setter
    def article(self, article):
        """Sets the article of this TrendingTrendingEntryNews.


        :param article: The article of this TrendingTrendingEntryNews.  # noqa: E501
        :type: ContentContentItemPublicContract
        """

        self._article = article

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrendingTrendingEntryNews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
