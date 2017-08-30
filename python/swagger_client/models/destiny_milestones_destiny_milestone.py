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


class DestinyMilestonesDestinyMilestone(object):
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
        'milestone_hash': 'int',
        'available_quests': 'list[DestinyMilestonesDestinyMilestoneQuest]',
        'values': 'dict(str, float)',
        'vendor_hashes': 'list[int]',
        'rewards': 'list[DestinyMilestonesDestinyMilestoneRewardCategory]',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'milestone_hash': 'milestoneHash',
        'available_quests': 'availableQuests',
        'values': 'values',
        'vendor_hashes': 'vendorHashes',
        'rewards': 'rewards',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, milestone_hash=None, available_quests=None, values=None, vendor_hashes=None, rewards=None, start_date=None, end_date=None):
        """
        DestinyMilestonesDestinyMilestone - a model defined in Swagger
        """

        self._milestone_hash = None
        self._available_quests = None
        self._values = None
        self._vendor_hashes = None
        self._rewards = None
        self._start_date = None
        self._end_date = None

        if milestone_hash is not None:
          self.milestone_hash = milestone_hash
        if available_quests is not None:
          self.available_quests = available_quests
        if values is not None:
          self.values = values
        if vendor_hashes is not None:
          self.vendor_hashes = vendor_hashes
        if rewards is not None:
          self.rewards = rewards
        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date

    @property
    def milestone_hash(self):
        """
        Gets the milestone_hash of this DestinyMilestonesDestinyMilestone.
        The unique identifier for the Milestone.  Use it to look up the DestinyMilestoneDefinition, soyou can combine the other data in this contract with static definition data.

        :return: The milestone_hash of this DestinyMilestonesDestinyMilestone.
        :rtype: int
        """
        return self._milestone_hash

    @milestone_hash.setter
    def milestone_hash(self, milestone_hash):
        """
        Sets the milestone_hash of this DestinyMilestonesDestinyMilestone.
        The unique identifier for the Milestone.  Use it to look up the DestinyMilestoneDefinition, soyou can combine the other data in this contract with static definition data.

        :param milestone_hash: The milestone_hash of this DestinyMilestonesDestinyMilestone.
        :type: int
        """

        self._milestone_hash = milestone_hash

    @property
    def available_quests(self):
        """
        Gets the available_quests of this DestinyMilestonesDestinyMilestone.
        Indicates what quests are available for this Milestone.Usually this will be only a single Quest, but some quests have multiple available that youcan choose from at any given time.All possible quests for a milestone can be found in the DestinyMilestoneDefinition, but they mustbe combined with this Live data to determine which one(s) are actually active right now.It is possible for Milestones to not have any quests.

        :return: The available_quests of this DestinyMilestonesDestinyMilestone.
        :rtype: list[DestinyMilestonesDestinyMilestoneQuest]
        """
        return self._available_quests

    @available_quests.setter
    def available_quests(self, available_quests):
        """
        Sets the available_quests of this DestinyMilestonesDestinyMilestone.
        Indicates what quests are available for this Milestone.Usually this will be only a single Quest, but some quests have multiple available that youcan choose from at any given time.All possible quests for a milestone can be found in the DestinyMilestoneDefinition, but they mustbe combined with this Live data to determine which one(s) are actually active right now.It is possible for Milestones to not have any quests.

        :param available_quests: The available_quests of this DestinyMilestonesDestinyMilestone.
        :type: list[DestinyMilestonesDestinyMilestoneQuest]
        """

        self._available_quests = available_quests

    @property
    def values(self):
        """
        Gets the values of this DestinyMilestonesDestinyMilestone.
        Milestones may have arbitrary key/value pairs associated with them, for data that users willwant to know about but that doesn't fit neatly into any of the common components such as Quests.A good example of this would be - if this existed in Destiny 1 - the number of wins you currently haveon your Trials of Osiris ticket.Looking in the DestinyMilestoneDefinition,you can use the string identifier of this dictionary to look up more info about the value, includinglocalized string content for displaying the value.  The value in the dictionary is the floating pointnumber.  The definition will tell you how to format this number.

        :return: The values of this DestinyMilestonesDestinyMilestone.
        :rtype: dict(str, float)
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DestinyMilestonesDestinyMilestone.
        Milestones may have arbitrary key/value pairs associated with them, for data that users willwant to know about but that doesn't fit neatly into any of the common components such as Quests.A good example of this would be - if this existed in Destiny 1 - the number of wins you currently haveon your Trials of Osiris ticket.Looking in the DestinyMilestoneDefinition,you can use the string identifier of this dictionary to look up more info about the value, includinglocalized string content for displaying the value.  The value in the dictionary is the floating pointnumber.  The definition will tell you how to format this number.

        :param values: The values of this DestinyMilestonesDestinyMilestone.
        :type: dict(str, float)
        """

        self._values = values

    @property
    def vendor_hashes(self):
        """
        Gets the vendor_hashes of this DestinyMilestonesDestinyMilestone.
        A milestone may have one or more active vendors that are \"related\" to it (that provide rewards, or thatare the initiators of the Milestone).  I already regret this, even as I'm typing it.You see, sometimes a milestone may be directly correlated with a set of vendors that provide varying tiersof rewards.  The player may not be able to interact with one or more of those vendors.  This will returnthe hashes of the Vendors that the player *can* interact with, allowing you to show their current inventoryas rewards or related items to the Milestone or its activities.

        :return: The vendor_hashes of this DestinyMilestonesDestinyMilestone.
        :rtype: list[int]
        """
        return self._vendor_hashes

    @vendor_hashes.setter
    def vendor_hashes(self, vendor_hashes):
        """
        Sets the vendor_hashes of this DestinyMilestonesDestinyMilestone.
        A milestone may have one or more active vendors that are \"related\" to it (that provide rewards, or thatare the initiators of the Milestone).  I already regret this, even as I'm typing it.You see, sometimes a milestone may be directly correlated with a set of vendors that provide varying tiersof rewards.  The player may not be able to interact with one or more of those vendors.  This will returnthe hashes of the Vendors that the player *can* interact with, allowing you to show their current inventoryas rewards or related items to the Milestone or its activities.

        :param vendor_hashes: The vendor_hashes of this DestinyMilestonesDestinyMilestone.
        :type: list[int]
        """

        self._vendor_hashes = vendor_hashes

    @property
    def rewards(self):
        """
        Gets the rewards of this DestinyMilestonesDestinyMilestone.
        If the entity to which this component is attached has known active Rewards for the player, this will detailinformation about those rewards, keyed by the RewardEntry Hash. (See DestinyMilestoneDefinition formore information about Reward Entries)Note that these rewards are not for the Quests related to the Milestone.  Think of these as \"overview/checklist\"rewards that may be provided for Milestones that may provide rewards for performing a variety of tasks thataren't under a specific Quest.

        :return: The rewards of this DestinyMilestonesDestinyMilestone.
        :rtype: list[DestinyMilestonesDestinyMilestoneRewardCategory]
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """
        Sets the rewards of this DestinyMilestonesDestinyMilestone.
        If the entity to which this component is attached has known active Rewards for the player, this will detailinformation about those rewards, keyed by the RewardEntry Hash. (See DestinyMilestoneDefinition formore information about Reward Entries)Note that these rewards are not for the Quests related to the Milestone.  Think of these as \"overview/checklist\"rewards that may be provided for Milestones that may provide rewards for performing a variety of tasks thataren't under a specific Quest.

        :param rewards: The rewards of this DestinyMilestonesDestinyMilestone.
        :type: list[DestinyMilestonesDestinyMilestoneRewardCategory]
        """

        self._rewards = rewards

    @property
    def start_date(self):
        """
        Gets the start_date of this DestinyMilestonesDestinyMilestone.
        If known, this is the date when the event last began or refreshed.  It will only be populated for events with fixedand repeating start and end dates.

        :return: The start_date of this DestinyMilestonesDestinyMilestone.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this DestinyMilestonesDestinyMilestone.
        If known, this is the date when the event last began or refreshed.  It will only be populated for events with fixedand repeating start and end dates.

        :param start_date: The start_date of this DestinyMilestonesDestinyMilestone.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this DestinyMilestonesDestinyMilestone.
        If known, this is the date when the event will next end or repeat.  It will only be populated for events with fixedand repeating start and end dates.

        :return: The end_date of this DestinyMilestonesDestinyMilestone.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this DestinyMilestonesDestinyMilestone.
        If known, this is the date when the event will next end or repeat.  It will only be populated for events with fixedand repeating start and end dates.

        :param end_date: The end_date of this DestinyMilestonesDestinyMilestone.
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, DestinyMilestonesDestinyMilestone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
