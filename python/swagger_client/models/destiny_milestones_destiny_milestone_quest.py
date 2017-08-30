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


class DestinyMilestonesDestinyMilestoneQuest(object):
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
        'challenges': 'list[DestinyChallengesDestinyChallengeStatus]'
    }

    attribute_map = {
        'quest_item_hash': 'questItemHash',
        'challenges': 'challenges'
    }

    def __init__(self, quest_item_hash=None, challenges=None):
        """
        DestinyMilestonesDestinyMilestoneQuest - a model defined in Swagger
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
        Gets the quest_item_hash of this DestinyMilestonesDestinyMilestoneQuest.
        Quests are defined as Items in content.  As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest.  It will have pointers to all of the stepsin the quest, and display information for the quest (title, description, icon etc)Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setDataproperty, and themselves are Items with their own renderable data.

        :return: The quest_item_hash of this DestinyMilestonesDestinyMilestoneQuest.
        :rtype: int
        """
        return self._quest_item_hash

    @quest_item_hash.setter
    def quest_item_hash(self, quest_item_hash):
        """
        Sets the quest_item_hash of this DestinyMilestonesDestinyMilestoneQuest.
        Quests are defined as Items in content.  As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest.  It will have pointers to all of the stepsin the quest, and display information for the quest (title, description, icon etc)Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setDataproperty, and themselves are Items with their own renderable data.

        :param quest_item_hash: The quest_item_hash of this DestinyMilestonesDestinyMilestoneQuest.
        :type: int
        """

        self._quest_item_hash = quest_item_hash

    @property
    def challenges(self):
        """
        Gets the challenges of this DestinyMilestonesDestinyMilestoneQuest.
        The activities referred to by this quest can have many associated challenges.They are all contained here, with activityHashes so that you can associate them withthe specific activity variants in which they can be found.In retrospect, I probably should have put these under the specific Activity Variants,but it's too late to change it now.Theoretically, a quest without Activities can still have Challenges, which is whythis is on a higher level than activity/variants, but it probably should have beenin both places.  That may come as a later revision.

        :return: The challenges of this DestinyMilestonesDestinyMilestoneQuest.
        :rtype: list[DestinyChallengesDestinyChallengeStatus]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """
        Sets the challenges of this DestinyMilestonesDestinyMilestoneQuest.
        The activities referred to by this quest can have many associated challenges.They are all contained here, with activityHashes so that you can associate them withthe specific activity variants in which they can be found.In retrospect, I probably should have put these under the specific Activity Variants,but it's too late to change it now.Theoretically, a quest without Activities can still have Challenges, which is whythis is on a higher level than activity/variants, but it probably should have beenin both places.  That may come as a later revision.

        :param challenges: The challenges of this DestinyMilestonesDestinyMilestoneQuest.
        :type: list[DestinyChallengesDestinyChallengeStatus]
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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneQuest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
