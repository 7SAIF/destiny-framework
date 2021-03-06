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


class DestinyEntitiesItemsDestinyItemComponent(object):
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
        'item_hash': 'int',
        'item_instance_id': 'int',
        'quantity': 'int',
        'bind_status': 'object',
        'location': 'object',
        'bucket_hash': 'int',
        'transfer_status': 'object',
        'lockable': 'bool',
        'state': 'object'
    }

    attribute_map = {
        'item_hash': 'itemHash',
        'item_instance_id': 'itemInstanceId',
        'quantity': 'quantity',
        'bind_status': 'bindStatus',
        'location': 'location',
        'bucket_hash': 'bucketHash',
        'transfer_status': 'transferStatus',
        'lockable': 'lockable',
        'state': 'state'
    }

    def __init__(self, item_hash=None, item_instance_id=None, quantity=None, bind_status=None, location=None, bucket_hash=None, transfer_status=None, lockable=None, state=None):  # noqa: E501
        """DestinyEntitiesItemsDestinyItemComponent - a model defined in Swagger"""  # noqa: E501

        self._item_hash = None
        self._item_instance_id = None
        self._quantity = None
        self._bind_status = None
        self._location = None
        self._bucket_hash = None
        self._transfer_status = None
        self._lockable = None
        self._state = None
        self.discriminator = None

        if item_hash is not None:
            self.item_hash = item_hash
        if item_instance_id is not None:
            self.item_instance_id = item_instance_id
        if quantity is not None:
            self.quantity = quantity
        if bind_status is not None:
            self.bind_status = bind_status
        if location is not None:
            self.location = location
        if bucket_hash is not None:
            self.bucket_hash = bucket_hash
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if lockable is not None:
            self.lockable = lockable
        if state is not None:
            self.state = state

    @property
    def item_hash(self):
        """Gets the item_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        The identifier for the item's definition, which is where most of the useful static information for the item can be found.  # noqa: E501

        :return: The item_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """Sets the item_hash of this DestinyEntitiesItemsDestinyItemComponent.

        The identifier for the item's definition, which is where most of the useful static information for the item can be found.  # noqa: E501

        :param item_hash: The item_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: int
        """

        self._item_hash = item_hash

    @property
    def item_instance_id(self):
        """Gets the item_instance_id of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.  # noqa: E501

        :return: The item_instance_id of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: int
        """
        return self._item_instance_id

    @item_instance_id.setter
    def item_instance_id(self, item_instance_id):
        """Sets the item_instance_id of this DestinyEntitiesItemsDestinyItemComponent.

        If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.  # noqa: E501

        :param item_instance_id: The item_instance_id of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: int
        """

        self._item_instance_id = item_instance_id

    @property
    def quantity(self):
        """Gets the quantity of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it)  # noqa: E501

        :return: The quantity of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DestinyEntitiesItemsDestinyItemComponent.

        The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it)  # noqa: E501

        :param quantity: The quantity of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def bind_status(self):
        """Gets the bind_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        If the item is bound to a location, it will be specified in this enum.  # noqa: E501

        :return: The bind_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: object
        """
        return self._bind_status

    @bind_status.setter
    def bind_status(self, bind_status):
        """Sets the bind_status of this DestinyEntitiesItemsDestinyItemComponent.

        If the item is bound to a location, it will be specified in this enum.  # noqa: E501

        :param bind_status: The bind_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: object
        """

        self._bind_status = bind_status

    @property
    def location(self):
        """Gets the location of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items.  # noqa: E501

        :return: The location of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DestinyEntitiesItemsDestinyItemComponent.

        An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items.  # noqa: E501

        :param location: The location of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: object
        """

        self._location = location

    @property
    def bucket_hash(self):
        """Gets the bucket_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        The hash identifier for the specific inventory bucket in which the item is located.  # noqa: E501

        :return: The bucket_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: int
        """
        return self._bucket_hash

    @bucket_hash.setter
    def bucket_hash(self, bucket_hash):
        """Sets the bucket_hash of this DestinyEntitiesItemsDestinyItemComponent.

        The hash identifier for the specific inventory bucket in which the item is located.  # noqa: E501

        :param bucket_hash: The bucket_hash of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: int
        """

        self._bucket_hash = bucket_hash

    @property
    def transfer_status(self):
        """Gets the transfer_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).  # noqa: E501

        :return: The transfer_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: object
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this DestinyEntitiesItemsDestinyItemComponent.

        If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).  # noqa: E501

        :param transfer_status: The transfer_status of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: object
        """

        self._transfer_status = transfer_status

    @property
    def lockable(self):
        """Gets the lockable of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        If the item can be locked, this will indicate that state.  # noqa: E501

        :return: The lockable of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: bool
        """
        return self._lockable

    @lockable.setter
    def lockable(self, lockable):
        """Sets the lockable of this DestinyEntitiesItemsDestinyItemComponent.

        If the item can be locked, this will indicate that state.  # noqa: E501

        :param lockable: The lockable of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: bool
        """

        self._lockable = lockable

    @property
    def state(self):
        """Gets the state of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501

        A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted.  # noqa: E501

        :return: The state of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :rtype: object
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DestinyEntitiesItemsDestinyItemComponent.

        A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted.  # noqa: E501

        :param state: The state of this DestinyEntitiesItemsDestinyItemComponent.  # noqa: E501
        :type: object
        """

        self._state = state

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
        if not isinstance(other, DestinyEntitiesItemsDestinyItemComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
