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


class DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition(object):
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
        'description': 'str',
        'name': 'str',
        'icon': 'str',
        'has_icon': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'icon': 'icon',
        'has_icon': 'hasIcon'
    }

    def __init__(self, description=None, name=None, icon=None, has_icon=None):
        """
        DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition - a model defined in Swagger
        """

        self._description = None
        self._name = None
        self._icon = None
        self._has_icon = None

        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if icon is not None:
          self.icon = icon
        if has_icon is not None:
          self.has_icon = has_icon

    @property
    def description(self):
        """
        Gets the description of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :return: The description of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :param description: The description of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :return: The name of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :param name: The name of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :type: str
        """

        self._name = name

    @property
    def icon(self):
        """
        Gets the icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        Note that \"icon\" is sometimes misleading, and should be interpreted in the context of the entity.  For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.    But usually, it will be a small square image that you can use as... well, an icon.

        :return: The icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        Note that \"icon\" is sometimes misleading, and should be interpreted in the context of the entity.  For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.    But usually, it will be a small square image that you can use as... well, an icon.

        :param icon: The icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :type: str
        """

        self._icon = icon

    @property
    def has_icon(self):
        """
        Gets the has_icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :return: The has_icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :rtype: bool
        """
        return self._has_icon

    @has_icon.setter
    def has_icon(self, has_icon):
        """
        Sets the has_icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.

        :param has_icon: The has_icon of this DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.
        :type: bool
        """

        self._has_icon = has_icon

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
        if not isinstance(other, DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
