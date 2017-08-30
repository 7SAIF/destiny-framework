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


class DestinyMilestonesDestinyMilestoneActivity(object):
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
        'activity_hash': 'int',
        'modifier_hashes': 'list[int]',
        'variants': 'list[DestinyMilestonesDestinyMilestoneActivityVariant]'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'modifier_hashes': 'modifierHashes',
        'variants': 'variants'
    }

    def __init__(self, activity_hash=None, modifier_hashes=None, variants=None):
        """
        DestinyMilestonesDestinyMilestoneActivity - a model defined in Swagger
        """

        self._activity_hash = None
        self._modifier_hashes = None
        self._variants = None

        if activity_hash is not None:
          self.activity_hash = activity_hash
        if modifier_hashes is not None:
          self.modifier_hashes = modifier_hashes
        if variants is not None:
          self.variants = variants

    @property
    def activity_hash(self):
        """
        Gets the activity_hash of this DestinyMilestonesDestinyMilestoneActivity.
        The hash of an arbitrarily chosen variant of this activity.  We'll go ahead and  call that the \"canonical\" activity, because if you're using this value you should  only use it for properties that are common across the variants: things like the  name of the activity, it's location, etc...  Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.

        :return: The activity_hash of this DestinyMilestonesDestinyMilestoneActivity.
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """
        Sets the activity_hash of this DestinyMilestonesDestinyMilestoneActivity.
        The hash of an arbitrarily chosen variant of this activity.  We'll go ahead and  call that the \"canonical\" activity, because if you're using this value you should  only use it for properties that are common across the variants: things like the  name of the activity, it's location, etc...  Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.

        :param activity_hash: The activity_hash of this DestinyMilestonesDestinyMilestoneActivity.
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def modifier_hashes(self):
        """
        Gets the modifier_hashes of this DestinyMilestonesDestinyMilestoneActivity.
        If the activity has modifiers, this will be the list of modifiers that all variants  have in common.  Perform lookups against  DestinyActivityModifierDefinition which defines the modifier being applied to get  at the modifier data.  Note that, in the DestiyActivityDefinition, you will see many more modifiers than this  being referred to: those are all *possible* modifiers for the activity, not the active ones.  Use only the active ones to match what's really live.

        :return: The modifier_hashes of this DestinyMilestonesDestinyMilestoneActivity.
        :rtype: list[int]
        """
        return self._modifier_hashes

    @modifier_hashes.setter
    def modifier_hashes(self, modifier_hashes):
        """
        Sets the modifier_hashes of this DestinyMilestonesDestinyMilestoneActivity.
        If the activity has modifiers, this will be the list of modifiers that all variants  have in common.  Perform lookups against  DestinyActivityModifierDefinition which defines the modifier being applied to get  at the modifier data.  Note that, in the DestiyActivityDefinition, you will see many more modifiers than this  being referred to: those are all *possible* modifiers for the activity, not the active ones.  Use only the active ones to match what's really live.

        :param modifier_hashes: The modifier_hashes of this DestinyMilestonesDestinyMilestoneActivity.
        :type: list[int]
        """

        self._modifier_hashes = modifier_hashes

    @property
    def variants(self):
        """
        Gets the variants of this DestinyMilestonesDestinyMilestoneActivity.
        If you want more than just name/location/etc... you're going to have to dig into  and show the variants of the conceptual activity.  These will differ in seemingly  arbitrary ways, like difficulty level and modifiers applied.  Show it in whatever  way tickles your fancy.

        :return: The variants of this DestinyMilestonesDestinyMilestoneActivity.
        :rtype: list[DestinyMilestonesDestinyMilestoneActivityVariant]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """
        Sets the variants of this DestinyMilestonesDestinyMilestoneActivity.
        If you want more than just name/location/etc... you're going to have to dig into  and show the variants of the conceptual activity.  These will differ in seemingly  arbitrary ways, like difficulty level and modifiers applied.  Show it in whatever  way tickles your fancy.

        :param variants: The variants of this DestinyMilestonesDestinyMilestoneActivity.
        :type: list[DestinyMilestonesDestinyMilestoneActivityVariant]
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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
