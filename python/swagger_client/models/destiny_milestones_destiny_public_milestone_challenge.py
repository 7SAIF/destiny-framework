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


class DestinyMilestonesDestinyPublicMilestoneChallenge(object):
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
        'objective_hash': 'int',
        'activity_hash': 'int'
    }

    attribute_map = {
        'objective_hash': 'objectiveHash',
        'activity_hash': 'activityHash'
    }

    def __init__(self, objective_hash=None, activity_hash=None):
        """
        DestinyMilestonesDestinyPublicMilestoneChallenge - a model defined in Swagger
        """

        self._objective_hash = None
        self._activity_hash = None

        if objective_hash is not None:
          self.objective_hash = objective_hash
        if activity_hash is not None:
          self.activity_hash = activity_hash

    @property
    def objective_hash(self):
        """
        Gets the objective_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        The objective for the Challenge, which should have human-readable data about what  needs to be done to accomplish the objective.  Use this hash to look up the DestinyObjectiveDefinition.

        :return: The objective_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        :rtype: int
        """
        return self._objective_hash

    @objective_hash.setter
    def objective_hash(self, objective_hash):
        """
        Sets the objective_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        The objective for the Challenge, which should have human-readable data about what  needs to be done to accomplish the objective.  Use this hash to look up the DestinyObjectiveDefinition.

        :param objective_hash: The objective_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        :type: int
        """

        self._objective_hash = objective_hash

    @property
    def activity_hash(self):
        """
        Gets the activity_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        IF the Objective is related to a specific Activity, this will be that activity's hash.  Use it to look up the DestinyActivityDefinition for additional data to show.

        :return: The activity_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """
        Sets the activity_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        IF the Objective is related to a specific Activity, this will be that activity's hash.  Use it to look up the DestinyActivityDefinition for additional data to show.

        :param activity_hash: The activity_hash of this DestinyMilestonesDestinyPublicMilestoneChallenge.
        :type: int
        """

        self._activity_hash = activity_hash

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
        if not isinstance(other, DestinyMilestonesDestinyPublicMilestoneChallenge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other