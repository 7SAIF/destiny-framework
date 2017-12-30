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


class DestinyHistoricalStatsDestinyClanAggregateStat(object):
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
        'mode': 'object',
        'stat_id': 'str',
        'value': 'object'
    }

    attribute_map = {
        'mode': 'mode',
        'stat_id': 'statId',
        'value': 'value'
    }

    def __init__(self, mode=None, stat_id=None, value=None):  # noqa: E501
        """DestinyHistoricalStatsDestinyClanAggregateStat - a model defined in Swagger"""  # noqa: E501

        self._mode = None
        self._stat_id = None
        self._value = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if stat_id is not None:
            self.stat_id = stat_id
        if value is not None:
            self.value = value

    @property
    def mode(self):
        """Gets the mode of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501

        The id of the mode of stats (allPvp, allPvE, etc)  # noqa: E501

        :return: The mode of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :rtype: object
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DestinyHistoricalStatsDestinyClanAggregateStat.

        The id of the mode of stats (allPvp, allPvE, etc)  # noqa: E501

        :param mode: The mode of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :type: object
        """

        self._mode = mode

    @property
    def stat_id(self):
        """Gets the stat_id of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501

        The id of the stat  # noqa: E501

        :return: The stat_id of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :rtype: str
        """
        return self._stat_id

    @stat_id.setter
    def stat_id(self, stat_id):
        """Sets the stat_id of this DestinyHistoricalStatsDestinyClanAggregateStat.

        The id of the stat  # noqa: E501

        :param stat_id: The stat_id of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :type: str
        """

        self._stat_id = stat_id

    @property
    def value(self):
        """Gets the value of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501

        Value of the stat for this player  # noqa: E501

        :return: The value of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DestinyHistoricalStatsDestinyClanAggregateStat.

        Value of the stat for this player  # noqa: E501

        :param value: The value of this DestinyHistoricalStatsDestinyClanAggregateStat.  # noqa: E501
        :type: object
        """

        self._value = value

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
        if not isinstance(other, DestinyHistoricalStatsDestinyClanAggregateStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
