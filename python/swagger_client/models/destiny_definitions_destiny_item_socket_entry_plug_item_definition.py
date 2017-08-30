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


class DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition(object):
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
        'plug_item_hash': 'int'
    }

    attribute_map = {
        'plug_item_hash': 'plugItemHash'
    }

    def __init__(self, plug_item_hash=None):
        """
        DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition - a model defined in Swagger
        """

        self._plug_item_hash = None

        if plug_item_hash is not None:
          self.plug_item_hash = plug_item_hash

    @property
    def plug_item_hash(self):
        """
        Gets the plug_item_hash of this DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition.
        The hash identifier of a DestinyInventoryItemDefinition representing the plug  that can be inserted.

        :return: The plug_item_hash of this DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition.
        :rtype: int
        """
        return self._plug_item_hash

    @plug_item_hash.setter
    def plug_item_hash(self, plug_item_hash):
        """
        Sets the plug_item_hash of this DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition.
        The hash identifier of a DestinyInventoryItemDefinition representing the plug  that can be inserted.

        :param plug_item_hash: The plug_item_hash of this DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition.
        :type: int
        """

        self._plug_item_hash = plug_item_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
