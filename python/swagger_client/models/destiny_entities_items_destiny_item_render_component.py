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


class DestinyEntitiesItemsDestinyItemRenderComponent(object):
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
        'use_custom_dyes': 'bool',
        'art_regions': 'dict(str, int)'
    }

    attribute_map = {
        'use_custom_dyes': 'useCustomDyes',
        'art_regions': 'artRegions'
    }

    def __init__(self, use_custom_dyes=None, art_regions=None):  # noqa: E501
        """DestinyEntitiesItemsDestinyItemRenderComponent - a model defined in Swagger"""  # noqa: E501

        self._use_custom_dyes = None
        self._art_regions = None
        self.discriminator = None

        if use_custom_dyes is not None:
            self.use_custom_dyes = use_custom_dyes
        if art_regions is not None:
            self.art_regions = art_regions

    @property
    def use_custom_dyes(self):
        """Gets the use_custom_dyes of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501

        If you should use custom dyes on this item, it will be indicated here.  # noqa: E501

        :return: The use_custom_dyes of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_dyes

    @use_custom_dyes.setter
    def use_custom_dyes(self, use_custom_dyes):
        """Sets the use_custom_dyes of this DestinyEntitiesItemsDestinyItemRenderComponent.

        If you should use custom dyes on this item, it will be indicated here.  # noqa: E501

        :param use_custom_dyes: The use_custom_dyes of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501
        :type: bool
        """

        self._use_custom_dyes = use_custom_dyes

    @property
    def art_regions(self):
        """Gets the art_regions of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501

        A dictionary for rendering gear components, with:  key = Art Arrangement Region Index  value = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.  # noqa: E501

        :return: The art_regions of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._art_regions

    @art_regions.setter
    def art_regions(self, art_regions):
        """Sets the art_regions of this DestinyEntitiesItemsDestinyItemRenderComponent.

        A dictionary for rendering gear components, with:  key = Art Arrangement Region Index  value = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.  # noqa: E501

        :param art_regions: The art_regions of this DestinyEntitiesItemsDestinyItemRenderComponent.  # noqa: E501
        :type: dict(str, int)
        """

        self._art_regions = art_regions

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
        if not isinstance(other, DestinyEntitiesItemsDestinyItemRenderComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
