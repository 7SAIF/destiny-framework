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

from swagger_client.models.groups_v2_group_potential_member_status import GroupsV2GroupPotentialMemberStatus  # noqa: F401,E501
from swagger_client.models.user_user_info_card import UserUserInfoCard  # noqa: F401,E501


class GroupsV2GroupPotentialMember(object):
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
        'potential_status': 'GroupsV2GroupPotentialMemberStatus',
        'group_id': 'int',
        'destiny_user_info': 'UserUserInfoCard',
        'bungie_net_user_info': 'UserUserInfoCard',
        'join_date': 'datetime'
    }

    attribute_map = {
        'potential_status': 'potentialStatus',
        'group_id': 'groupId',
        'destiny_user_info': 'destinyUserInfo',
        'bungie_net_user_info': 'bungieNetUserInfo',
        'join_date': 'joinDate'
    }

    def __init__(self, potential_status=None, group_id=None, destiny_user_info=None, bungie_net_user_info=None, join_date=None):  # noqa: E501
        """GroupsV2GroupPotentialMember - a model defined in Swagger"""  # noqa: E501

        self._potential_status = None
        self._group_id = None
        self._destiny_user_info = None
        self._bungie_net_user_info = None
        self._join_date = None
        self.discriminator = None

        if potential_status is not None:
            self.potential_status = potential_status
        if group_id is not None:
            self.group_id = group_id
        if destiny_user_info is not None:
            self.destiny_user_info = destiny_user_info
        if bungie_net_user_info is not None:
            self.bungie_net_user_info = bungie_net_user_info
        if join_date is not None:
            self.join_date = join_date

    @property
    def potential_status(self):
        """Gets the potential_status of this GroupsV2GroupPotentialMember.  # noqa: E501


        :return: The potential_status of this GroupsV2GroupPotentialMember.  # noqa: E501
        :rtype: GroupsV2GroupPotentialMemberStatus
        """
        return self._potential_status

    @potential_status.setter
    def potential_status(self, potential_status):
        """Sets the potential_status of this GroupsV2GroupPotentialMember.


        :param potential_status: The potential_status of this GroupsV2GroupPotentialMember.  # noqa: E501
        :type: GroupsV2GroupPotentialMemberStatus
        """

        self._potential_status = potential_status

    @property
    def group_id(self):
        """Gets the group_id of this GroupsV2GroupPotentialMember.  # noqa: E501


        :return: The group_id of this GroupsV2GroupPotentialMember.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupsV2GroupPotentialMember.


        :param group_id: The group_id of this GroupsV2GroupPotentialMember.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def destiny_user_info(self):
        """Gets the destiny_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501


        :return: The destiny_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501
        :rtype: UserUserInfoCard
        """
        return self._destiny_user_info

    @destiny_user_info.setter
    def destiny_user_info(self, destiny_user_info):
        """Sets the destiny_user_info of this GroupsV2GroupPotentialMember.


        :param destiny_user_info: The destiny_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501
        :type: UserUserInfoCard
        """

        self._destiny_user_info = destiny_user_info

    @property
    def bungie_net_user_info(self):
        """Gets the bungie_net_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501


        :return: The bungie_net_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501
        :rtype: UserUserInfoCard
        """
        return self._bungie_net_user_info

    @bungie_net_user_info.setter
    def bungie_net_user_info(self, bungie_net_user_info):
        """Sets the bungie_net_user_info of this GroupsV2GroupPotentialMember.


        :param bungie_net_user_info: The bungie_net_user_info of this GroupsV2GroupPotentialMember.  # noqa: E501
        :type: UserUserInfoCard
        """

        self._bungie_net_user_info = bungie_net_user_info

    @property
    def join_date(self):
        """Gets the join_date of this GroupsV2GroupPotentialMember.  # noqa: E501


        :return: The join_date of this GroupsV2GroupPotentialMember.  # noqa: E501
        :rtype: datetime
        """
        return self._join_date

    @join_date.setter
    def join_date(self, join_date):
        """Sets the join_date of this GroupsV2GroupPotentialMember.


        :param join_date: The join_date of this GroupsV2GroupPotentialMember.  # noqa: E501
        :type: datetime
        """

        self._join_date = join_date

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
        if not isinstance(other, GroupsV2GroupPotentialMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
