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


class DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition(object):
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
        'id': 'int',
        'objective_hash': 'int'
    }

    attribute_map = {
        'id': 'id',
        'objective_hash': 'objectiveHash'
    }

    def __init__(self, id=None, objective_hash=None):
        """
        DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition - a model defined in Swagger
        """

        self._id = None
        self._objective_hash = None

        if id is not None:
          self.id = id
        if objective_hash is not None:
          self.objective_hash = objective_hash

    @property
    def id(self):
        """
        Gets the id of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        $NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives  to display info.  I am unsure how it works.

        :return: The id of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        $NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives  to display info.  I am unsure how it works.

        :param id: The id of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        :type: int
        """

        self._id = id

    @property
    def objective_hash(self):
        """
        Gets the objective_hash of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        The objective being shown on the map.

        :return: The objective_hash of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        :rtype: int
        """
        return self._objective_hash

    @objective_hash.setter
    def objective_hash(self, objective_hash):
        """
        Sets the objective_hash of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        The objective being shown on the map.

        :param objective_hash: The objective_hash of this DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition.
        :type: int
        """

        self._objective_hash = objective_hash

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
        if not isinstance(other, DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
