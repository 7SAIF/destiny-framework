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


class DestinyDefinitionsDestinyStatOverrideDefinition(object):
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
        'stat_hash': 'int'
    }

    attribute_map = {
        'stat_hash': 'statHash'
    }

    def __init__(self, stat_hash=None):
        """
        DestinyDefinitionsDestinyStatOverrideDefinition - a model defined in Swagger
        """

        self._stat_hash = None

        if stat_hash is not None:
          self.stat_hash = stat_hash

    @property
    def stat_hash(self):
        """
        Gets the stat_hash of this DestinyDefinitionsDestinyStatOverrideDefinition.
        The hash identifier of the stat whose display properties are being overridden.

        :return: The stat_hash of this DestinyDefinitionsDestinyStatOverrideDefinition.
        :rtype: int
        """
        return self._stat_hash

    @stat_hash.setter
    def stat_hash(self, stat_hash):
        """
        Sets the stat_hash of this DestinyDefinitionsDestinyStatOverrideDefinition.
        The hash identifier of the stat whose display properties are being overridden.

        :param stat_hash: The stat_hash of this DestinyDefinitionsDestinyStatOverrideDefinition.
        :type: int
        """

        self._stat_hash = stat_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyStatOverrideDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
