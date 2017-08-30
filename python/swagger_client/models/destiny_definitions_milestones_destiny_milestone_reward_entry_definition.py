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


class DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition(object):
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
        'reward_entry_hash': 'int',
        'reward_entry_identifier': 'str',
        'items': 'list[DestinyDestinyItemQuantity]',
        'vendor_hash': 'int',
        'order': 'int'
    }

    attribute_map = {
        'reward_entry_hash': 'rewardEntryHash',
        'reward_entry_identifier': 'rewardEntryIdentifier',
        'items': 'items',
        'vendor_hash': 'vendorHash',
        'order': 'order'
    }

    def __init__(self, reward_entry_hash=None, reward_entry_identifier=None, items=None, vendor_hash=None, order=None):
        """
        DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition - a model defined in Swagger
        """

        self._reward_entry_hash = None
        self._reward_entry_identifier = None
        self._items = None
        self._vendor_hash = None
        self._order = None

        if reward_entry_hash is not None:
          self.reward_entry_hash = reward_entry_hash
        if reward_entry_identifier is not None:
          self.reward_entry_identifier = reward_entry_identifier
        if items is not None:
          self.items = items
        if vendor_hash is not None:
          self.vendor_hash = vendor_hash
        if order is not None:
          self.order = order

    @property
    def reward_entry_hash(self):
        """
        Gets the reward_entry_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The identifier for this reward entry.  Runtime data will refer to reward entries  by this hash.  Only guaranteed unique within the specific Milestone.

        :return: The reward_entry_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :rtype: int
        """
        return self._reward_entry_hash

    @reward_entry_hash.setter
    def reward_entry_hash(self, reward_entry_hash):
        """
        Sets the reward_entry_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The identifier for this reward entry.  Runtime data will refer to reward entries  by this hash.  Only guaranteed unique within the specific Milestone.

        :param reward_entry_hash: The reward_entry_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :type: int
        """

        self._reward_entry_hash = reward_entry_hash

    @property
    def reward_entry_identifier(self):
        """
        Gets the reward_entry_identifier of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The string identifier, if you care about it.  Only guaranteed unique within the specific Milestone.

        :return: The reward_entry_identifier of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :rtype: str
        """
        return self._reward_entry_identifier

    @reward_entry_identifier.setter
    def reward_entry_identifier(self, reward_entry_identifier):
        """
        Sets the reward_entry_identifier of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The string identifier, if you care about it.  Only guaranteed unique within the specific Milestone.

        :param reward_entry_identifier: The reward_entry_identifier of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :type: str
        """

        self._reward_entry_identifier = reward_entry_identifier

    @property
    def items(self):
        """
        Gets the items of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The items you will get as rewards, and how much of it you'll get.

        :return: The items of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :rtype: list[DestinyDestinyItemQuantity]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        The items you will get as rewards, and how much of it you'll get.

        :param items: The items of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :type: list[DestinyDestinyItemQuantity]
        """

        self._items = items

    @property
    def vendor_hash(self):
        """
        Gets the vendor_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order  to redeem the reward.  Use this hash to look up the DestinyVendorDefinition.

        :return: The vendor_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :rtype: int
        """
        return self._vendor_hash

    @vendor_hash.setter
    def vendor_hash(self, vendor_hash):
        """
        Sets the vendor_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in order  to redeem the reward.  Use this hash to look up the DestinyVendorDefinition.

        :param vendor_hash: The vendor_hash of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :type: int
        """

        self._vendor_hash = vendor_hash

    @property
    def order(self):
        """
        Gets the order of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        If you want to follow BNet's ordering of these rewards, use this number within a given category  to order the rewards.  Yeah, I know.  I feel dirty too.

        :return: The order of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        If you want to follow BNet's ordering of these rewards, use this number within a given category  to order the rewards.  Yeah, I know.  I feel dirty too.

        :param order: The order of this DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition.
        :type: int
        """

        self._order = order

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
        if not isinstance(other, DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
