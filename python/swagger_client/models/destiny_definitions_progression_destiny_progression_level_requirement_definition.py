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

from swagger_client.models.interpolation_interpolation_point_float import InterpolationInterpolationPointFloat  # noqa: F401,E501


class DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition(object):
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
        'requirement_curve': 'list[InterpolationInterpolationPointFloat]',
        'progression_hash': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'requirement_curve': 'requirementCurve',
        'progression_hash': 'progressionHash',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, requirement_curve=None, progression_hash=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition - a model defined in Swagger"""  # noqa: E501

        self._requirement_curve = None
        self._progression_hash = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if requirement_curve is not None:
            self.requirement_curve = requirement_curve
        if progression_hash is not None:
            self.progression_hash = progression_hash
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def requirement_curve(self):
        """Gets the requirement_curve of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501

        A curve of level requirements, weighted by the related progressions' level.  Interpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.  # noqa: E501

        :return: The requirement_curve of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :rtype: list[InterpolationInterpolationPointFloat]
        """
        return self._requirement_curve

    @requirement_curve.setter
    def requirement_curve(self, requirement_curve):
        """Sets the requirement_curve of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.

        A curve of level requirements, weighted by the related progressions' level.  Interpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.  # noqa: E501

        :param requirement_curve: The requirement_curve of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :type: list[InterpolationInterpolationPointFloat]
        """

        self._requirement_curve = requirement_curve

    @property
    def progression_hash(self):
        """Gets the progression_hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501

        The progression whose level should be used to determine the level requirement.  Look up the DestinyProgressionDefinition with this hash for more information about the progression in question.  # noqa: E501

        :return: The progression_hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :rtype: int
        """
        return self._progression_hash

    @progression_hash.setter
    def progression_hash(self, progression_hash):
        """Sets the progression_hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.

        The progression whose level should be used to determine the level requirement.  Look up the DestinyProgressionDefinition with this hash for more information about the progression in question.  # noqa: E501

        :param progression_hash: The progression_hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :type: int
        """

        self._progression_hash = progression_hash

    @property
    def hash(self):
        """Gets the hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition.  # noqa: E501
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
