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


class DestinyHistoricalStatsDestinyHistoricalWeaponStats(object):
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
        'reference_id': 'int',
        'values': 'dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)'
    }

    attribute_map = {
        'reference_id': 'referenceId',
        'values': 'values'
    }

    def __init__(self, reference_id=None, values=None):
        """
        DestinyHistoricalStatsDestinyHistoricalWeaponStats - a model defined in Swagger
        """

        self._reference_id = None
        self._values = None

        if reference_id is not None:
          self.reference_id = reference_id
        if values is not None:
          self.values = values

    @property
    def reference_id(self):
        """
        Gets the reference_id of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        The hash ID of the item definition that describes the weapon.

        :return: The reference_id of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        :rtype: int
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        The hash ID of the item definition that describes the weapon.

        :param reference_id: The reference_id of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        :type: int
        """

        self._reference_id = reference_id

    @property
    def values(self):
        """
        Gets the values of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        Collection of stats for the period.

        :return: The values of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        :rtype: dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        Collection of stats for the period.

        :param values: The values of this DestinyHistoricalStatsDestinyHistoricalWeaponStats.
        :type: dict(str, DestinyHistoricalStatsDestinyHistoricalStatsValue)
        """

        self._values = values

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
        if not isinstance(other, DestinyHistoricalStatsDestinyHistoricalWeaponStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
