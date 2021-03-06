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

from swagger_client.models.destiny_dye_reference import DestinyDyeReference  # noqa: F401,E501


class DestinyEntitiesCharactersDestinyCharacterRenderComponent(object):
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
        'custom_dyes': 'list[DestinyDyeReference]',
        'customization': 'object',
        'peer_view': 'object'
    }

    attribute_map = {
        'custom_dyes': 'customDyes',
        'customization': 'customization',
        'peer_view': 'peerView'
    }

    def __init__(self, custom_dyes=None, customization=None, peer_view=None):  # noqa: E501
        """DestinyEntitiesCharactersDestinyCharacterRenderComponent - a model defined in Swagger"""  # noqa: E501

        self._custom_dyes = None
        self._customization = None
        self._peer_view = None
        self.discriminator = None

        if custom_dyes is not None:
            self.custom_dyes = custom_dyes
        if customization is not None:
            self.customization = customization
        if peer_view is not None:
            self.peer_view = peer_view

    @property
    def custom_dyes(self):
        """Gets the custom_dyes of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501

        Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.  # noqa: E501

        :return: The custom_dyes of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :rtype: list[DestinyDyeReference]
        """
        return self._custom_dyes

    @custom_dyes.setter
    def custom_dyes(self, custom_dyes):
        """Sets the custom_dyes of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.

        Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.  # noqa: E501

        :param custom_dyes: The custom_dyes of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :type: list[DestinyDyeReference]
        """

        self._custom_dyes = custom_dyes

    @property
    def customization(self):
        """Gets the customization of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501

        This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.  # noqa: E501

        :return: The customization of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :rtype: object
        """
        return self._customization

    @customization.setter
    def customization(self, customization):
        """Sets the customization of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.

        This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.  # noqa: E501

        :param customization: The customization of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :type: object
        """

        self._customization = customization

    @property
    def peer_view(self):
        """Gets the peer_view of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501

        A minimal view of:  - Equipped items  - The rendering-related custom options on those equipped items  Combined, that should be enough to render all of the items on the equipped character.  # noqa: E501

        :return: The peer_view of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :rtype: object
        """
        return self._peer_view

    @peer_view.setter
    def peer_view(self, peer_view):
        """Sets the peer_view of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.

        A minimal view of:  - Equipped items  - The rendering-related custom options on those equipped items  Combined, that should be enough to render all of the items on the equipped character.  # noqa: E501

        :param peer_view: The peer_view of this DestinyEntitiesCharactersDestinyCharacterRenderComponent.  # noqa: E501
        :type: object
        """

        self._peer_view = peer_view

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
        if not isinstance(other, DestinyEntitiesCharactersDestinyCharacterRenderComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
