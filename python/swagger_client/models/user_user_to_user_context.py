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

from swagger_client.models.ignores_ignore_response import IgnoresIgnoreResponse  # noqa: F401,E501


class UserUserToUserContext(object):
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
        'is_following': 'bool',
        'ignore_status': 'IgnoresIgnoreResponse',
        'global_ignore_end_date': 'datetime'
    }

    attribute_map = {
        'is_following': 'isFollowing',
        'ignore_status': 'ignoreStatus',
        'global_ignore_end_date': 'globalIgnoreEndDate'
    }

    def __init__(self, is_following=None, ignore_status=None, global_ignore_end_date=None):  # noqa: E501
        """UserUserToUserContext - a model defined in Swagger"""  # noqa: E501

        self._is_following = None
        self._ignore_status = None
        self._global_ignore_end_date = None
        self.discriminator = None

        if is_following is not None:
            self.is_following = is_following
        if ignore_status is not None:
            self.ignore_status = ignore_status
        if global_ignore_end_date is not None:
            self.global_ignore_end_date = global_ignore_end_date

    @property
    def is_following(self):
        """Gets the is_following of this UserUserToUserContext.  # noqa: E501


        :return: The is_following of this UserUserToUserContext.  # noqa: E501
        :rtype: bool
        """
        return self._is_following

    @is_following.setter
    def is_following(self, is_following):
        """Sets the is_following of this UserUserToUserContext.


        :param is_following: The is_following of this UserUserToUserContext.  # noqa: E501
        :type: bool
        """

        self._is_following = is_following

    @property
    def ignore_status(self):
        """Gets the ignore_status of this UserUserToUserContext.  # noqa: E501


        :return: The ignore_status of this UserUserToUserContext.  # noqa: E501
        :rtype: IgnoresIgnoreResponse
        """
        return self._ignore_status

    @ignore_status.setter
    def ignore_status(self, ignore_status):
        """Sets the ignore_status of this UserUserToUserContext.


        :param ignore_status: The ignore_status of this UserUserToUserContext.  # noqa: E501
        :type: IgnoresIgnoreResponse
        """

        self._ignore_status = ignore_status

    @property
    def global_ignore_end_date(self):
        """Gets the global_ignore_end_date of this UserUserToUserContext.  # noqa: E501


        :return: The global_ignore_end_date of this UserUserToUserContext.  # noqa: E501
        :rtype: datetime
        """
        return self._global_ignore_end_date

    @global_ignore_end_date.setter
    def global_ignore_end_date(self, global_ignore_end_date):
        """Sets the global_ignore_end_date of this UserUserToUserContext.


        :param global_ignore_end_date: The global_ignore_end_date of this UserUserToUserContext.  # noqa: E501
        :type: datetime
        """

        self._global_ignore_end_date = global_ignore_end_date

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
        if not isinstance(other, UserUserToUserContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
