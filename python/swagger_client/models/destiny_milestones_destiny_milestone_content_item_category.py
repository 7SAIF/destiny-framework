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


class DestinyMilestonesDestinyMilestoneContentItemCategory(object):
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
        'title': 'str',
        'item_hashes': 'list[int]'
    }

    attribute_map = {
        'title': 'title',
        'item_hashes': 'itemHashes'
    }

    def __init__(self, title=None, item_hashes=None):
        """
        DestinyMilestonesDestinyMilestoneContentItemCategory - a model defined in Swagger
        """

        self._title = None
        self._item_hashes = None

        if title is not None:
          self.title = title
        if item_hashes is not None:
          self.item_hashes = item_hashes

    @property
    def title(self):
        """
        Gets the title of this DestinyMilestonesDestinyMilestoneContentItemCategory.

        :return: The title of this DestinyMilestonesDestinyMilestoneContentItemCategory.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DestinyMilestonesDestinyMilestoneContentItemCategory.

        :param title: The title of this DestinyMilestonesDestinyMilestoneContentItemCategory.
        :type: str
        """

        self._title = title

    @property
    def item_hashes(self):
        """
        Gets the item_hashes of this DestinyMilestonesDestinyMilestoneContentItemCategory.

        :return: The item_hashes of this DestinyMilestonesDestinyMilestoneContentItemCategory.
        :rtype: list[int]
        """
        return self._item_hashes

    @item_hashes.setter
    def item_hashes(self, item_hashes):
        """
        Sets the item_hashes of this DestinyMilestonesDestinyMilestoneContentItemCategory.

        :param item_hashes: The item_hashes of this DestinyMilestonesDestinyMilestoneContentItemCategory.
        :type: list[int]
        """

        self._item_hashes = item_hashes

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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneContentItemCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
