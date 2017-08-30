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


class DestinyDefinitionsDestinyStatGroupDefinition(object):
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
        'maximum_value': 'int',
        'ui_position': 'int',
        'scaled_stats': 'list[DestinyDefinitionsDestinyStatDisplayDefinition]',
        'overrides': 'dict(str, DestinyDefinitionsDestinyStatOverrideDefinition)',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'maximum_value': 'maximumValue',
        'ui_position': 'uiPosition',
        'scaled_stats': 'scaledStats',
        'overrides': 'overrides',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, maximum_value=None, ui_position=None, scaled_stats=None, overrides=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyStatGroupDefinition - a model defined in Swagger
        """

        self._maximum_value = None
        self._ui_position = None
        self._scaled_stats = None
        self._overrides = None
        self._hash = None
        self._index = None
        self._redacted = None

        if maximum_value is not None:
          self.maximum_value = maximum_value
        if ui_position is not None:
          self.ui_position = ui_position
        if scaled_stats is not None:
          self.scaled_stats = scaled_stats
        if overrides is not None:
          self.overrides = overrides
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def maximum_value(self):
        """
        Gets the maximum_value of this DestinyDefinitionsDestinyStatGroupDefinition.
        The maximum possible value that any stat in this group can be transformed into.    This is used by stats that *don't* have scaledStats entries below, but that  still need to be displayed as a progress bar, in which case this is used  as the upper bound for said progress bar.  (the lower bound is always 0)

        :return: The maximum_value of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: int
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """
        Sets the maximum_value of this DestinyDefinitionsDestinyStatGroupDefinition.
        The maximum possible value that any stat in this group can be transformed into.    This is used by stats that *don't* have scaledStats entries below, but that  still need to be displayed as a progress bar, in which case this is used  as the upper bound for said progress bar.  (the lower bound is always 0)

        :param maximum_value: The maximum_value of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: int
        """

        self._maximum_value = maximum_value

    @property
    def ui_position(self):
        """
        Gets the ui_position of this DestinyDefinitionsDestinyStatGroupDefinition.
        This apparently indicates the position of the stats in the UI?  I've returned it  in case anyone can use it, but it's not of any use to us on BNet.  Something's being  lost in translation with this value.

        :return: The ui_position of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: int
        """
        return self._ui_position

    @ui_position.setter
    def ui_position(self, ui_position):
        """
        Sets the ui_position of this DestinyDefinitionsDestinyStatGroupDefinition.
        This apparently indicates the position of the stats in the UI?  I've returned it  in case anyone can use it, but it's not of any use to us on BNet.  Something's being  lost in translation with this value.

        :param ui_position: The ui_position of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: int
        """

        self._ui_position = ui_position

    @property
    def scaled_stats(self):
        """
        Gets the scaled_stats of this DestinyDefinitionsDestinyStatGroupDefinition.
        Any stat that requires scaling to be transformed from an \"Investment\" stat to a \"Display\"  stat will have an entry in this list.  For more information on what those types of stats  mean and the transformation process, see DestinyStatDefinition.    In retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead.  But I'm going to leave it be because [[After Apple Picking]].

        :return: The scaled_stats of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: list[DestinyDefinitionsDestinyStatDisplayDefinition]
        """
        return self._scaled_stats

    @scaled_stats.setter
    def scaled_stats(self, scaled_stats):
        """
        Sets the scaled_stats of this DestinyDefinitionsDestinyStatGroupDefinition.
        Any stat that requires scaling to be transformed from an \"Investment\" stat to a \"Display\"  stat will have an entry in this list.  For more information on what those types of stats  mean and the transformation process, see DestinyStatDefinition.    In retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead.  But I'm going to leave it be because [[After Apple Picking]].

        :param scaled_stats: The scaled_stats of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: list[DestinyDefinitionsDestinyStatDisplayDefinition]
        """

        self._scaled_stats = scaled_stats

    @property
    def overrides(self):
        """
        Gets the overrides of this DestinyDefinitionsDestinyStatGroupDefinition.
        The game has the ability to override, based on the stat group, what the localized text is  that is displayed for Stats being shown on the item.    Mercifully, no Stat Groups use this feature currently.  If they start using them,  we'll all need to start using them (and those of you who are more prudent than I am  can go ahead and start pre-checking for this.)

        :return: The overrides of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: dict(str, DestinyDefinitionsDestinyStatOverrideDefinition)
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """
        Sets the overrides of this DestinyDefinitionsDestinyStatGroupDefinition.
        The game has the ability to override, based on the stat group, what the localized text is  that is displayed for Stats being shown on the item.    Mercifully, no Stat Groups use this feature currently.  If they start using them,  we'll all need to start using them (and those of you who are more prudent than I am  can go ahead and start pre-checking for this.)

        :param overrides: The overrides of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: dict(str, DestinyDefinitionsDestinyStatOverrideDefinition)
        """

        self._overrides = overrides

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyStatGroupDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.    When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyStatGroupDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.    When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyStatGroupDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyStatGroupDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyStatGroupDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet is  not yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyStatGroupDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyStatGroupDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet is  not yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyStatGroupDefinition.
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyDefinitionsDestinyStatGroupDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
