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


class DestinyDefinitionsDestinyNodeStepDefinition(object):
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
        'step_index': 'int',
        'node_step_hash': 'int',
        'interaction_description': 'str',
        'damage_type_hash': 'int',
        'can_activate_next_step': 'bool',
        'next_step_index': 'int',
        'is_next_step_random': 'bool',
        'perk_hashes': 'list[int]',
        'start_progression_bar_at_progress': 'int',
        'stat_hashes': 'list[int]',
        'affects_quality': 'bool',
        'affects_level': 'bool',
        'socket_replacements': 'list[DestinyDefinitionsDestinyNodeSocketReplaceResponse]'
    }

    attribute_map = {
        'step_index': 'stepIndex',
        'node_step_hash': 'nodeStepHash',
        'interaction_description': 'interactionDescription',
        'damage_type_hash': 'damageTypeHash',
        'can_activate_next_step': 'canActivateNextStep',
        'next_step_index': 'nextStepIndex',
        'is_next_step_random': 'isNextStepRandom',
        'perk_hashes': 'perkHashes',
        'start_progression_bar_at_progress': 'startProgressionBarAtProgress',
        'stat_hashes': 'statHashes',
        'affects_quality': 'affectsQuality',
        'affects_level': 'affectsLevel',
        'socket_replacements': 'socketReplacements'
    }

    def __init__(self, step_index=None, node_step_hash=None, interaction_description=None, damage_type_hash=None, can_activate_next_step=None, next_step_index=None, is_next_step_random=None, perk_hashes=None, start_progression_bar_at_progress=None, stat_hashes=None, affects_quality=None, affects_level=None, socket_replacements=None):
        """
        DestinyDefinitionsDestinyNodeStepDefinition - a model defined in Swagger
        """

        self._step_index = None
        self._node_step_hash = None
        self._interaction_description = None
        self._damage_type_hash = None
        self._can_activate_next_step = None
        self._next_step_index = None
        self._is_next_step_random = None
        self._perk_hashes = None
        self._start_progression_bar_at_progress = None
        self._stat_hashes = None
        self._affects_quality = None
        self._affects_level = None
        self._socket_replacements = None

        if step_index is not None:
          self.step_index = step_index
        if node_step_hash is not None:
          self.node_step_hash = node_step_hash
        if interaction_description is not None:
          self.interaction_description = interaction_description
        if damage_type_hash is not None:
          self.damage_type_hash = damage_type_hash
        if can_activate_next_step is not None:
          self.can_activate_next_step = can_activate_next_step
        if next_step_index is not None:
          self.next_step_index = next_step_index
        if is_next_step_random is not None:
          self.is_next_step_random = is_next_step_random
        if perk_hashes is not None:
          self.perk_hashes = perk_hashes
        if start_progression_bar_at_progress is not None:
          self.start_progression_bar_at_progress = start_progression_bar_at_progress
        if stat_hashes is not None:
          self.stat_hashes = stat_hashes
        if affects_quality is not None:
          self.affects_quality = affects_quality
        if affects_level is not None:
          self.affects_level = affects_level
        if socket_replacements is not None:
          self.socket_replacements = socket_replacements

    @property
    def step_index(self):
        """
        Gets the step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        The index of this step in the list of Steps on the Talent Node.    Unfortunately, this is the closest thing we have to an identifier for the Step:  steps are not provided a content version agnostic identifier.  This means that,  when you are dealing with talent nodes, you will need to first ensure that you have  the latest version of content.

        :return: The step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: int
        """
        return self._step_index

    @step_index.setter
    def step_index(self, step_index):
        """
        Sets the step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        The index of this step in the list of Steps on the Talent Node.    Unfortunately, this is the closest thing we have to an identifier for the Step:  steps are not provided a content version agnostic identifier.  This means that,  when you are dealing with talent nodes, you will need to first ensure that you have  the latest version of content.

        :param step_index: The step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: int
        """

        self._step_index = step_index

    @property
    def node_step_hash(self):
        """
        Gets the node_step_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        The hash of this node step.  Unfortunately, while it can be used to uniquely identify  the step within a node, it is also content version dependent and should not be relied on  without ensuring you have the latest vesion of content.

        :return: The node_step_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: int
        """
        return self._node_step_hash

    @node_step_hash.setter
    def node_step_hash(self, node_step_hash):
        """
        Sets the node_step_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        The hash of this node step.  Unfortunately, while it can be used to uniquely identify  the step within a node, it is also content version dependent and should not be relied on  without ensuring you have the latest vesion of content.

        :param node_step_hash: The node_step_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: int
        """

        self._node_step_hash = node_step_hash

    @property
    def interaction_description(self):
        """
        Gets the interaction_description of this DestinyDefinitionsDestinyNodeStepDefinition.
        If you can interact with this node in some way, this is the localized description  of that interaction.

        :return: The interaction_description of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: str
        """
        return self._interaction_description

    @interaction_description.setter
    def interaction_description(self, interaction_description):
        """
        Sets the interaction_description of this DestinyDefinitionsDestinyNodeStepDefinition.
        If you can interact with this node in some way, this is the localized description  of that interaction.

        :param interaction_description: The interaction_description of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: str
        """

        self._interaction_description = interaction_description

    @property
    def damage_type_hash(self):
        """
        Gets the damage_type_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        If the step provides a damage type, this will be the hash identifier used to look up  the damage type's DestinyDamageTypeDefinition.

        :return: The damage_type_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: int
        """
        return self._damage_type_hash

    @damage_type_hash.setter
    def damage_type_hash(self, damage_type_hash):
        """
        Sets the damage_type_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        If the step provides a damage type, this will be the hash identifier used to look up  the damage type's DestinyDamageTypeDefinition.

        :param damage_type_hash: The damage_type_hash of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: int
        """

        self._damage_type_hash = damage_type_hash

    @property
    def can_activate_next_step(self):
        """
        Gets the can_activate_next_step of this DestinyDefinitionsDestinyNodeStepDefinition.
        There was a time when talent nodes could be activated multiple times, and  the effects of subsequent Steps would be compounded on each other, essentially  \"upgrading\" the node.  We have moved away from this, but theoretically the capability  still exists.    I continue to return this in case it is used in the future: if true and  this step is the current step in the node, you are allowed to activate the node  a second time to receive the benefits of the next step in the node, which will then  become the active step.

        :return: The can_activate_next_step of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: bool
        """
        return self._can_activate_next_step

    @can_activate_next_step.setter
    def can_activate_next_step(self, can_activate_next_step):
        """
        Sets the can_activate_next_step of this DestinyDefinitionsDestinyNodeStepDefinition.
        There was a time when talent nodes could be activated multiple times, and  the effects of subsequent Steps would be compounded on each other, essentially  \"upgrading\" the node.  We have moved away from this, but theoretically the capability  still exists.    I continue to return this in case it is used in the future: if true and  this step is the current step in the node, you are allowed to activate the node  a second time to receive the benefits of the next step in the node, which will then  become the active step.

        :param can_activate_next_step: The can_activate_next_step of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: bool
        """

        self._can_activate_next_step = can_activate_next_step

    @property
    def next_step_index(self):
        """
        Gets the next_step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        The stepIndex of the next step in the talent node, or -1 if this is the last step or if  the next step to be chosen is random.    This doesn't really matter anymore unless canActivateNextStep begins to be used again.

        :return: The next_step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: int
        """
        return self._next_step_index

    @next_step_index.setter
    def next_step_index(self, next_step_index):
        """
        Sets the next_step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        The stepIndex of the next step in the talent node, or -1 if this is the last step or if  the next step to be chosen is random.    This doesn't really matter anymore unless canActivateNextStep begins to be used again.

        :param next_step_index: The next_step_index of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: int
        """

        self._next_step_index = next_step_index

    @property
    def is_next_step_random(self):
        """
        Gets the is_next_step_random of this DestinyDefinitionsDestinyNodeStepDefinition.
        If true, the next step to be chosen is random, and if you're allowed to activate the  next step. (if canActivateNextStep = true)

        :return: The is_next_step_random of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: bool
        """
        return self._is_next_step_random

    @is_next_step_random.setter
    def is_next_step_random(self, is_next_step_random):
        """
        Sets the is_next_step_random of this DestinyDefinitionsDestinyNodeStepDefinition.
        If true, the next step to be chosen is random, and if you're allowed to activate the  next step. (if canActivateNextStep = true)

        :param is_next_step_random: The is_next_step_random of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: bool
        """

        self._is_next_step_random = is_next_step_random

    @property
    def perk_hashes(self):
        """
        Gets the perk_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied  when this step is active.  Perks provide a variety of benefits and modifications - examine  DestinySandboxPerkDefinition to learn more.

        :return: The perk_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: list[int]
        """
        return self._perk_hashes

    @perk_hashes.setter
    def perk_hashes(self, perk_hashes):
        """
        Sets the perk_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied  when this step is active.  Perks provide a variety of benefits and modifications - examine  DestinySandboxPerkDefinition to learn more.

        :param perk_hashes: The perk_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: list[int]
        """

        self._perk_hashes = perk_hashes

    @property
    def start_progression_bar_at_progress(self):
        """
        Gets the start_progression_bar_at_progress of this DestinyDefinitionsDestinyNodeStepDefinition.
        When the Talent Grid's progression reaches this value, the circular \"progress bar\" that  surrounds the talent node should be shown.    This also indicates the lower bound of said  progress bar, with the upper bound being the progress required to reach   activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put  it in the definition to save people time)

        :return: The start_progression_bar_at_progress of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: int
        """
        return self._start_progression_bar_at_progress

    @start_progression_bar_at_progress.setter
    def start_progression_bar_at_progress(self, start_progression_bar_at_progress):
        """
        Sets the start_progression_bar_at_progress of this DestinyDefinitionsDestinyNodeStepDefinition.
        When the Talent Grid's progression reaches this value, the circular \"progress bar\" that  surrounds the talent node should be shown.    This also indicates the lower bound of said  progress bar, with the upper bound being the progress required to reach   activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put  it in the definition to save people time)

        :param start_progression_bar_at_progress: The start_progression_bar_at_progress of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: int
        """

        self._start_progression_bar_at_progress = start_progression_bar_at_progress

    @property
    def stat_hashes(self):
        """
        Gets the stat_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        When the step provides stat benefits on the item or character, this is the list of hash identifiers  for stats (DestinyStatDefinition) that are provided.

        :return: The stat_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: list[int]
        """
        return self._stat_hashes

    @stat_hashes.setter
    def stat_hashes(self, stat_hashes):
        """
        Sets the stat_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        When the step provides stat benefits on the item or character, this is the list of hash identifiers  for stats (DestinyStatDefinition) that are provided.

        :param stat_hashes: The stat_hashes of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: list[int]
        """

        self._stat_hashes = stat_hashes

    @property
    def affects_quality(self):
        """
        Gets the affects_quality of this DestinyDefinitionsDestinyNodeStepDefinition.
        If this is true, the step affects the item's Quality in some way.  See DestinyInventoryItemDefinition  for more information about the meaning of Quality.  I already made a joke about Zen and the Art of  Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again.  Oops too late

        :return: The affects_quality of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: bool
        """
        return self._affects_quality

    @affects_quality.setter
    def affects_quality(self, affects_quality):
        """
        Sets the affects_quality of this DestinyDefinitionsDestinyNodeStepDefinition.
        If this is true, the step affects the item's Quality in some way.  See DestinyInventoryItemDefinition  for more information about the meaning of Quality.  I already made a joke about Zen and the Art of  Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again.  Oops too late

        :param affects_quality: The affects_quality of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: bool
        """

        self._affects_quality = affects_quality

    @property
    def affects_level(self):
        """
        Gets the affects_level of this DestinyDefinitionsDestinyNodeStepDefinition.
        If true, this step can affect the level of the item.  See DestinyInventoryItemDefintion for more  information about item levels and their effect on stats.

        :return: The affects_level of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: bool
        """
        return self._affects_level

    @affects_level.setter
    def affects_level(self, affects_level):
        """
        Sets the affects_level of this DestinyDefinitionsDestinyNodeStepDefinition.
        If true, this step can affect the level of the item.  See DestinyInventoryItemDefintion for more  information about item levels and their effect on stats.

        :param affects_level: The affects_level of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: bool
        """

        self._affects_level = affects_level

    @property
    def socket_replacements(self):
        """
        Gets the socket_replacements of this DestinyDefinitionsDestinyNodeStepDefinition.
        If this step is activated, this will be a list of information used to replace socket items  with new Plugs.  See DestinyInventoryItemDefinition for more information about sockets and plugs.

        :return: The socket_replacements of this DestinyDefinitionsDestinyNodeStepDefinition.
        :rtype: list[DestinyDefinitionsDestinyNodeSocketReplaceResponse]
        """
        return self._socket_replacements

    @socket_replacements.setter
    def socket_replacements(self, socket_replacements):
        """
        Sets the socket_replacements of this DestinyDefinitionsDestinyNodeStepDefinition.
        If this step is activated, this will be a list of information used to replace socket items  with new Plugs.  See DestinyInventoryItemDefinition for more information about sockets and plugs.

        :param socket_replacements: The socket_replacements of this DestinyDefinitionsDestinyNodeStepDefinition.
        :type: list[DestinyDefinitionsDestinyNodeSocketReplaceResponse]
        """

        self._socket_replacements = socket_replacements

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
        if not isinstance(other, DestinyDefinitionsDestinyNodeStepDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
