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


class DestinyHistoricalStatsDestinyLeaderboardEntry(object):
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
        'rank': 'int',
        'character_id': 'int'
    }

    attribute_map = {
        'rank': 'rank',
        'character_id': 'characterId'
    }

    def __init__(self, rank=None, character_id=None):
        """
        DestinyHistoricalStatsDestinyLeaderboardEntry - a model defined in Swagger
        """

        self._rank = None
        self._character_id = None

        if rank is not None:
          self.rank = rank
        if character_id is not None:
          self.character_id = character_id

    @property
    def rank(self):
        """
        Gets the rank of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        Where this player ranks on the leaderboard.  A value of 1 is the top rank.

        :return: The rank of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        Where this player ranks on the leaderboard.  A value of 1 is the top rank.

        :param rank: The rank of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        :type: int
        """

        self._rank = rank

    @property
    def character_id(self):
        """
        Gets the character_id of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        ID of the player's best character for the reported stat.

        :return: The character_id of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        ID of the player's best character for the reported stat.

        :param character_id: The character_id of this DestinyHistoricalStatsDestinyLeaderboardEntry.
        :type: int
        """

        self._character_id = character_id

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
        if not isinstance(other, DestinyHistoricalStatsDestinyLeaderboardEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other