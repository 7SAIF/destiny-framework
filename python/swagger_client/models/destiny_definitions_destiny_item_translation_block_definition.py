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

from swagger_client.models.destiny_definitions_destiny_gear_art_arrangement_reference import DestinyDefinitionsDestinyGearArtArrangementReference  # noqa: F401,E501
from swagger_client.models.destiny_dye_reference import DestinyDyeReference  # noqa: F401,E501


class DestinyDefinitionsDestinyItemTranslationBlockDefinition(object):
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
        'weapon_pattern_identifier': 'str',
        'weapon_pattern_hash': 'int',
        'default_dyes': 'list[DestinyDyeReference]',
        'locked_dyes': 'list[DestinyDyeReference]',
        'custom_dyes': 'list[DestinyDyeReference]',
        'arrangements': 'list[DestinyDefinitionsDestinyGearArtArrangementReference]',
        'has_geometry': 'bool'
    }

    attribute_map = {
        'weapon_pattern_identifier': 'weaponPatternIdentifier',
        'weapon_pattern_hash': 'weaponPatternHash',
        'default_dyes': 'defaultDyes',
        'locked_dyes': 'lockedDyes',
        'custom_dyes': 'customDyes',
        'arrangements': 'arrangements',
        'has_geometry': 'hasGeometry'
    }

    def __init__(self, weapon_pattern_identifier=None, weapon_pattern_hash=None, default_dyes=None, locked_dyes=None, custom_dyes=None, arrangements=None, has_geometry=None):  # noqa: E501
        """DestinyDefinitionsDestinyItemTranslationBlockDefinition - a model defined in Swagger"""  # noqa: E501

        self._weapon_pattern_identifier = None
        self._weapon_pattern_hash = None
        self._default_dyes = None
        self._locked_dyes = None
        self._custom_dyes = None
        self._arrangements = None
        self._has_geometry = None
        self.discriminator = None

        if weapon_pattern_identifier is not None:
            self.weapon_pattern_identifier = weapon_pattern_identifier
        if weapon_pattern_hash is not None:
            self.weapon_pattern_hash = weapon_pattern_hash
        if default_dyes is not None:
            self.default_dyes = default_dyes
        if locked_dyes is not None:
            self.locked_dyes = locked_dyes
        if custom_dyes is not None:
            self.custom_dyes = custom_dyes
        if arrangements is not None:
            self.arrangements = arrangements
        if has_geometry is not None:
            self.has_geometry = has_geometry

    @property
    def weapon_pattern_identifier(self):
        """Gets the weapon_pattern_identifier of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The weapon_pattern_identifier of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._weapon_pattern_identifier

    @weapon_pattern_identifier.setter
    def weapon_pattern_identifier(self, weapon_pattern_identifier):
        """Sets the weapon_pattern_identifier of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param weapon_pattern_identifier: The weapon_pattern_identifier of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: str
        """

        self._weapon_pattern_identifier = weapon_pattern_identifier

    @property
    def weapon_pattern_hash(self):
        """Gets the weapon_pattern_hash of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The weapon_pattern_hash of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._weapon_pattern_hash

    @weapon_pattern_hash.setter
    def weapon_pattern_hash(self, weapon_pattern_hash):
        """Sets the weapon_pattern_hash of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param weapon_pattern_hash: The weapon_pattern_hash of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: int
        """

        self._weapon_pattern_hash = weapon_pattern_hash

    @property
    def default_dyes(self):
        """Gets the default_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The default_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: list[DestinyDyeReference]
        """
        return self._default_dyes

    @default_dyes.setter
    def default_dyes(self, default_dyes):
        """Sets the default_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param default_dyes: The default_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: list[DestinyDyeReference]
        """

        self._default_dyes = default_dyes

    @property
    def locked_dyes(self):
        """Gets the locked_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The locked_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: list[DestinyDyeReference]
        """
        return self._locked_dyes

    @locked_dyes.setter
    def locked_dyes(self, locked_dyes):
        """Sets the locked_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param locked_dyes: The locked_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: list[DestinyDyeReference]
        """

        self._locked_dyes = locked_dyes

    @property
    def custom_dyes(self):
        """Gets the custom_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The custom_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: list[DestinyDyeReference]
        """
        return self._custom_dyes

    @custom_dyes.setter
    def custom_dyes(self, custom_dyes):
        """Sets the custom_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param custom_dyes: The custom_dyes of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: list[DestinyDyeReference]
        """

        self._custom_dyes = custom_dyes

    @property
    def arrangements(self):
        """Gets the arrangements of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The arrangements of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: list[DestinyDefinitionsDestinyGearArtArrangementReference]
        """
        return self._arrangements

    @arrangements.setter
    def arrangements(self, arrangements):
        """Sets the arrangements of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param arrangements: The arrangements of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: list[DestinyDefinitionsDestinyGearArtArrangementReference]
        """

        self._arrangements = arrangements

    @property
    def has_geometry(self):
        """Gets the has_geometry of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501


        :return: The has_geometry of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._has_geometry

    @has_geometry.setter
    def has_geometry(self, has_geometry):
        """Sets the has_geometry of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.


        :param has_geometry: The has_geometry of this DestinyDefinitionsDestinyItemTranslationBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._has_geometry = has_geometry

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
        if not isinstance(other, DestinyDefinitionsDestinyItemTranslationBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
