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


class DestinyDefinitionsDestinyDestinationDefinition(object):
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
        'display_properties': 'DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition',
        'place_hash': 'int',
        'default_freeroam_activity_hash': 'int',
        'activity_graph_entries': 'list[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]',
        'bubble_settings': 'list[DestinyDefinitionsDestinyDestinationBubbleSettingDefinition]',
        'bubbles': 'list[DestinyDefinitionsDestinyBubbleDefinition]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'place_hash': 'placeHash',
        'default_freeroam_activity_hash': 'defaultFreeroamActivityHash',
        'activity_graph_entries': 'activityGraphEntries',
        'bubble_settings': 'bubbleSettings',
        'bubbles': 'bubbles',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, place_hash=None, default_freeroam_activity_hash=None, activity_graph_entries=None, bubble_settings=None, bubbles=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyDestinationDefinition - a model defined in Swagger
        """

        self._display_properties = None
        self._place_hash = None
        self._default_freeroam_activity_hash = None
        self._activity_graph_entries = None
        self._bubble_settings = None
        self._bubbles = None
        self._hash = None
        self._index = None
        self._redacted = None

        if display_properties is not None:
          self.display_properties = display_properties
        if place_hash is not None:
          self.place_hash = place_hash
        if default_freeroam_activity_hash is not None:
          self.default_freeroam_activity_hash = default_freeroam_activity_hash
        if activity_graph_entries is not None:
          self.activity_graph_entries = activity_graph_entries
        if bubble_settings is not None:
          self.bubble_settings = bubble_settings
        if bubbles is not None:
          self.bubbles = bubbles
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def display_properties(self):
        """
        Gets the display_properties of this DestinyDefinitionsDestinyDestinationDefinition.

        :return: The display_properties of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this DestinyDefinitionsDestinyDestinationDefinition.

        :param display_properties: The display_properties of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def place_hash(self):
        """
        Gets the place_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        The place that \"owns\" this Destination.  Use this hash to look up the DestinyPlaceDefinition.

        :return: The place_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: int
        """
        return self._place_hash

    @place_hash.setter
    def place_hash(self, place_hash):
        """
        Sets the place_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        The place that \"owns\" this Destination.  Use this hash to look up the DestinyPlaceDefinition.

        :param place_hash: The place_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: int
        """

        self._place_hash = place_hash

    @property
    def default_freeroam_activity_hash(self):
        """
        Gets the default_freeroam_activity_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        If this Destination has a default Free-Roam activity, this is the hash for that Activity.  Use it to look up the DestinyActivityDefintion.

        :return: The default_freeroam_activity_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: int
        """
        return self._default_freeroam_activity_hash

    @default_freeroam_activity_hash.setter
    def default_freeroam_activity_hash(self, default_freeroam_activity_hash):
        """
        Sets the default_freeroam_activity_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        If this Destination has a default Free-Roam activity, this is the hash for that Activity.  Use it to look up the DestinyActivityDefintion.

        :param default_freeroam_activity_hash: The default_freeroam_activity_hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: int
        """

        self._default_freeroam_activity_hash = default_freeroam_activity_hash

    @property
    def activity_graph_entries(self):
        """
        Gets the activity_graph_entries of this DestinyDefinitionsDestinyDestinationDefinition.
        If the Destination has default Activity Graphs (i.e. \"Map\") that should be shown  in the director, this is the list of those Graphs.  At most, only one should be active  at any given time for a Destination: these would represent, for example, different  variants on a Map if the Destination is changing on a macro level based on game state.

        :return: The activity_graph_entries of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: list[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]
        """
        return self._activity_graph_entries

    @activity_graph_entries.setter
    def activity_graph_entries(self, activity_graph_entries):
        """
        Sets the activity_graph_entries of this DestinyDefinitionsDestinyDestinationDefinition.
        If the Destination has default Activity Graphs (i.e. \"Map\") that should be shown  in the director, this is the list of those Graphs.  At most, only one should be active  at any given time for a Destination: these would represent, for example, different  variants on a Map if the Destination is changing on a macro level based on game state.

        :param activity_graph_entries: The activity_graph_entries of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: list[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]
        """

        self._activity_graph_entries = activity_graph_entries

    @property
    def bubble_settings(self):
        """
        Gets the bubble_settings of this DestinyDefinitionsDestinyDestinationDefinition.
        A Destination may have many \"Bubbles\" zones with human readable properties.    We don't get as much info as I'd like about them - I'd love to return info like   where on the map they are located - but at least this gives you the name of those bubbles.  bubbleSettings and bubbles both have the identical number of entries, and you should  match up their indexes to provide matching bubble and bubbleSettings data.

        :return: The bubble_settings of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: list[DestinyDefinitionsDestinyDestinationBubbleSettingDefinition]
        """
        return self._bubble_settings

    @bubble_settings.setter
    def bubble_settings(self, bubble_settings):
        """
        Sets the bubble_settings of this DestinyDefinitionsDestinyDestinationDefinition.
        A Destination may have many \"Bubbles\" zones with human readable properties.    We don't get as much info as I'd like about them - I'd love to return info like   where on the map they are located - but at least this gives you the name of those bubbles.  bubbleSettings and bubbles both have the identical number of entries, and you should  match up their indexes to provide matching bubble and bubbleSettings data.

        :param bubble_settings: The bubble_settings of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: list[DestinyDefinitionsDestinyDestinationBubbleSettingDefinition]
        """

        self._bubble_settings = bubble_settings

    @property
    def bubbles(self):
        """
        Gets the bubbles of this DestinyDefinitionsDestinyDestinationDefinition.
        This provides the unique identifiers for every bubble in the destination  (only guaranteed unique within the destination), and any intrinsic properties of the bubble.    bubbleSettings and bubbles both have the identical number of entries, and you should  match up their indexes to provide matching bubble and bubbleSettings data.

        :return: The bubbles of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: list[DestinyDefinitionsDestinyBubbleDefinition]
        """
        return self._bubbles

    @bubbles.setter
    def bubbles(self, bubbles):
        """
        Sets the bubbles of this DestinyDefinitionsDestinyDestinationDefinition.
        This provides the unique identifiers for every bubble in the destination  (only guaranteed unique within the destination), and any intrinsic properties of the bubble.    bubbleSettings and bubbles both have the identical number of entries, and you should  match up their indexes to provide matching bubble and bubbleSettings data.

        :param bubbles: The bubbles of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: list[DestinyDefinitionsDestinyBubbleDefinition]
        """

        self._bubbles = bubbles

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyDestinationDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.    When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyDestinationDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.    When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyDestinationDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyDestinationDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyDestinationDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyDestinationDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet is  not yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyDestinationDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyDestinationDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet is  not yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyDestinationDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinyDestinationDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
