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


class DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry(object):
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
        'team_id': 'int',
        'standing': 'object',
        'score': 'object',
        'team_name': 'str'
    }

    attribute_map = {
        'team_id': 'teamId',
        'standing': 'standing',
        'score': 'score',
        'team_name': 'teamName'
    }

    def __init__(self, team_id=None, standing=None, score=None, team_name=None):  # noqa: E501
        """DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry - a model defined in Swagger"""  # noqa: E501

        self._team_id = None
        self._standing = None
        self._score = None
        self._team_name = None
        self.discriminator = None

        if team_id is not None:
            self.team_id = team_id
        if standing is not None:
            self.standing = standing
        if score is not None:
            self.score = score
        if team_name is not None:
            self.team_name = team_name

    @property
    def team_id(self):
        """Gets the team_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501

        Integer ID for the team.  # noqa: E501

        :return: The team_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.

        Integer ID for the team.  # noqa: E501

        :param team_id: The team_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def standing(self):
        """Gets the standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501

        Team's standing relative to other teams.  # noqa: E501

        :return: The standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :rtype: object
        """
        return self._standing

    @standing.setter
    def standing(self, standing):
        """Sets the standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.

        Team's standing relative to other teams.  # noqa: E501

        :param standing: The standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :type: object
        """

        self._standing = standing

    @property
    def score(self):
        """Gets the score of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501

        Score earned by the team  # noqa: E501

        :return: The score of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :rtype: object
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.

        Score earned by the team  # noqa: E501

        :param score: The score of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :type: object
        """

        self._score = score

    @property
    def team_name(self):
        """Gets the team_name of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501

        Alpha or Bravo  # noqa: E501

        :return: The team_name of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.

        Alpha or Bravo  # noqa: E501

        :param team_name: The team_name of this DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

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
        if not isinstance(other, DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
