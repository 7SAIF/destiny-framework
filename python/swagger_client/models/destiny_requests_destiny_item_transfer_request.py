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

from swagger_client.models.bungie_membership_type import BungieMembershipType  # noqa: F401,E501


class DestinyRequestsDestinyItemTransferRequest(object):
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
        'item_reference_hash': 'int',
        'stack_size': 'int',
        'transfer_to_vault': 'bool',
        'item_id': 'int',
        'character_id': 'int',
        'membership_type': 'BungieMembershipType'
    }

    attribute_map = {
        'item_reference_hash': 'itemReferenceHash',
        'stack_size': 'stackSize',
        'transfer_to_vault': 'transferToVault',
        'item_id': 'itemId',
        'character_id': 'characterId',
        'membership_type': 'membershipType'
    }

    def __init__(self, item_reference_hash=None, stack_size=None, transfer_to_vault=None, item_id=None, character_id=None, membership_type=None):  # noqa: E501
        """DestinyRequestsDestinyItemTransferRequest - a model defined in Swagger"""  # noqa: E501

        self._item_reference_hash = None
        self._stack_size = None
        self._transfer_to_vault = None
        self._item_id = None
        self._character_id = None
        self._membership_type = None
        self.discriminator = None

        if item_reference_hash is not None:
            self.item_reference_hash = item_reference_hash
        if stack_size is not None:
            self.stack_size = stack_size
        if transfer_to_vault is not None:
            self.transfer_to_vault = transfer_to_vault
        if item_id is not None:
            self.item_id = item_id
        if character_id is not None:
            self.character_id = character_id
        if membership_type is not None:
            self.membership_type = membership_type

    @property
    def item_reference_hash(self):
        """Gets the item_reference_hash of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The item_reference_hash of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_reference_hash

    @item_reference_hash.setter
    def item_reference_hash(self, item_reference_hash):
        """Sets the item_reference_hash of this DestinyRequestsDestinyItemTransferRequest.


        :param item_reference_hash: The item_reference_hash of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: int
        """

        self._item_reference_hash = item_reference_hash

    @property
    def stack_size(self):
        """Gets the stack_size of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The stack_size of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: int
        """
        return self._stack_size

    @stack_size.setter
    def stack_size(self, stack_size):
        """Sets the stack_size of this DestinyRequestsDestinyItemTransferRequest.


        :param stack_size: The stack_size of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: int
        """

        self._stack_size = stack_size

    @property
    def transfer_to_vault(self):
        """Gets the transfer_to_vault of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The transfer_to_vault of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: bool
        """
        return self._transfer_to_vault

    @transfer_to_vault.setter
    def transfer_to_vault(self, transfer_to_vault):
        """Sets the transfer_to_vault of this DestinyRequestsDestinyItemTransferRequest.


        :param transfer_to_vault: The transfer_to_vault of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: bool
        """

        self._transfer_to_vault = transfer_to_vault

    @property
    def item_id(self):
        """Gets the item_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The item_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this DestinyRequestsDestinyItemTransferRequest.


        :param item_id: The item_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def character_id(self):
        """Gets the character_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The character_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this DestinyRequestsDestinyItemTransferRequest.


        :param character_id: The character_id of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def membership_type(self):
        """Gets the membership_type of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501


        :return: The membership_type of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :rtype: BungieMembershipType
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """Sets the membership_type of this DestinyRequestsDestinyItemTransferRequest.


        :param membership_type: The membership_type of this DestinyRequestsDestinyItemTransferRequest.  # noqa: E501
        :type: BungieMembershipType
        """

        self._membership_type = membership_type

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
        if not isinstance(other, DestinyRequestsDestinyItemTransferRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
