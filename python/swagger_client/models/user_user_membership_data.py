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


class UserUserMembershipData(object):
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
        'destiny_memberships': 'list[UserUserInfoCard]',
        'bungie_net_user': 'UserGeneralUser'
    }

    attribute_map = {
        'destiny_memberships': 'destinyMemberships',
        'bungie_net_user': 'bungieNetUser'
    }

    def __init__(self, destiny_memberships=None, bungie_net_user=None):
        """
        UserUserMembershipData - a model defined in Swagger
        """

        self._destiny_memberships = None
        self._bungie_net_user = None

        if destiny_memberships is not None:
          self.destiny_memberships = destiny_memberships
        if bungie_net_user is not None:
          self.bungie_net_user = bungie_net_user

    @property
    def destiny_memberships(self):
        """
        Gets the destiny_memberships of this UserUserMembershipData.
        this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)

        :return: The destiny_memberships of this UserUserMembershipData.
        :rtype: list[UserUserInfoCard]
        """
        return self._destiny_memberships

    @destiny_memberships.setter
    def destiny_memberships(self, destiny_memberships):
        """
        Sets the destiny_memberships of this UserUserMembershipData.
        this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)

        :param destiny_memberships: The destiny_memberships of this UserUserMembershipData.
        :type: list[UserUserInfoCard]
        """

        self._destiny_memberships = destiny_memberships

    @property
    def bungie_net_user(self):
        """
        Gets the bungie_net_user of this UserUserMembershipData.

        :return: The bungie_net_user of this UserUserMembershipData.
        :rtype: UserGeneralUser
        """
        return self._bungie_net_user

    @bungie_net_user.setter
    def bungie_net_user(self, bungie_net_user):
        """
        Sets the bungie_net_user of this UserUserMembershipData.

        :param bungie_net_user: The bungie_net_user of this UserUserMembershipData.
        :type: UserGeneralUser
        """

        self._bungie_net_user = bungie_net_user

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
        if not isinstance(other, UserUserMembershipData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
