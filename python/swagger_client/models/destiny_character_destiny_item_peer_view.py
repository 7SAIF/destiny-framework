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


class DestinyCharacterDestinyItemPeerView(object):
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
        'item_hash': 'int',
        'dyes': 'list[DestinyDyeReference]'
    }

    attribute_map = {
        'item_hash': 'itemHash',
        'dyes': 'dyes'
    }

    def __init__(self, item_hash=None, dyes=None):
        """
        DestinyCharacterDestinyItemPeerView - a model defined in Swagger
        """

        self._item_hash = None
        self._dyes = None

        if item_hash is not None:
          self.item_hash = item_hash
        if dyes is not None:
          self.dyes = dyes

    @property
    def item_hash(self):
        """
        Gets the item_hash of this DestinyCharacterDestinyItemPeerView.
        The hash identifier of the item in question.  Use it to look up the DestinyInventoryItemDefinition of the item  for static rendering data.

        :return: The item_hash of this DestinyCharacterDestinyItemPeerView.
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """
        Sets the item_hash of this DestinyCharacterDestinyItemPeerView.
        The hash identifier of the item in question.  Use it to look up the DestinyInventoryItemDefinition of the item  for static rendering data.

        :param item_hash: The item_hash of this DestinyCharacterDestinyItemPeerView.
        :type: int
        """

        self._item_hash = item_hash

    @property
    def dyes(self):
        """
        Gets the dyes of this DestinyCharacterDestinyItemPeerView.
        The list of dyes that have been applied to this item.

        :return: The dyes of this DestinyCharacterDestinyItemPeerView.
        :rtype: list[DestinyDyeReference]
        """
        return self._dyes

    @dyes.setter
    def dyes(self, dyes):
        """
        Sets the dyes of this DestinyCharacterDestinyItemPeerView.
        The list of dyes that have been applied to this item.

        :param dyes: The dyes of this DestinyCharacterDestinyItemPeerView.
        :type: list[DestinyDyeReference]
        """

        self._dyes = dyes

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
        if not isinstance(other, DestinyCharacterDestinyItemPeerView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
