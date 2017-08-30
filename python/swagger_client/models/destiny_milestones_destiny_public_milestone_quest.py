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


class DestinyMilestonesDestinyPublicMilestoneQuest(object):
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
        'quest_item_hash': 'int',
        'challenges': 'list[DestinyMilestonesDestinyPublicMilestoneChallenge]'
    }

    attribute_map = {
        'quest_item_hash': 'questItemHash',
        'challenges': 'challenges'
    }

    def __init__(self, quest_item_hash=None, challenges=None):
        """
        DestinyMilestonesDestinyPublicMilestoneQuest - a model defined in Swagger
        """

        self._quest_item_hash = None
        self._challenges = None

        if quest_item_hash is not None:
          self.quest_item_hash = quest_item_hash
        if challenges is not None:
          self.challenges = challenges

    @property
    def quest_item_hash(self):
        """
        Gets the quest_item_hash of this DestinyMilestonesDestinyPublicMilestoneQuest.
        Quests are defined as Items in content.  As such, this is the hash identifier   of the DestinyInventoryItemDefinition that represents this quest.  It will have pointers to all of the steps  in the quest, and display information for the quest (title, description, icon etc)  Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData  property, and themselves are Items with their own renderable data.

        :return: The quest_item_hash of this DestinyMilestonesDestinyPublicMilestoneQuest.
        :rtype: int
        """
        return self._quest_item_hash

    @quest_item_hash.setter
    def quest_item_hash(self, quest_item_hash):
        """
        Sets the quest_item_hash of this DestinyMilestonesDestinyPublicMilestoneQuest.
        Quests are defined as Items in content.  As such, this is the hash identifier   of the DestinyInventoryItemDefinition that represents this quest.  It will have pointers to all of the steps  in the quest, and display information for the quest (title, description, icon etc)  Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData  property, and themselves are Items with their own renderable data.

        :param quest_item_hash: The quest_item_hash of this DestinyMilestonesDestinyPublicMilestoneQuest.
        :type: int
        """

        self._quest_item_hash = quest_item_hash

    @property
    def challenges(self):
        """
        Gets the challenges of this DestinyMilestonesDestinyPublicMilestoneQuest.
        For the given quest there could be 0-to-Many challenges: mini quests  that you can perform in the course of doing this quest, that may grant you rewards and benefits.

        :return: The challenges of this DestinyMilestonesDestinyPublicMilestoneQuest.
        :rtype: list[DestinyMilestonesDestinyPublicMilestoneChallenge]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """
        Sets the challenges of this DestinyMilestonesDestinyPublicMilestoneQuest.
        For the given quest there could be 0-to-Many challenges: mini quests  that you can perform in the course of doing this quest, that may grant you rewards and benefits.

        :param challenges: The challenges of this DestinyMilestonesDestinyPublicMilestoneQuest.
        :type: list[DestinyMilestonesDestinyPublicMilestoneChallenge]
        """

        self._challenges = challenges

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
        if not isinstance(other, DestinyMilestonesDestinyPublicMilestoneQuest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
