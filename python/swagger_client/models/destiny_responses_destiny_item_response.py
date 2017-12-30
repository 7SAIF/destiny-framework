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


class DestinyResponsesDestinyItemResponse(object):
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
        'character_id': 'int',
        'item': 'object',
        'instance': 'object',
        'objectives': 'object',
        'perks': 'object',
        'render_data': 'object',
        'stats': 'object',
        'talent_grid': 'object',
        'sockets': 'object'
    }

    attribute_map = {
        'character_id': 'characterId',
        'item': 'item',
        'instance': 'instance',
        'objectives': 'objectives',
        'perks': 'perks',
        'render_data': 'renderData',
        'stats': 'stats',
        'talent_grid': 'talentGrid',
        'sockets': 'sockets'
    }

    def __init__(self, character_id=None, item=None, instance=None, objectives=None, perks=None, render_data=None, stats=None, talent_grid=None, sockets=None):  # noqa: E501
        """DestinyResponsesDestinyItemResponse - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._item = None
        self._instance = None
        self._objectives = None
        self._perks = None
        self._render_data = None
        self._stats = None
        self._talent_grid = None
        self._sockets = None
        self.discriminator = None

        if character_id is not None:
            self.character_id = character_id
        if item is not None:
            self.item = item
        if instance is not None:
            self.instance = instance
        if objectives is not None:
            self.objectives = objectives
        if perks is not None:
            self.perks = perks
        if render_data is not None:
            self.render_data = render_data
        if stats is not None:
            self.stats = stats
        if talent_grid is not None:
            self.talent_grid = talent_grid
        if sockets is not None:
            self.sockets = sockets

    @property
    def character_id(self):
        """Gets the character_id of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        If the item is on a character, this will return the ID of the character that is holding the item.  # noqa: E501

        :return: The character_id of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this DestinyResponsesDestinyItemResponse.

        If the item is on a character, this will return the ID of the character that is holding the item.  # noqa: E501

        :param character_id: The character_id of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def item(self):
        """Gets the item of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Common data for the item relevant to its non-instanced properties.  COMPONENT TYPE: ItemCommonData  # noqa: E501

        :return: The item of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this DestinyResponsesDestinyItemResponse.

        Common data for the item relevant to its non-instanced properties.  COMPONENT TYPE: ItemCommonData  # noqa: E501

        :param item: The item of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._item = item

    @property
    def instance(self):
        """Gets the instance of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Basic instance data for the item.  COMPONENT TYPE: ItemInstances  # noqa: E501

        :return: The instance of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this DestinyResponsesDestinyItemResponse.

        Basic instance data for the item.  COMPONENT TYPE: ItemInstances  # noqa: E501

        :param instance: The instance of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._instance = instance

    @property
    def objectives(self):
        """Gets the objectives of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information specifically about the item's objectives.  COMPONENT TYPE: ItemObjectives  # noqa: E501

        :return: The objectives of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives):
        """Sets the objectives of this DestinyResponsesDestinyItemResponse.

        Information specifically about the item's objectives.  COMPONENT TYPE: ItemObjectives  # noqa: E501

        :param objectives: The objectives of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._objectives = objectives

    @property
    def perks(self):
        """Gets the perks of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information specifically about the perks currently active on the item.  COMPONENT TYPE: ItemPerks  # noqa: E501

        :return: The perks of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._perks

    @perks.setter
    def perks(self, perks):
        """Sets the perks of this DestinyResponsesDestinyItemResponse.

        Information specifically about the perks currently active on the item.  COMPONENT TYPE: ItemPerks  # noqa: E501

        :param perks: The perks of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._perks = perks

    @property
    def render_data(self):
        """Gets the render_data of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information about how to render the item in 3D.  COMPONENT TYPE: ItemRenderData  # noqa: E501

        :return: The render_data of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._render_data

    @render_data.setter
    def render_data(self, render_data):
        """Sets the render_data of this DestinyResponsesDestinyItemResponse.

        Information about how to render the item in 3D.  COMPONENT TYPE: ItemRenderData  # noqa: E501

        :param render_data: The render_data of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._render_data = render_data

    @property
    def stats(self):
        """Gets the stats of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information about the computed stats of the item: power, defense, etc...  COMPONENT TYPE: ItemStats  # noqa: E501

        :return: The stats of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this DestinyResponsesDestinyItemResponse.

        Information about the computed stats of the item: power, defense, etc...  COMPONENT TYPE: ItemStats  # noqa: E501

        :param stats: The stats of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._stats = stats

    @property
    def talent_grid(self):
        """Gets the talent_grid of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's \"Builds\".  COMPONENT TYPE: ItemTalentGrids  # noqa: E501

        :return: The talent_grid of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._talent_grid

    @talent_grid.setter
    def talent_grid(self, talent_grid):
        """Sets the talent_grid of this DestinyResponsesDestinyItemResponse.

        Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's \"Builds\".  COMPONENT TYPE: ItemTalentGrids  # noqa: E501

        :param talent_grid: The talent_grid of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._talent_grid = talent_grid

    @property
    def sockets(self):
        """Gets the sockets of this DestinyResponsesDestinyItemResponse.  # noqa: E501

        Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them.  COMPONENT TYPE: ItemSockets  # noqa: E501

        :return: The sockets of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this DestinyResponsesDestinyItemResponse.

        Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them.  COMPONENT TYPE: ItemSockets  # noqa: E501

        :param sockets: The sockets of this DestinyResponsesDestinyItemResponse.  # noqa: E501
        :type: object
        """

        self._sockets = sockets

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
        if not isinstance(other, DestinyResponsesDestinyItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
