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


class DestinyDestinyTalentNodeStatBlock(object):
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
        'current_step_stats': 'list[DestinyDestinyStat]',
        'next_step_stats': 'list[DestinyDestinyStat]'
    }

    attribute_map = {
        'current_step_stats': 'currentStepStats',
        'next_step_stats': 'nextStepStats'
    }

    def __init__(self, current_step_stats=None, next_step_stats=None):
        """
        DestinyDestinyTalentNodeStatBlock - a model defined in Swagger
        """

        self._current_step_stats = None
        self._next_step_stats = None

        if current_step_stats is not None:
          self.current_step_stats = current_step_stats
        if next_step_stats is not None:
          self.next_step_stats = next_step_stats

    @property
    def current_step_stats(self):
        """
        Gets the current_step_stats of this DestinyDestinyTalentNodeStatBlock.
        The stat benefits conferred when this talent node is activated for the current Step that is active on the node.

        :return: The current_step_stats of this DestinyDestinyTalentNodeStatBlock.
        :rtype: list[DestinyDestinyStat]
        """
        return self._current_step_stats

    @current_step_stats.setter
    def current_step_stats(self, current_step_stats):
        """
        Sets the current_step_stats of this DestinyDestinyTalentNodeStatBlock.
        The stat benefits conferred when this talent node is activated for the current Step that is active on the node.

        :param current_step_stats: The current_step_stats of this DestinyDestinyTalentNodeStatBlock.
        :type: list[DestinyDestinyStat]
        """

        self._current_step_stats = current_step_stats

    @property
    def next_step_stats(self):
        """
        Gets the next_step_stats of this DestinyDestinyTalentNodeStatBlock.
        This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring  multiple steps worth of benefits: you would use this property to show what activating the \"next\" step on the node  would provide vs. what the current step is providing.  While Nodes are currently not being used this way, the underlying system for this functionality still exists.  I hesitate to remove this property while the ability for designers to make such a talent grid still exists.  Whether you want to show it is up to you.

        :return: The next_step_stats of this DestinyDestinyTalentNodeStatBlock.
        :rtype: list[DestinyDestinyStat]
        """
        return self._next_step_stats

    @next_step_stats.setter
    def next_step_stats(self, next_step_stats):
        """
        Sets the next_step_stats of this DestinyDestinyTalentNodeStatBlock.
        This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring  multiple steps worth of benefits: you would use this property to show what activating the \"next\" step on the node  would provide vs. what the current step is providing.  While Nodes are currently not being used this way, the underlying system for this functionality still exists.  I hesitate to remove this property while the ability for designers to make such a talent grid still exists.  Whether you want to show it is up to you.

        :param next_step_stats: The next_step_stats of this DestinyDestinyTalentNodeStatBlock.
        :type: list[DestinyDestinyStat]
        """

        self._next_step_stats = next_step_stats

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
        if not isinstance(other, DestinyDestinyTalentNodeStatBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other