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


class DestinyDefinitionsDestinyTalentNodeCategory(object):
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
        'identifier': 'str',
        'is_lore_driven': 'bool',
        'node_hashes': 'list[int]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'is_lore_driven': 'isLoreDriven',
        'node_hashes': 'nodeHashes'
    }

    def __init__(self, identifier=None, is_lore_driven=None, node_hashes=None):
        """
        DestinyDefinitionsDestinyTalentNodeCategory - a model defined in Swagger
        """

        self._identifier = None
        self._is_lore_driven = None
        self._node_hashes = None

        if identifier is not None:
          self.identifier = identifier
        if is_lore_driven is not None:
          self.is_lore_driven = is_lore_driven
        if node_hashes is not None:
          self.node_hashes = node_hashes

    @property
    def identifier(self):
        """
        Gets the identifier of this DestinyDefinitionsDestinyTalentNodeCategory.
        Mostly just for debug purposes, but if you find it useful you can have it.  This is BNet's manually created identifier for this category.

        :return: The identifier of this DestinyDefinitionsDestinyTalentNodeCategory.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DestinyDefinitionsDestinyTalentNodeCategory.
        Mostly just for debug purposes, but if you find it useful you can have it.  This is BNet's manually created identifier for this category.

        :param identifier: The identifier of this DestinyDefinitionsDestinyTalentNodeCategory.
        :type: str
        """

        self._identifier = identifier

    @property
    def is_lore_driven(self):
        """
        Gets the is_lore_driven of this DestinyDefinitionsDestinyTalentNodeCategory.
        If true, we found the localized content in a related DestinyLoreDefinition  instead of local BNet localization files.  This is mostly for ease of my own future investigations.

        :return: The is_lore_driven of this DestinyDefinitionsDestinyTalentNodeCategory.
        :rtype: bool
        """
        return self._is_lore_driven

    @is_lore_driven.setter
    def is_lore_driven(self, is_lore_driven):
        """
        Sets the is_lore_driven of this DestinyDefinitionsDestinyTalentNodeCategory.
        If true, we found the localized content in a related DestinyLoreDefinition  instead of local BNet localization files.  This is mostly for ease of my own future investigations.

        :param is_lore_driven: The is_lore_driven of this DestinyDefinitionsDestinyTalentNodeCategory.
        :type: bool
        """

        self._is_lore_driven = is_lore_driven

    @property
    def node_hashes(self):
        """
        Gets the node_hashes of this DestinyDefinitionsDestinyTalentNodeCategory.
        The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition)  in this Talent Grid that are part of this Category.

        :return: The node_hashes of this DestinyDefinitionsDestinyTalentNodeCategory.
        :rtype: list[int]
        """
        return self._node_hashes

    @node_hashes.setter
    def node_hashes(self, node_hashes):
        """
        Sets the node_hashes of this DestinyDefinitionsDestinyTalentNodeCategory.
        The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition)  in this Talent Grid that are part of this Category.

        :param node_hashes: The node_hashes of this DestinyDefinitionsDestinyTalentNodeCategory.
        :type: list[int]
        """

        self._node_hashes = node_hashes

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
        if not isinstance(other, DestinyDefinitionsDestinyTalentNodeCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
