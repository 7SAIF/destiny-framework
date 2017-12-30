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


class DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition(object):
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
        'plug_item_hash': 'int',
        'socket_type_hash': 'int'
    }

    attribute_map = {
        'plug_item_hash': 'plugItemHash',
        'socket_type_hash': 'socketTypeHash'
    }

    def __init__(self, plug_item_hash=None, socket_type_hash=None):  # noqa: E501
        """DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition - a model defined in Swagger"""  # noqa: E501

        self._plug_item_hash = None
        self._socket_type_hash = None
        self.discriminator = None

        if plug_item_hash is not None:
            self.plug_item_hash = plug_item_hash
        if socket_type_hash is not None:
            self.socket_type_hash = socket_type_hash

    @property
    def plug_item_hash(self):
        """Gets the plug_item_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501

        Indicates the plug that is intrinsically inserted into this socket.  # noqa: E501

        :return: The plug_item_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._plug_item_hash

    @plug_item_hash.setter
    def plug_item_hash(self, plug_item_hash):
        """Sets the plug_item_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.

        Indicates the plug that is intrinsically inserted into this socket.  # noqa: E501

        :param plug_item_hash: The plug_item_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501
        :type: int
        """

        self._plug_item_hash = plug_item_hash

    @property
    def socket_type_hash(self):
        """Gets the socket_type_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501

        Indicates the type of this intrinsic socket.  # noqa: E501

        :return: The socket_type_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._socket_type_hash

    @socket_type_hash.setter
    def socket_type_hash(self, socket_type_hash):
        """Sets the socket_type_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.

        Indicates the type of this intrinsic socket.  # noqa: E501

        :param socket_type_hash: The socket_type_hash of this DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition.  # noqa: E501
        :type: int
        """

        self._socket_type_hash = socket_type_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other