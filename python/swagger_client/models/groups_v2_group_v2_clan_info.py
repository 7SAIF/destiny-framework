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


class GroupsV2GroupV2ClanInfo(object):
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
        'clan_callsign': 'str',
        'clan_banner_data': 'GroupsV2ClanBanner'
    }

    attribute_map = {
        'clan_callsign': 'clanCallsign',
        'clan_banner_data': 'clanBannerData'
    }

    def __init__(self, clan_callsign=None, clan_banner_data=None):
        """
        GroupsV2GroupV2ClanInfo - a model defined in Swagger
        """

        self._clan_callsign = None
        self._clan_banner_data = None

        if clan_callsign is not None:
          self.clan_callsign = clan_callsign
        if clan_banner_data is not None:
          self.clan_banner_data = clan_banner_data

    @property
    def clan_callsign(self):
        """
        Gets the clan_callsign of this GroupsV2GroupV2ClanInfo.

        :return: The clan_callsign of this GroupsV2GroupV2ClanInfo.
        :rtype: str
        """
        return self._clan_callsign

    @clan_callsign.setter
    def clan_callsign(self, clan_callsign):
        """
        Sets the clan_callsign of this GroupsV2GroupV2ClanInfo.

        :param clan_callsign: The clan_callsign of this GroupsV2GroupV2ClanInfo.
        :type: str
        """

        self._clan_callsign = clan_callsign

    @property
    def clan_banner_data(self):
        """
        Gets the clan_banner_data of this GroupsV2GroupV2ClanInfo.

        :return: The clan_banner_data of this GroupsV2GroupV2ClanInfo.
        :rtype: GroupsV2ClanBanner
        """
        return self._clan_banner_data

    @clan_banner_data.setter
    def clan_banner_data(self, clan_banner_data):
        """
        Sets the clan_banner_data of this GroupsV2GroupV2ClanInfo.

        :param clan_banner_data: The clan_banner_data of this GroupsV2GroupV2ClanInfo.
        :type: GroupsV2ClanBanner
        """

        self._clan_banner_data = clan_banner_data

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
        if not isinstance(other, GroupsV2GroupV2ClanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
