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


class DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition(object):
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
        'category_hash': 'int',
        'category_identifier': 'str'
    }

    attribute_map = {
        'category_hash': 'categoryHash',
        'category_identifier': 'categoryIdentifier'
    }

    def __init__(self, category_hash=None, category_identifier=None):
        """
        DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition - a model defined in Swagger
        """

        self._category_hash = None
        self._category_identifier = None

        if category_hash is not None:
          self.category_hash = category_hash
        if category_identifier is not None:
          self.category_identifier = category_identifier

    @property
    def category_hash(self):
        """
        Gets the category_hash of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.  Note that this does NOT relate to any Definition in itself, it is only used for comparison purposes.

        :return: The category_hash of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        :rtype: int
        """
        return self._category_hash

    @category_hash.setter
    def category_hash(self, category_hash):
        """
        Sets the category_hash of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.  Note that this does NOT relate to any Definition in itself, it is only used for comparison purposes.

        :param category_hash: The category_hash of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        :type: int
        """

        self._category_hash = category_hash

    @property
    def category_identifier(self):
        """
        Gets the category_identifier of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        The string identifier for the category, which is here mostly for debug purposes.

        :return: The category_identifier of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        :rtype: str
        """
        return self._category_identifier

    @category_identifier.setter
    def category_identifier(self, category_identifier):
        """
        Sets the category_identifier of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        The string identifier for the category, which is here mostly for debug purposes.

        :param category_identifier: The category_identifier of this DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition.
        :type: str
        """

        self._category_identifier = category_identifier

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
        if not isinstance(other, DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
