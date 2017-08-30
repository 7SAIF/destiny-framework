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


class DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition(object):
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
        'conceptual_activity_hash': 'int',
        'variants': 'dict(str, DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition)'
    }

    attribute_map = {
        'conceptual_activity_hash': 'conceptualActivityHash',
        'variants': 'variants'
    }

    def __init__(self, conceptual_activity_hash=None, variants=None):
        """
        DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition - a model defined in Swagger
        """

        self._conceptual_activity_hash = None
        self._variants = None

        if conceptual_activity_hash is not None:
          self.conceptual_activity_hash = conceptual_activity_hash
        if variants is not None:
          self.variants = variants

    @property
    def conceptual_activity_hash(self):
        """
        Gets the conceptual_activity_hash of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        The \"Conceptual\" activity hash.  Basically, we picked the lowest level activity  and are treating it as the canonical definition of the activity for rendering purposes.    If you care about the specific difficulty modes and variations, use the activities under  \"Variants\".

        :return: The conceptual_activity_hash of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        :rtype: int
        """
        return self._conceptual_activity_hash

    @conceptual_activity_hash.setter
    def conceptual_activity_hash(self, conceptual_activity_hash):
        """
        Sets the conceptual_activity_hash of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        The \"Conceptual\" activity hash.  Basically, we picked the lowest level activity  and are treating it as the canonical definition of the activity for rendering purposes.    If you care about the specific difficulty modes and variations, use the activities under  \"Variants\".

        :param conceptual_activity_hash: The conceptual_activity_hash of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        :type: int
        """

        self._conceptual_activity_hash = conceptual_activity_hash

    @property
    def variants(self):
        """
        Gets the variants of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        A milestone-referenced activity can have many variants, such as Tiers or alternative modes of play.    Even if there is only a single variant, the details for these are represented within as a variant definition.    It is assumed that, if this DestinyMilestoneActivityDefinition is active, then all variants should be active.    If a Milestone could ever split the variants' active status conditionally, they should all have their own   DestinyMilestoneActivityDefinition instead!  The potential duplication will be worth it for the obviousness of processing  and use.

        :return: The variants of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        :rtype: dict(str, DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition)
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """
        Sets the variants of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        A milestone-referenced activity can have many variants, such as Tiers or alternative modes of play.    Even if there is only a single variant, the details for these are represented within as a variant definition.    It is assumed that, if this DestinyMilestoneActivityDefinition is active, then all variants should be active.    If a Milestone could ever split the variants' active status conditionally, they should all have their own   DestinyMilestoneActivityDefinition instead!  The potential duplication will be worth it for the obviousness of processing  and use.

        :param variants: The variants of this DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.
        :type: dict(str, DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition)
        """

        self._variants = variants

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
        if not isinstance(other, DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
