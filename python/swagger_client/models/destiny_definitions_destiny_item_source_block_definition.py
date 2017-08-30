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


class DestinyDefinitionsDestinyItemSourceBlockDefinition(object):
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
        'source_hashes': 'list[int]',
        'sources': 'list[DestinyDefinitionsSourcesDestinyItemSourceDefinition]'
    }

    attribute_map = {
        'source_hashes': 'sourceHashes',
        'sources': 'sources'
    }

    def __init__(self, source_hashes=None, sources=None):
        """
        DestinyDefinitionsDestinyItemSourceBlockDefinition - a model defined in Swagger
        """

        self._source_hashes = None
        self._sources = None

        if source_hashes is not None:
          self.source_hashes = source_hashes
        if sources is not None:
          self.sources = sources

    @property
    def source_hashes(self):
        """
        Gets the source_hashes of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition).

        :return: The source_hashes of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        :rtype: list[int]
        """
        return self._source_hashes

    @source_hashes.setter
    def source_hashes(self, source_hashes):
        """
        Sets the source_hashes of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition).

        :param source_hashes: The source_hashes of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        :type: list[int]
        """

        self._source_hashes = source_hashes

    @property
    def sources(self):
        """
        Gets the sources of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        A collection of details about the stats that were computed for the ways we found that the item  could be spawned.

        :return: The sources of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        :rtype: list[DestinyDefinitionsSourcesDestinyItemSourceDefinition]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        A collection of details about the stats that were computed for the ways we found that the item  could be spawned.

        :param sources: The sources of this DestinyDefinitionsDestinyItemSourceBlockDefinition.
        :type: list[DestinyDefinitionsSourcesDestinyItemSourceDefinition]
        """

        self._sources = sources

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
        if not isinstance(other, DestinyDefinitionsDestinyItemSourceBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
