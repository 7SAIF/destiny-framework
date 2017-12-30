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


class DestinyDefinitionsDestinyObjectivePerkEntryDefinition(object):
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
        'perk_hash': 'int',
        'style': 'object'
    }

    attribute_map = {
        'perk_hash': 'perkHash',
        'style': 'style'
    }

    def __init__(self, perk_hash=None, style=None):  # noqa: E501
        """DestinyDefinitionsDestinyObjectivePerkEntryDefinition - a model defined in Swagger"""  # noqa: E501

        self._perk_hash = None
        self._style = None
        self.discriminator = None

        if perk_hash is not None:
            self.perk_hash = perk_hash
        if style is not None:
            self.style = style

    @property
    def perk_hash(self):
        """Gets the perk_hash of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501

        The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character.  # noqa: E501

        :return: The perk_hash of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._perk_hash

    @perk_hash.setter
    def perk_hash(self, perk_hash):
        """Sets the perk_hash of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.

        The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character.  # noqa: E501

        :param perk_hash: The perk_hash of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501
        :type: int
        """

        self._perk_hash = perk_hash

    @property
    def style(self):
        """Gets the style of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501

        An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed.  # noqa: E501

        :return: The style of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501
        :rtype: object
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.

        An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed.  # noqa: E501

        :param style: The style of this DestinyDefinitionsDestinyObjectivePerkEntryDefinition.  # noqa: E501
        :type: object
        """

        self._style = style

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
        if not isinstance(other, DestinyDefinitionsDestinyObjectivePerkEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
