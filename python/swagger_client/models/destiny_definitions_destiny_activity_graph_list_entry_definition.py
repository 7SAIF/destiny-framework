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


class DestinyDefinitionsDestinyActivityGraphListEntryDefinition(object):
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
        'activity_graph_hash': 'int'
    }

    attribute_map = {
        'activity_graph_hash': 'activityGraphHash'
    }

    def __init__(self, activity_graph_hash=None):
        """
        DestinyDefinitionsDestinyActivityGraphListEntryDefinition - a model defined in Swagger
        """

        self._activity_graph_hash = None

        if activity_graph_hash is not None:
          self.activity_graph_hash = activity_graph_hash

    @property
    def activity_graph_hash(self):
        """
        Gets the activity_graph_hash of this DestinyDefinitionsDestinyActivityGraphListEntryDefinition.
        The hash identifier of the DestinyActivityGraphDefinition that should be shown when openingthe director.

        :return: The activity_graph_hash of this DestinyDefinitionsDestinyActivityGraphListEntryDefinition.
        :rtype: int
        """
        return self._activity_graph_hash

    @activity_graph_hash.setter
    def activity_graph_hash(self, activity_graph_hash):
        """
        Sets the activity_graph_hash of this DestinyDefinitionsDestinyActivityGraphListEntryDefinition.
        The hash identifier of the DestinyActivityGraphDefinition that should be shown when openingthe director.

        :param activity_graph_hash: The activity_graph_hash of this DestinyDefinitionsDestinyActivityGraphListEntryDefinition.
        :type: int
        """

        self._activity_graph_hash = activity_graph_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyActivityGraphListEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
