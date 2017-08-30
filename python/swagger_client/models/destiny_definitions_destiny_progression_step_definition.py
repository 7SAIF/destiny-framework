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


class DestinyDefinitionsDestinyProgressionStepDefinition(object):
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
        'step_name': 'str',
        'progress_total': 'int',
        'reward_items': 'list[DestinyDestinyItemQuantity]'
    }

    attribute_map = {
        'step_name': 'stepName',
        'progress_total': 'progressTotal',
        'reward_items': 'rewardItems'
    }

    def __init__(self, step_name=None, progress_total=None, reward_items=None):
        """
        DestinyDefinitionsDestinyProgressionStepDefinition - a model defined in Swagger
        """

        self._step_name = None
        self._progress_total = None
        self._reward_items = None

        if step_name is not None:
          self.step_name = step_name
        if progress_total is not None:
          self.progress_total = progress_total
        if reward_items is not None:
          self.reward_items = reward_items

    @property
    def step_name(self):
        """
        Gets the step_name of this DestinyDefinitionsDestinyProgressionStepDefinition.
        Very rarely, Progressions will have localized text describing the Level of the progression.  This will be that localized text, if it exists.  Otherwise, the standard appears to be  to simply show the level numerically.

        :return: The step_name of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this DestinyDefinitionsDestinyProgressionStepDefinition.
        Very rarely, Progressions will have localized text describing the Level of the progression.  This will be that localized text, if it exists.  Otherwise, the standard appears to be  to simply show the level numerically.

        :param step_name: The step_name of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :type: str
        """

        self._step_name = step_name

    @property
    def progress_total(self):
        """
        Gets the progress_total of this DestinyDefinitionsDestinyProgressionStepDefinition.
        The total amount of progression points/\"experience\" you will need to initially reach this step.  If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep),  this will also be the progress needed to level it up further by repeating this step again.

        :return: The progress_total of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :rtype: int
        """
        return self._progress_total

    @progress_total.setter
    def progress_total(self, progress_total):
        """
        Sets the progress_total of this DestinyDefinitionsDestinyProgressionStepDefinition.
        The total amount of progression points/\"experience\" you will need to initially reach this step.  If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep),  this will also be the progress needed to level it up further by repeating this step again.

        :param progress_total: The progress_total of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :type: int
        """

        self._progress_total = progress_total

    @property
    def reward_items(self):
        """
        Gets the reward_items of this DestinyDefinitionsDestinyProgressionStepDefinition.
        A listing of items rewarded as a result of reaching this level.

        :return: The reward_items of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :rtype: list[DestinyDestinyItemQuantity]
        """
        return self._reward_items

    @reward_items.setter
    def reward_items(self, reward_items):
        """
        Sets the reward_items of this DestinyDefinitionsDestinyProgressionStepDefinition.
        A listing of items rewarded as a result of reaching this level.

        :param reward_items: The reward_items of this DestinyDefinitionsDestinyProgressionStepDefinition.
        :type: list[DestinyDestinyItemQuantity]
        """

        self._reward_items = reward_items

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
        if not isinstance(other, DestinyDefinitionsDestinyProgressionStepDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
