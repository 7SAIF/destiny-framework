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


class DestinyResponsesDestinyCharacterResponse(object):
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
        'inventory': 'object',
        'character': 'object',
        'progressions': 'object',
        'render_data': 'object',
        'activities': 'object',
        'equipment': 'object',
        'kiosks': 'object',
        'item_components': 'object'
    }

    attribute_map = {
        'inventory': 'inventory',
        'character': 'character',
        'progressions': 'progressions',
        'render_data': 'renderData',
        'activities': 'activities',
        'equipment': 'equipment',
        'kiosks': 'kiosks',
        'item_components': 'itemComponents'
    }

    def __init__(self, inventory=None, character=None, progressions=None, render_data=None, activities=None, equipment=None, kiosks=None, item_components=None):  # noqa: E501
        """DestinyResponsesDestinyCharacterResponse - a model defined in Swagger"""  # noqa: E501

        self._inventory = None
        self._character = None
        self._progressions = None
        self._render_data = None
        self._activities = None
        self._equipment = None
        self._kiosks = None
        self._item_components = None
        self.discriminator = None

        if inventory is not None:
            self.inventory = inventory
        if character is not None:
            self.character = character
        if progressions is not None:
            self.progressions = progressions
        if render_data is not None:
            self.render_data = render_data
        if activities is not None:
            self.activities = activities
        if equipment is not None:
            self.equipment = equipment
        if kiosks is not None:
            self.kiosks = kiosks
        if item_components is not None:
            self.item_components = item_components

    @property
    def inventory(self):
        """Gets the inventory of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        The character-level non-equipped inventory items.  COMPONENT TYPE: CharacterInventories  # noqa: E501

        :return: The inventory of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this DestinyResponsesDestinyCharacterResponse.

        The character-level non-equipped inventory items.  COMPONENT TYPE: CharacterInventories  # noqa: E501

        :param inventory: The inventory of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._inventory = inventory

    @property
    def character(self):
        """Gets the character of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Base information about the character in question.  COMPONENT TYPE: Characters  # noqa: E501

        :return: The character of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this DestinyResponsesDestinyCharacterResponse.

        Base information about the character in question.  COMPONENT TYPE: Characters  # noqa: E501

        :param character: The character of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._character = character

    @property
    def progressions(self):
        """Gets the progressions of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Character progression data, including Milestones.  COMPONENT TYPE: CharacterProgressions  # noqa: E501

        :return: The progressions of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._progressions

    @progressions.setter
    def progressions(self, progressions):
        """Sets the progressions of this DestinyResponsesDestinyCharacterResponse.

        Character progression data, including Milestones.  COMPONENT TYPE: CharacterProgressions  # noqa: E501

        :param progressions: The progressions of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._progressions = progressions

    @property
    def render_data(self):
        """Gets the render_data of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Character rendering data - a minimal set of information about equipment and dyes used for rendering.  COMPONENT TYPE: CharacterRenderData  # noqa: E501

        :return: The render_data of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._render_data

    @render_data.setter
    def render_data(self, render_data):
        """Sets the render_data of this DestinyResponsesDestinyCharacterResponse.

        Character rendering data - a minimal set of information about equipment and dyes used for rendering.  COMPONENT TYPE: CharacterRenderData  # noqa: E501

        :param render_data: The render_data of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._render_data = render_data

    @property
    def activities(self):
        """Gets the activities of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Activity data - info about current activities available to the player.  COMPONENT TYPE: CharacterActivities  # noqa: E501

        :return: The activities of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this DestinyResponsesDestinyCharacterResponse.

        Activity data - info about current activities available to the player.  COMPONENT TYPE: CharacterActivities  # noqa: E501

        :param activities: The activities of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._activities = activities

    @property
    def equipment(self):
        """Gets the equipment of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Equipped items on the character.  COMPONENT TYPE: CharacterEquipment  # noqa: E501

        :return: The equipment of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this DestinyResponsesDestinyCharacterResponse.

        Equipped items on the character.  COMPONENT TYPE: CharacterEquipment  # noqa: E501

        :param equipment: The equipment of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._equipment = equipment

    @property
    def kiosks(self):
        """Gets the kiosks of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        Items available from Kiosks that are available to this specific character.   COMPONENT TYPE: Kiosks  # noqa: E501

        :return: The kiosks of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._kiosks

    @kiosks.setter
    def kiosks(self, kiosks):
        """Sets the kiosks of this DestinyResponsesDestinyCharacterResponse.

        Items available from Kiosks that are available to this specific character.   COMPONENT TYPE: Kiosks  # noqa: E501

        :param kiosks: The kiosks of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._kiosks = kiosks

    @property
    def item_components(self):
        """Gets the item_components of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501

        The set of components belonging to the player's instanced items.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]  # noqa: E501

        :return: The item_components of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :rtype: object
        """
        return self._item_components

    @item_components.setter
    def item_components(self, item_components):
        """Sets the item_components of this DestinyResponsesDestinyCharacterResponse.

        The set of components belonging to the player's instanced items.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]  # noqa: E501

        :param item_components: The item_components of this DestinyResponsesDestinyCharacterResponse.  # noqa: E501
        :type: object
        """

        self._item_components = item_components

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
        if not isinstance(other, DestinyResponsesDestinyCharacterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
