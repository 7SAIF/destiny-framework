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


class DestinyItemComponentSetint32(object):
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
        'instances': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemInstanceComponent',
        'objectives': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemObjectivesComponent',
        'perks': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemPerksComponent',
        'render_data': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemRenderComponent',
        'stats': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemStatsComponent',
        'sockets': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemSocketsComponent',
        'talent_grids': 'DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemTalentGridComponent',
        'plug_states': 'DictionaryComponentResponseuint32DestinyComponentsItemsDestinyItemPlugComponent'
    }

    attribute_map = {
        'instances': 'instances',
        'objectives': 'objectives',
        'perks': 'perks',
        'render_data': 'renderData',
        'stats': 'stats',
        'sockets': 'sockets',
        'talent_grids': 'talentGrids',
        'plug_states': 'plugStates'
    }

    def __init__(self, instances=None, objectives=None, perks=None, render_data=None, stats=None, sockets=None, talent_grids=None, plug_states=None):
        """
        DestinyItemComponentSetint32 - a model defined in Swagger
        """

        self._instances = None
        self._objectives = None
        self._perks = None
        self._render_data = None
        self._stats = None
        self._sockets = None
        self._talent_grids = None
        self._plug_states = None

        if instances is not None:
          self.instances = instances
        if objectives is not None:
          self.objectives = objectives
        if perks is not None:
          self.perks = perks
        if render_data is not None:
          self.render_data = render_data
        if stats is not None:
          self.stats = stats
        if sockets is not None:
          self.sockets = sockets
        if talent_grids is not None:
          self.talent_grids = talent_grids
        if plug_states is not None:
          self.plug_states = plug_states

    @property
    def instances(self):
        """
        Gets the instances of this DestinyItemComponentSetint32.

        :return: The instances of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemInstanceComponent
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this DestinyItemComponentSetint32.

        :param instances: The instances of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemInstanceComponent
        """

        self._instances = instances

    @property
    def objectives(self):
        """
        Gets the objectives of this DestinyItemComponentSetint32.

        :return: The objectives of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemObjectivesComponent
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives):
        """
        Sets the objectives of this DestinyItemComponentSetint32.

        :param objectives: The objectives of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemObjectivesComponent
        """

        self._objectives = objectives

    @property
    def perks(self):
        """
        Gets the perks of this DestinyItemComponentSetint32.

        :return: The perks of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemPerksComponent
        """
        return self._perks

    @perks.setter
    def perks(self, perks):
        """
        Sets the perks of this DestinyItemComponentSetint32.

        :param perks: The perks of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemPerksComponent
        """

        self._perks = perks

    @property
    def render_data(self):
        """
        Gets the render_data of this DestinyItemComponentSetint32.

        :return: The render_data of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemRenderComponent
        """
        return self._render_data

    @render_data.setter
    def render_data(self, render_data):
        """
        Sets the render_data of this DestinyItemComponentSetint32.

        :param render_data: The render_data of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemRenderComponent
        """

        self._render_data = render_data

    @property
    def stats(self):
        """
        Gets the stats of this DestinyItemComponentSetint32.

        :return: The stats of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemStatsComponent
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this DestinyItemComponentSetint32.

        :param stats: The stats of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemStatsComponent
        """

        self._stats = stats

    @property
    def sockets(self):
        """
        Gets the sockets of this DestinyItemComponentSetint32.

        :return: The sockets of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemSocketsComponent
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """
        Sets the sockets of this DestinyItemComponentSetint32.

        :param sockets: The sockets of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemSocketsComponent
        """

        self._sockets = sockets

    @property
    def talent_grids(self):
        """
        Gets the talent_grids of this DestinyItemComponentSetint32.

        :return: The talent_grids of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemTalentGridComponent
        """
        return self._talent_grids

    @talent_grids.setter
    def talent_grids(self, talent_grids):
        """
        Sets the talent_grids of this DestinyItemComponentSetint32.

        :param talent_grids: The talent_grids of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseint32DestinyEntitiesItemsDestinyItemTalentGridComponent
        """

        self._talent_grids = talent_grids

    @property
    def plug_states(self):
        """
        Gets the plug_states of this DestinyItemComponentSetint32.

        :return: The plug_states of this DestinyItemComponentSetint32.
        :rtype: DictionaryComponentResponseuint32DestinyComponentsItemsDestinyItemPlugComponent
        """
        return self._plug_states

    @plug_states.setter
    def plug_states(self, plug_states):
        """
        Sets the plug_states of this DestinyItemComponentSetint32.

        :param plug_states: The plug_states of this DestinyItemComponentSetint32.
        :type: DictionaryComponentResponseuint32DestinyComponentsItemsDestinyItemPlugComponent
        """

        self._plug_states = plug_states

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
        if not isinstance(other, DestinyItemComponentSetint32):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other