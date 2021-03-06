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

from swagger_client.models.destiny_historical_stats_destiny_aggregate_activity_stats import DestinyHistoricalStatsDestinyAggregateActivityStats  # noqa: F401,E501


class DestinyHistoricalStatsDestinyAggregateActivityResults(object):
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
        'activities': 'list[DestinyHistoricalStatsDestinyAggregateActivityStats]'
    }

    attribute_map = {
        'activities': 'activities'
    }

    def __init__(self, activities=None):  # noqa: E501
        """DestinyHistoricalStatsDestinyAggregateActivityResults - a model defined in Swagger"""  # noqa: E501

        self._activities = None
        self.discriminator = None

        if activities is not None:
            self.activities = activities

    @property
    def activities(self):
        """Gets the activities of this DestinyHistoricalStatsDestinyAggregateActivityResults.  # noqa: E501

        List of all activities the player has participated in.  # noqa: E501

        :return: The activities of this DestinyHistoricalStatsDestinyAggregateActivityResults.  # noqa: E501
        :rtype: list[DestinyHistoricalStatsDestinyAggregateActivityStats]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this DestinyHistoricalStatsDestinyAggregateActivityResults.

        List of all activities the player has participated in.  # noqa: E501

        :param activities: The activities of this DestinyHistoricalStatsDestinyAggregateActivityResults.  # noqa: E501
        :type: list[DestinyHistoricalStatsDestinyAggregateActivityStats]
        """

        self._activities = activities

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
        if not isinstance(other, DestinyHistoricalStatsDestinyAggregateActivityResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
