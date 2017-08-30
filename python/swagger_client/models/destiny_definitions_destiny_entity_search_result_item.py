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


class DestinyDefinitionsDestinyEntitySearchResultItem(object):
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
        'hash': 'int',
        'entity_type': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'hash': 'hash',
        'entity_type': 'entityType',
        'weight': 'weight'
    }

    def __init__(self, hash=None, entity_type=None, weight=None):
        """
        DestinyDefinitionsDestinyEntitySearchResultItem - a model defined in Swagger
        """

        self._hash = None
        self._entity_type = None
        self._weight = None

        if hash is not None:
          self.hash = hash
        if entity_type is not None:
          self.entity_type = entity_type
        if weight is not None:
          self.weight = weight

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The hash identifier of the entity.  You will use this to look up the DestinyDefinition  relevant for the entity found.

        :return: The hash of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The hash identifier of the entity.  You will use this to look up the DestinyDefinition  relevant for the entity found.

        :param hash: The hash of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :type: int
        """

        self._hash = hash

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The type of entity, returned as a string matching the DestinyDefinition's contract class name.  You'll have to have your own mapping from class names to actually looking up those definitions  in the manifest databases.

        :return: The entity_type of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The type of entity, returned as a string matching the DestinyDefinition's contract class name.  You'll have to have your own mapping from class names to actually looking up those definitions  in the manifest databases.

        :param entity_type: The entity_type of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def weight(self):
        """
        Gets the weight of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The ranking value for sorting that we calculated using our relevance formula.  This  will hopefully get better with time and iteration.

        :return: The weight of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this DestinyDefinitionsDestinyEntitySearchResultItem.
        The ranking value for sorting that we calculated using our relevance formula.  This  will hopefully get better with time and iteration.

        :param weight: The weight of this DestinyDefinitionsDestinyEntitySearchResultItem.
        :type: float
        """

        self._weight = weight

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
        if not isinstance(other, DestinyDefinitionsDestinyEntitySearchResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other