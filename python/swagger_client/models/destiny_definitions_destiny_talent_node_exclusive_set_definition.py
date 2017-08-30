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


class DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition(object):
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
        'node_indexes': 'list[int]'
    }

    attribute_map = {
        'node_indexes': 'nodeIndexes'
    }

    def __init__(self, node_indexes=None):
        """
        DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition - a model defined in Swagger
        """

        self._node_indexes = None

        if node_indexes is not None:
          self.node_indexes = node_indexes

    @property
    def node_indexes(self):
        """
        Gets the node_indexes of this DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition.
        The list of node indexes for the exclusive set.  Historically, these were indexes.  I would have liked to replace this with nodeHashes for consistency, but it's way too late for that.  (9:09 PM, he's right!)

        :return: The node_indexes of this DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition.
        :rtype: list[int]
        """
        return self._node_indexes

    @node_indexes.setter
    def node_indexes(self, node_indexes):
        """
        Sets the node_indexes of this DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition.
        The list of node indexes for the exclusive set.  Historically, these were indexes.  I would have liked to replace this with nodeHashes for consistency, but it's way too late for that.  (9:09 PM, he's right!)

        :param node_indexes: The node_indexes of this DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition.
        :type: list[int]
        """

        self._node_indexes = node_indexes

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
        if not isinstance(other, DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
