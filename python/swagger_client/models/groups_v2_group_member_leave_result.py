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

from swagger_client.models.groups_v2_group_v2 import GroupsV2GroupV2  # noqa: F401,E501


class GroupsV2GroupMemberLeaveResult(object):
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
        'group': 'GroupsV2GroupV2',
        'group_deleted': 'bool'
    }

    attribute_map = {
        'group': 'group',
        'group_deleted': 'groupDeleted'
    }

    def __init__(self, group=None, group_deleted=None):  # noqa: E501
        """GroupsV2GroupMemberLeaveResult - a model defined in Swagger"""  # noqa: E501

        self._group = None
        self._group_deleted = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if group_deleted is not None:
            self.group_deleted = group_deleted

    @property
    def group(self):
        """Gets the group of this GroupsV2GroupMemberLeaveResult.  # noqa: E501


        :return: The group of this GroupsV2GroupMemberLeaveResult.  # noqa: E501
        :rtype: GroupsV2GroupV2
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupsV2GroupMemberLeaveResult.


        :param group: The group of this GroupsV2GroupMemberLeaveResult.  # noqa: E501
        :type: GroupsV2GroupV2
        """

        self._group = group

    @property
    def group_deleted(self):
        """Gets the group_deleted of this GroupsV2GroupMemberLeaveResult.  # noqa: E501


        :return: The group_deleted of this GroupsV2GroupMemberLeaveResult.  # noqa: E501
        :rtype: bool
        """
        return self._group_deleted

    @group_deleted.setter
    def group_deleted(self, group_deleted):
        """Sets the group_deleted of this GroupsV2GroupMemberLeaveResult.


        :param group_deleted: The group_deleted of this GroupsV2GroupMemberLeaveResult.  # noqa: E501
        :type: bool
        """

        self._group_deleted = group_deleted

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
        if not isinstance(other, GroupsV2GroupMemberLeaveResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
