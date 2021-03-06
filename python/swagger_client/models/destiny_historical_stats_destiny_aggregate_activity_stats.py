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

from swagger_client.models.destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue  # noqa: F401,E501


class DestinyHistoricalStatsDestinyAggregateActivityStats(object):
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
        'activity_hash': 'int',
        'values': 'dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'values': 'values'
    }

    def __init__(self, activity_hash=None, values=None):  # noqa: E501
        """DestinyHistoricalStatsDestinyAggregateActivityStats - a model defined in Swagger"""  # noqa: E501

        self._activity_hash = None
        self._values = None
        self.discriminator = None

        if activity_hash is not None:
            self.activity_hash = activity_hash
        if values is not None:
            self.values = values

    @property
    def activity_hash(self):
        """Gets the activity_hash of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501

        Hash ID that can be looked up in the DestinyActivityTable.  # noqa: E501

        :return: The activity_hash of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """Sets the activity_hash of this DestinyHistoricalStatsDestinyAggregateActivityStats.

        Hash ID that can be looked up in the DestinyActivityTable.  # noqa: E501

        :param activity_hash: The activity_hash of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def values(self):
        """Gets the values of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501

        Collection of stats for the player in this activity.  # noqa: E501

        :return: The values of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501
        :rtype: dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DestinyHistoricalStatsDestinyAggregateActivityStats.

        Collection of stats for the player in this activity.  # noqa: E501

        :param values: The values of this DestinyHistoricalStatsDestinyAggregateActivityStats.  # noqa: E501
        :type: dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)
        """

        self._values = values

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
        if not isinstance(other, DestinyHistoricalStatsDestinyAggregateActivityStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
