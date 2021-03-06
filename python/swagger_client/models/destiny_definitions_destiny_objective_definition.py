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


class DestinyDefinitionsDestinyObjectiveDefinition(object):
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
        'display_properties': 'object',
        'completion_value': 'int',
        'location_hash': 'int',
        'allow_negative_value': 'bool',
        'allow_value_change_when_completed': 'bool',
        'is_counting_downward': 'bool',
        'value_style': 'object',
        'progress_description': 'str',
        'perks': 'object',
        'stats': 'object',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'completion_value': 'completionValue',
        'location_hash': 'locationHash',
        'allow_negative_value': 'allowNegativeValue',
        'allow_value_change_when_completed': 'allowValueChangeWhenCompleted',
        'is_counting_downward': 'isCountingDownward',
        'value_style': 'valueStyle',
        'progress_description': 'progressDescription',
        'perks': 'perks',
        'stats': 'stats',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, completion_value=None, location_hash=None, allow_negative_value=None, allow_value_change_when_completed=None, is_counting_downward=None, value_style=None, progress_description=None, perks=None, stats=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyDefinitionsDestinyObjectiveDefinition - a model defined in Swagger"""  # noqa: E501

        self._display_properties = None
        self._completion_value = None
        self._location_hash = None
        self._allow_negative_value = None
        self._allow_value_change_when_completed = None
        self._is_counting_downward = None
        self._value_style = None
        self._progress_description = None
        self._perks = None
        self._stats = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if completion_value is not None:
            self.completion_value = completion_value
        if location_hash is not None:
            self.location_hash = location_hash
        if allow_negative_value is not None:
            self.allow_negative_value = allow_negative_value
        if allow_value_change_when_completed is not None:
            self.allow_value_change_when_completed = allow_value_change_when_completed
        if is_counting_downward is not None:
            self.is_counting_downward = is_counting_downward
        if value_style is not None:
            self.value_style = value_style
        if progress_description is not None:
            self.progress_description = progress_description
        if perks is not None:
            self.perks = perks
        if stats is not None:
            self.stats = stats
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it.  # noqa: E501

        :return: The display_properties of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: object
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyDefinitionsDestinyObjectiveDefinition.

        Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it.  # noqa: E501

        :param display_properties: The display_properties of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: object
        """

        self._display_properties = display_properties

    @property
    def completion_value(self):
        """Gets the completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status.  # noqa: E501

        :return: The completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: int
        """
        return self._completion_value

    @completion_value.setter
    def completion_value(self, completion_value):
        """Sets the completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.

        The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status.  # noqa: E501

        :param completion_value: The completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: int
        """

        self._completion_value = completion_value

    @property
    def location_hash(self):
        """Gets the location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info.  # noqa: E501

        :return: The location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: int
        """
        return self._location_hash

    @location_hash.setter
    def location_hash(self, location_hash):
        """Sets the location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.

        OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info.  # noqa: E501

        :param location_hash: The location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: int
        """

        self._location_hash = location_hash

    @property
    def allow_negative_value(self):
        """Gets the allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If true, the value is allowed to go negative.  # noqa: E501

        :return: The allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._allow_negative_value

    @allow_negative_value.setter
    def allow_negative_value(self, allow_negative_value):
        """Sets the allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.

        If true, the value is allowed to go negative.  # noqa: E501

        :param allow_negative_value: The allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: bool
        """

        self._allow_negative_value = allow_negative_value

    @property
    def allow_value_change_when_completed(self):
        """Gets the allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If true, you can effectively \"un-complete\" this objective if you lose progress after crossing the completion threshold.   If False, once you complete the task it will remain completed forever by locking the value.  # noqa: E501

        :return: The allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._allow_value_change_when_completed

    @allow_value_change_when_completed.setter
    def allow_value_change_when_completed(self, allow_value_change_when_completed):
        """Sets the allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.

        If true, you can effectively \"un-complete\" this objective if you lose progress after crossing the completion threshold.   If False, once you complete the task it will remain completed forever by locking the value.  # noqa: E501

        :param allow_value_change_when_completed: The allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: bool
        """

        self._allow_value_change_when_completed = allow_value_change_when_completed

    @property
    def is_counting_downward(self):
        """Gets the is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue.  # noqa: E501

        :return: The is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_counting_downward

    @is_counting_downward.setter
    def is_counting_downward(self, is_counting_downward):
        """Sets the is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.

        If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue.  # noqa: E501

        :param is_counting_downward: The is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: bool
        """

        self._is_counting_downward = is_counting_downward

    @property
    def value_style(self):
        """Gets the value_style of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.  # noqa: E501

        :return: The value_style of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: object
        """
        return self._value_style

    @value_style.setter
    def value_style(self, value_style):
        """Sets the value_style of this DestinyDefinitionsDestinyObjectiveDefinition.

        The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.  # noqa: E501

        :param value_style: The value_style of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: object
        """

        self._value_style = value_style

    @property
    def progress_description(self):
        """Gets the progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        Text to describe the progress bar.  # noqa: E501

        :return: The progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: str
        """
        return self._progress_description

    @progress_description.setter
    def progress_description(self, progress_description):
        """Sets the progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.

        Text to describe the progress bar.  # noqa: E501

        :param progress_description: The progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: str
        """

        self._progress_description = progress_description

    @property
    def perks(self):
        """Gets the perks of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If this objective enables Perks intrinsically, the conditions for that enabling are defined here.  # noqa: E501

        :return: The perks of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: object
        """
        return self._perks

    @perks.setter
    def perks(self, perks):
        """Sets the perks of this DestinyDefinitionsDestinyObjectiveDefinition.

        If this objective enables Perks intrinsically, the conditions for that enabling are defined here.  # noqa: E501

        :param perks: The perks of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: object
        """

        self._perks = perks

    @property
    def stats(self):
        """Gets the stats of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If this objective enables modifications on a player's stats intrinsically, the conditions are defined here.  # noqa: E501

        :return: The stats of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: object
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this DestinyDefinitionsDestinyObjectiveDefinition.

        If this objective enables modifications on a player's stats intrinsically, the conditions are defined here.  # noqa: E501

        :param stats: The stats of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: object
        """

        self._stats = stats

    @property
    def hash(self):
        """Gets the hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyDefinitionsDestinyObjectiveDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyDefinitionsDestinyObjectiveDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyDefinitionsDestinyObjectiveDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyDefinitionsDestinyObjectiveDefinition.  # noqa: E501
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyDefinitionsDestinyObjectiveDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
