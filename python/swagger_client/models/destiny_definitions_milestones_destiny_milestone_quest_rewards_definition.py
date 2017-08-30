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


class DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition(object):
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
        'items': 'list[DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None):
        """
        DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition - a model defined in Swagger
        """

        self._items = None

        if items is not None:
          self.items = items

    @property
    def items(self):
        """
        Gets the items of this DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition.
        The items that represent your reward for completing the quest.    Be warned, these could be \"dummy\" items: items that are only used to  render a good-looking in-game tooltip, but aren't the actual items themselves.    For instance, when experience is given there's often a dummy item representing \"experience\",  with quantity being the amount of experience you got.  We don't have a programmatic association  between those and whatever Progression is actually getting that experience... yet.

        :return: The items of this DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition.
        :rtype: list[DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition.
        The items that represent your reward for completing the quest.    Be warned, these could be \"dummy\" items: items that are only used to  render a good-looking in-game tooltip, but aren't the actual items themselves.    For instance, when experience is given there's often a dummy item representing \"experience\",  with quantity being the amount of experience you got.  We don't have a programmatic association  between those and whatever Progression is actually getting that experience... yet.

        :param items: The items of this DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition.
        :type: list[DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem]
        """

        self._items = items

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
        if not isinstance(other, DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
