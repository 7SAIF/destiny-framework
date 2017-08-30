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


class DestinyDefinitionsCommonDestinyPositionDefinition(object):
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
        'x': 'int',
        'y': 'int',
        'z': 'int'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }

    def __init__(self, x=None, y=None, z=None):
        """
        DestinyDefinitionsCommonDestinyPositionDefinition - a model defined in Swagger
        """

        self._x = None
        self._y = None
        self._z = None

        if x is not None:
          self.x = x
        if y is not None:
          self.y = y
        if z is not None:
          self.z = z

    @property
    def x(self):
        """
        Gets the x of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :return: The x of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :param x: The x of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """
        Gets the y of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :return: The y of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :param y: The y of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :type: int
        """

        self._y = y

    @property
    def z(self):
        """
        Gets the z of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :return: The z of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :rtype: int
        """
        return self._z

    @z.setter
    def z(self, z):
        """
        Sets the z of this DestinyDefinitionsCommonDestinyPositionDefinition.

        :param z: The z of this DestinyDefinitionsCommonDestinyPositionDefinition.
        :type: int
        """

        self._z = z

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
        if not isinstance(other, DestinyDefinitionsCommonDestinyPositionDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
