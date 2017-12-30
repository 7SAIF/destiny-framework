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

from swagger_client.models.destiny_definitions_common_destiny_display_properties_definition import DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition  # noqa: F401,E501
from swagger_client.models.destiny_historical_stats_definitions_destiny_activity_mode_type import DestinyHistoricalStatsDefinitionsDestinyActivityModeType  # noqa: F401,E501


class DestinyDefinitionsDestinyActivityModeDefinition(object):
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
        'display_properties': 'DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition',
        'pgcr_image': 'str',
        'mode_type': 'object',
        'activity_mode_category': 'object',
        'is_team_based': 'bool',
        'is_aggregate_mode': 'bool',
        'parent_hashes': 'list[int]',
        'friendly_name': 'str',
        'activity_mode_mappings': 'dict(str, DestinyHistoricalStatsDefinitionsDestinyActivityModeType)',
        'display': 'bool',
        'order': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'pgcr_image': 'pgcrImage',
        'mode_type': 'modeType',
        'activity_mode_category': 'activityModeCategory',
        'is_team_based': 'isTeamBased',
        'is_aggregate_mode': 'isAggregateMode',
        'parent_hashes': 'parentHashes',
        'friendly_name': 'friendlyName',
        'activity_mode_mappings': 'activityModeMappings',
        'display': 'display',
        'order': 'order',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, pgcr_image=None, mode_type=None, activity_mode_category=None, is_team_based=None, is_aggregate_mode=None, parent_hashes=None, friendly_name=None, activity_mode_mappings=None, display=None, order=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyDefinitionsDestinyActivityModeDefinition - a model defined in Swagger"""  # noqa: E501

        self._display_properties = None
        self._pgcr_image = None
        self._mode_type = None
        self._activity_mode_category = None
        self._is_team_based = None
        self._is_aggregate_mode = None
        self._parent_hashes = None
        self._friendly_name = None
        self._activity_mode_mappings = None
        self._display = None
        self._order = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if pgcr_image is not None:
            self.pgcr_image = pgcr_image
        if mode_type is not None:
            self.mode_type = mode_type
        if activity_mode_category is not None:
            self.activity_mode_category = activity_mode_category
        if is_team_based is not None:
            self.is_team_based = is_team_based
        if is_aggregate_mode is not None:
            self.is_aggregate_mode = is_aggregate_mode
        if parent_hashes is not None:
            self.parent_hashes = parent_hashes
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if activity_mode_mappings is not None:
            self.activity_mode_mappings = activity_mode_mappings
        if display is not None:
            self.display = display
        if order is not None:
            self.order = order
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501


        :return: The display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.


        :param display_properties: The display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def pgcr_image(self):
        """Gets the pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If this activity mode has a related PGCR image, this will be the path to said image.  # noqa: E501

        :return: The pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pgcr_image

    @pgcr_image.setter
    def pgcr_image(self, pgcr_image):
        """Sets the pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.

        If this activity mode has a related PGCR image, this will be the path to said image.  # noqa: E501

        :param pgcr_image: The pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: str
        """

        self._pgcr_image = pgcr_image

    @property
    def mode_type(self):
        """Gets the mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode.  # noqa: E501

        :return: The mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: object
        """
        return self._mode_type

    @mode_type.setter
    def mode_type(self, mode_type):
        """Sets the mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.

        The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode.  # noqa: E501

        :param mode_type: The mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: object
        """

        self._mode_type = mode_type

    @property
    def activity_mode_category(self):
        """Gets the activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The type of play being performed in broad terms (PVP, PVE)  # noqa: E501

        :return: The activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: object
        """
        return self._activity_mode_category

    @activity_mode_category.setter
    def activity_mode_category(self, activity_mode_category):
        """Sets the activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.

        The type of play being performed in broad terms (PVP, PVE)  # noqa: E501

        :param activity_mode_category: The activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: object
        """

        self._activity_mode_category = activity_mode_category

    @property
    def is_team_based(self):
        """Gets the is_team_based of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If True, this mode has oppositional teams fighting against each other rather than \"Free-For-All\" or Co-operative modes of play.  Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become \"sometimes team based\"). Let's not deal with that right now.  # noqa: E501

        :return: The is_team_based of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_team_based

    @is_team_based.setter
    def is_team_based(self, is_team_based):
        """Sets the is_team_based of this DestinyDefinitionsDestinyActivityModeDefinition.

        If True, this mode has oppositional teams fighting against each other rather than \"Free-For-All\" or Co-operative modes of play.  Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become \"sometimes team based\"). Let's not deal with that right now.  # noqa: E501

        :param is_team_based: The is_team_based of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: bool
        """

        self._is_team_based = is_team_based

    @property
    def is_aggregate_mode(self):
        """Gets the is_aggregate_mode of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash.  # noqa: E501

        :return: The is_aggregate_mode of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_aggregate_mode

    @is_aggregate_mode.setter
    def is_aggregate_mode(self, is_aggregate_mode):
        """Sets the is_aggregate_mode of this DestinyDefinitionsDestinyActivityModeDefinition.

        If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash.  # noqa: E501

        :param is_aggregate_mode: The is_aggregate_mode of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: bool
        """

        self._is_aggregate_mode = is_aggregate_mode

    @property
    def parent_hashes(self):
        """Gets the parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The hash identifiers of the DestinyActivityModeDefinitions that represent all of the \"parent\" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE.  # noqa: E501

        :return: The parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_hashes

    @parent_hashes.setter
    def parent_hashes(self, parent_hashes):
        """Sets the parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.

        The hash identifiers of the DestinyActivityModeDefinitions that represent all of the \"parent\" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE.  # noqa: E501

        :param parent_hashes: The parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: list[int]
        """

        self._parent_hashes = parent_hashes

    @property
    def friendly_name(self):
        """Gets the friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth.  # noqa: E501

        :return: The friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.

        A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth.  # noqa: E501

        :param friendly_name: The friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def activity_mode_mappings(self):
        """Gets the activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played.  # noqa: E501

        :return: The activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: dict(str, DestinyHistoricalStatsDefinitionsDestinyActivityModeType)
        """
        return self._activity_mode_mappings

    @activity_mode_mappings.setter
    def activity_mode_mappings(self, activity_mode_mappings):
        """Sets the activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.

        If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played.  # noqa: E501

        :param activity_mode_mappings: The activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: dict(str, DestinyHistoricalStatsDefinitionsDestinyActivityModeType)
        """

        self._activity_mode_mappings = activity_mode_mappings

    @property
    def display(self):
        """Gets the display of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose.  # noqa: E501

        :return: The display of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this DestinyDefinitionsDestinyActivityModeDefinition.

        If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose.  # noqa: E501

        :param display: The display of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: bool
        """

        self._display = display

    @property
    def order(self):
        """Gets the order of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The relative ordering of activity modes.  # noqa: E501

        :return: The order of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DestinyDefinitionsDestinyActivityModeDefinition.

        The relative ordering of activity modes.  # noqa: E501

        :param order: The order of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def hash(self):
        """Gets the hash of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyDefinitionsDestinyActivityModeDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyDefinitionsDestinyActivityModeDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyDefinitionsDestinyActivityModeDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyDefinitionsDestinyActivityModeDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyDefinitionsDestinyActivityModeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
