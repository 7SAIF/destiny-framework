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


class DestinyHistoricalStatsDestinyLeaderboardResults(object):
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
        'focus_membership_id': 'int',
        'focus_character_id': 'int'
    }

    attribute_map = {
        'focus_membership_id': 'focusMembershipId',
        'focus_character_id': 'focusCharacterId'
    }

    def __init__(self, focus_membership_id=None, focus_character_id=None):
        """
        DestinyHistoricalStatsDestinyLeaderboardResults - a model defined in Swagger
        """

        self._focus_membership_id = None
        self._focus_character_id = None

        if focus_membership_id is not None:
          self.focus_membership_id = focus_membership_id
        if focus_character_id is not None:
          self.focus_character_id = focus_character_id

    @property
    def focus_membership_id(self):
        """
        Gets the focus_membership_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        Indicate the membership ID of the account that is the focal point of  the provided leaderboards.

        :return: The focus_membership_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        :rtype: int
        """
        return self._focus_membership_id

    @focus_membership_id.setter
    def focus_membership_id(self, focus_membership_id):
        """
        Sets the focus_membership_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        Indicate the membership ID of the account that is the focal point of  the provided leaderboards.

        :param focus_membership_id: The focus_membership_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        :type: int
        """

        self._focus_membership_id = focus_membership_id

    @property
    def focus_character_id(self):
        """
        Gets the focus_character_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        Indicate the character ID of the character that is the focal point of  the provided leaderboards. May be null, in which case any character  from the focus membership can appear in the provided leaderboards.

        :return: The focus_character_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        :rtype: int
        """
        return self._focus_character_id

    @focus_character_id.setter
    def focus_character_id(self, focus_character_id):
        """
        Sets the focus_character_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        Indicate the character ID of the character that is the focal point of  the provided leaderboards. May be null, in which case any character  from the focus membership can appear in the provided leaderboards.

        :param focus_character_id: The focus_character_id of this DestinyHistoricalStatsDestinyLeaderboardResults.
        :type: int
        """

        self._focus_character_id = focus_character_id

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
        if not isinstance(other, DestinyHistoricalStatsDestinyLeaderboardResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
