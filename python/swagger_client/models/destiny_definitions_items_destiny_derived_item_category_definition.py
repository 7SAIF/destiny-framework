# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'category_description': 'str',
        'items': 'list[DestinyDefinitionsItemsDestinyDerivedItemDefinition]'
    }

    attribute_map = {
        'category_description': 'categoryDescription',
        'items': 'items'
    }

    def __init__(self, category_description=None, items=None):
        """
        DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition - a model defined in Swagger
        """

        self._category_description = None
        self._items = None

        if category_description is not None:
          self.category_description = category_description
        if items is not None:
          self.items = items

    @property
    def category_description(self):
        """
        Gets the category_description of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        The localized string for the category title.  This will be something describing  the items you can get as a group, or your likelihood/the quantity you'll get.

        :return: The category_description of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        :rtype: str
        """
        return self._category_description

    @category_description.setter
    def category_description(self, category_description):
        """
        Sets the category_description of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        The localized string for the category title.  This will be something describing  the items you can get as a group, or your likelihood/the quantity you'll get.

        :param category_description: The category_description of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        :type: str
        """

        self._category_description = category_description

    @property
    def items(self):
        """
        Gets the items of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        This is the list of all of the items for this category and the basic properties we'll  know about them.

        :return: The items of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        :rtype: list[DestinyDefinitionsItemsDestinyDerivedItemDefinition]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        This is the list of all of the items for this category and the basic properties we'll  know about them.

        :param items: The items of this DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition.
        :type: list[DestinyDefinitionsItemsDestinyDerivedItemDefinition]
        """

        self._items = items

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
