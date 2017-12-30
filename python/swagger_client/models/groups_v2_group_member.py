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

from swagger_client.models.groups_v2_runtime_group_member_type import GroupsV2RuntimeGroupMemberType  # noqa: F401,E501
from swagger_client.models.user_user_info_card import UserUserInfoCard  # noqa: F401,E501


class GroupsV2GroupMember(object):
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
        'member_type': 'GroupsV2RuntimeGroupMemberType',
        'is_online': 'bool',
        'group_id': 'int',
        'destiny_user_info': 'UserUserInfoCard',
        'bungie_net_user_info': 'UserUserInfoCard',
        'join_date': 'datetime'
    }

    attribute_map = {
        'member_type': 'memberType',
        'is_online': 'isOnline',
        'group_id': 'groupId',
        'destiny_user_info': 'destinyUserInfo',
        'bungie_net_user_info': 'bungieNetUserInfo',
        'join_date': 'joinDate'
    }

    def __init__(self, member_type=None, is_online=None, group_id=None, destiny_user_info=None, bungie_net_user_info=None, join_date=None):  # noqa: E501
        """GroupsV2GroupMember - a model defined in Swagger"""  # noqa: E501

        self._member_type = None
        self._is_online = None
        self._group_id = None
        self._destiny_user_info = None
        self._bungie_net_user_info = None
        self._join_date = None
        self.discriminator = None

        if member_type is not None:
            self.member_type = member_type
        if is_online is not None:
            self.is_online = is_online
        if group_id is not None:
            self.group_id = group_id
        if destiny_user_info is not None:
            self.destiny_user_info = destiny_user_info
        if bungie_net_user_info is not None:
            self.bungie_net_user_info = bungie_net_user_info
        if join_date is not None:
            self.join_date = join_date

    @property
    def member_type(self):
        """Gets the member_type of this GroupsV2GroupMember.  # noqa: E501


        :return: The member_type of this GroupsV2GroupMember.  # noqa: E501
        :rtype: GroupsV2RuntimeGroupMemberType
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this GroupsV2GroupMember.


        :param member_type: The member_type of this GroupsV2GroupMember.  # noqa: E501
        :type: GroupsV2RuntimeGroupMemberType
        """

        self._member_type = member_type

    @property
    def is_online(self):
        """Gets the is_online of this GroupsV2GroupMember.  # noqa: E501


        :return: The is_online of this GroupsV2GroupMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_online

    @is_online.setter
    def is_online(self, is_online):
        """Sets the is_online of this GroupsV2GroupMember.


        :param is_online: The is_online of this GroupsV2GroupMember.  # noqa: E501
        :type: bool
        """

        self._is_online = is_online

    @property
    def group_id(self):
        """Gets the group_id of this GroupsV2GroupMember.  # noqa: E501


        :return: The group_id of this GroupsV2GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupsV2GroupMember.


        :param group_id: The group_id of this GroupsV2GroupMember.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def destiny_user_info(self):
        """Gets the destiny_user_info of this GroupsV2GroupMember.  # noqa: E501


        :return: The destiny_user_info of this GroupsV2GroupMember.  # noqa: E501
        :rtype: UserUserInfoCard
        """
        return self._destiny_user_info

    @destiny_user_info.setter
    def destiny_user_info(self, destiny_user_info):
        """Sets the destiny_user_info of this GroupsV2GroupMember.


        :param destiny_user_info: The destiny_user_info of this GroupsV2GroupMember.  # noqa: E501
        :type: UserUserInfoCard
        """

        self._destiny_user_info = destiny_user_info

    @property
    def bungie_net_user_info(self):
        """Gets the bungie_net_user_info of this GroupsV2GroupMember.  # noqa: E501


        :return: The bungie_net_user_info of this GroupsV2GroupMember.  # noqa: E501
        :rtype: UserUserInfoCard
        """
        return self._bungie_net_user_info

    @bungie_net_user_info.setter
    def bungie_net_user_info(self, bungie_net_user_info):
        """Sets the bungie_net_user_info of this GroupsV2GroupMember.


        :param bungie_net_user_info: The bungie_net_user_info of this GroupsV2GroupMember.  # noqa: E501
        :type: UserUserInfoCard
        """

        self._bungie_net_user_info = bungie_net_user_info

    @property
    def join_date(self):
        """Gets the join_date of this GroupsV2GroupMember.  # noqa: E501


        :return: The join_date of this GroupsV2GroupMember.  # noqa: E501
        :rtype: datetime
        """
        return self._join_date

    @join_date.setter
    def join_date(self, join_date):
        """Sets the join_date of this GroupsV2GroupMember.


        :param join_date: The join_date of this GroupsV2GroupMember.  # noqa: E501
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
        if not isinstance(other, GroupsV2GroupMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
