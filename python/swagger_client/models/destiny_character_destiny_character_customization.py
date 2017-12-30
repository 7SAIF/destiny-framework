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


class DestinyCharacterDestinyCharacterCustomization(object):
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
        'personality': 'int',
        'face': 'int',
        'skin_color': 'int',
        'lip_color': 'int',
        'eye_color': 'int',
        'hair_colors': 'list[int]',
        'feature_colors': 'list[int]',
        'decal_color': 'int',
        'wear_helmet': 'bool',
        'hair_index': 'int',
        'feature_index': 'int',
        'decal_index': 'int'
    }

    attribute_map = {
        'personality': 'personality',
        'face': 'face',
        'skin_color': 'skinColor',
        'lip_color': 'lipColor',
        'eye_color': 'eyeColor',
        'hair_colors': 'hairColors',
        'feature_colors': 'featureColors',
        'decal_color': 'decalColor',
        'wear_helmet': 'wearHelmet',
        'hair_index': 'hairIndex',
        'feature_index': 'featureIndex',
        'decal_index': 'decalIndex'
    }

    def __init__(self, personality=None, face=None, skin_color=None, lip_color=None, eye_color=None, hair_colors=None, feature_colors=None, decal_color=None, wear_helmet=None, hair_index=None, feature_index=None, decal_index=None):  # noqa: E501
        """DestinyCharacterDestinyCharacterCustomization - a model defined in Swagger"""  # noqa: E501

        self._personality = None
        self._face = None
        self._skin_color = None
        self._lip_color = None
        self._eye_color = None
        self._hair_colors = None
        self._feature_colors = None
        self._decal_color = None
        self._wear_helmet = None
        self._hair_index = None
        self._feature_index = None
        self._decal_index = None
        self.discriminator = None

        if personality is not None:
            self.personality = personality
        if face is not None:
            self.face = face
        if skin_color is not None:
            self.skin_color = skin_color
        if lip_color is not None:
            self.lip_color = lip_color
        if eye_color is not None:
            self.eye_color = eye_color
        if hair_colors is not None:
            self.hair_colors = hair_colors
        if feature_colors is not None:
            self.feature_colors = feature_colors
        if decal_color is not None:
            self.decal_color = decal_color
        if wear_helmet is not None:
            self.wear_helmet = wear_helmet
        if hair_index is not None:
            self.hair_index = hair_index
        if feature_index is not None:
            self.feature_index = feature_index
        if decal_index is not None:
            self.decal_index = decal_index

    @property
    def personality(self):
        """Gets the personality of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The personality of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._personality

    @personality.setter
    def personality(self, personality):
        """Sets the personality of this DestinyCharacterDestinyCharacterCustomization.


        :param personality: The personality of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._personality = personality

    @property
    def face(self):
        """Gets the face of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The face of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._face

    @face.setter
    def face(self, face):
        """Sets the face of this DestinyCharacterDestinyCharacterCustomization.


        :param face: The face of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._face = face

    @property
    def skin_color(self):
        """Gets the skin_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The skin_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._skin_color

    @skin_color.setter
    def skin_color(self, skin_color):
        """Sets the skin_color of this DestinyCharacterDestinyCharacterCustomization.


        :param skin_color: The skin_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._skin_color = skin_color

    @property
    def lip_color(self):
        """Gets the lip_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The lip_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._lip_color

    @lip_color.setter
    def lip_color(self, lip_color):
        """Sets the lip_color of this DestinyCharacterDestinyCharacterCustomization.


        :param lip_color: The lip_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._lip_color = lip_color

    @property
    def eye_color(self):
        """Gets the eye_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The eye_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._eye_color

    @eye_color.setter
    def eye_color(self, eye_color):
        """Sets the eye_color of this DestinyCharacterDestinyCharacterCustomization.


        :param eye_color: The eye_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._eye_color = eye_color

    @property
    def hair_colors(self):
        """Gets the hair_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The hair_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: list[int]
        """
        return self._hair_colors

    @hair_colors.setter
    def hair_colors(self, hair_colors):
        """Sets the hair_colors of this DestinyCharacterDestinyCharacterCustomization.


        :param hair_colors: The hair_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: list[int]
        """

        self._hair_colors = hair_colors

    @property
    def feature_colors(self):
        """Gets the feature_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The feature_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: list[int]
        """
        return self._feature_colors

    @feature_colors.setter
    def feature_colors(self, feature_colors):
        """Sets the feature_colors of this DestinyCharacterDestinyCharacterCustomization.


        :param feature_colors: The feature_colors of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: list[int]
        """

        self._feature_colors = feature_colors

    @property
    def decal_color(self):
        """Gets the decal_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The decal_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._decal_color

    @decal_color.setter
    def decal_color(self, decal_color):
        """Sets the decal_color of this DestinyCharacterDestinyCharacterCustomization.


        :param decal_color: The decal_color of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._decal_color = decal_color

    @property
    def wear_helmet(self):
        """Gets the wear_helmet of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The wear_helmet of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: bool
        """
        return self._wear_helmet

    @wear_helmet.setter
    def wear_helmet(self, wear_helmet):
        """Sets the wear_helmet of this DestinyCharacterDestinyCharacterCustomization.


        :param wear_helmet: The wear_helmet of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: bool
        """

        self._wear_helmet = wear_helmet

    @property
    def hair_index(self):
        """Gets the hair_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The hair_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._hair_index

    @hair_index.setter
    def hair_index(self, hair_index):
        """Sets the hair_index of this DestinyCharacterDestinyCharacterCustomization.


        :param hair_index: The hair_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._hair_index = hair_index

    @property
    def feature_index(self):
        """Gets the feature_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The feature_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._feature_index

    @feature_index.setter
    def feature_index(self, feature_index):
        """Sets the feature_index of this DestinyCharacterDestinyCharacterCustomization.


        :param feature_index: The feature_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._feature_index = feature_index

    @property
    def decal_index(self):
        """Gets the decal_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501


        :return: The decal_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :rtype: int
        """
        return self._decal_index

    @decal_index.setter
    def decal_index(self, decal_index):
        """Sets the decal_index of this DestinyCharacterDestinyCharacterCustomization.


        :param decal_index: The decal_index of this DestinyCharacterDestinyCharacterCustomization.  # noqa: E501
        :type: int
        """

        self._decal_index = decal_index

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
        if not isinstance(other, DestinyCharacterDestinyCharacterCustomization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
