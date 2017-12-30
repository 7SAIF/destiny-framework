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

from swagger_client.models.destiny_definitions_destiny_node_step_definition import DestinyDefinitionsDestinyNodeStepDefinition  # noqa: F401,E501


class DestinyDefinitionsDestinyTalentNodeDefinition(object):
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
        'node_index': 'int',
        'node_hash': 'int',
        'row': 'int',
        'column': 'int',
        'prerequisite_node_indexes': 'list[int]',
        'binary_pair_node_index': 'int',
        'auto_unlocks': 'bool',
        'last_step_repeats': 'bool',
        'is_random': 'bool',
        'random_activation_requirement': 'object',
        'is_random_repurchasable': 'bool',
        'steps': 'list[DestinyDefinitionsDestinyNodeStepDefinition]',
        'exclusive_with_node_hashes': 'list[int]',
        'random_start_progression_bar_at_progression': 'int',
        'layout_identifier': 'str',
        'group_hash': 'int',
        'lore_hash': 'int',
        'node_style_identifier': 'str',
        'ignore_for_completion': 'bool'
    }

    attribute_map = {
        'node_index': 'nodeIndex',
        'node_hash': 'nodeHash',
        'row': 'row',
        'column': 'column',
        'prerequisite_node_indexes': 'prerequisiteNodeIndexes',
        'binary_pair_node_index': 'binaryPairNodeIndex',
        'auto_unlocks': 'autoUnlocks',
        'last_step_repeats': 'lastStepRepeats',
        'is_random': 'isRandom',
        'random_activation_requirement': 'randomActivationRequirement',
        'is_random_repurchasable': 'isRandomRepurchasable',
        'steps': 'steps',
        'exclusive_with_node_hashes': 'exclusiveWithNodeHashes',
        'random_start_progression_bar_at_progression': 'randomStartProgressionBarAtProgression',
        'layout_identifier': 'layoutIdentifier',
        'group_hash': 'groupHash',
        'lore_hash': 'loreHash',
        'node_style_identifier': 'nodeStyleIdentifier',
        'ignore_for_completion': 'ignoreForCompletion'
    }

    def __init__(self, node_index=None, node_hash=None, row=None, column=None, prerequisite_node_indexes=None, binary_pair_node_index=None, auto_unlocks=None, last_step_repeats=None, is_random=None, random_activation_requirement=None, is_random_repurchasable=None, steps=None, exclusive_with_node_hashes=None, random_start_progression_bar_at_progression=None, layout_identifier=None, group_hash=None, lore_hash=None, node_style_identifier=None, ignore_for_completion=None):  # noqa: E501
        """DestinyDefinitionsDestinyTalentNodeDefinition - a model defined in Swagger"""  # noqa: E501

        self._node_index = None
        self._node_hash = None
        self._row = None
        self._column = None
        self._prerequisite_node_indexes = None
        self._binary_pair_node_index = None
        self._auto_unlocks = None
        self._last_step_repeats = None
        self._is_random = None
        self._random_activation_requirement = None
        self._is_random_repurchasable = None
        self._steps = None
        self._exclusive_with_node_hashes = None
        self._random_start_progression_bar_at_progression = None
        self._layout_identifier = None
        self._group_hash = None
        self._lore_hash = None
        self._node_style_identifier = None
        self._ignore_for_completion = None
        self.discriminator = None

        if node_index is not None:
            self.node_index = node_index
        if node_hash is not None:
            self.node_hash = node_hash
        if row is not None:
            self.row = row
        if column is not None:
            self.column = column
        if prerequisite_node_indexes is not None:
            self.prerequisite_node_indexes = prerequisite_node_indexes
        if binary_pair_node_index is not None:
            self.binary_pair_node_index = binary_pair_node_index
        if auto_unlocks is not None:
            self.auto_unlocks = auto_unlocks
        if last_step_repeats is not None:
            self.last_step_repeats = last_step_repeats
        if is_random is not None:
            self.is_random = is_random
        if random_activation_requirement is not None:
            self.random_activation_requirement = random_activation_requirement
        if is_random_repurchasable is not None:
            self.is_random_repurchasable = is_random_repurchasable
        if steps is not None:
            self.steps = steps
        if exclusive_with_node_hashes is not None:
            self.exclusive_with_node_hashes = exclusive_with_node_hashes
        if random_start_progression_bar_at_progression is not None:
            self.random_start_progression_bar_at_progression = random_start_progression_bar_at_progression
        if layout_identifier is not None:
            self.layout_identifier = layout_identifier
        if group_hash is not None:
            self.group_hash = group_hash
        if lore_hash is not None:
            self.lore_hash = lore_hash
        if node_style_identifier is not None:
            self.node_style_identifier = node_style_identifier
        if ignore_for_completion is not None:
            self.ignore_for_completion = ignore_for_completion

    @property
    def node_index(self):
        """Gets the node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        The index into the DestinyTalentGridDefinition's \"nodes\" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.  # noqa: E501

        :return: The node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._node_index

    @node_index.setter
    def node_index(self, node_index):
        """Sets the node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.

        The index into the DestinyTalentGridDefinition's \"nodes\" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.  # noqa: E501

        :param node_index: The node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._node_index = node_index

    @property
    def node_hash(self):
        """Gets the node_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.  The two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!  # noqa: E501

        :return: The node_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._node_hash

    @node_hash.setter
    def node_hash(self, node_hash):
        """Sets the node_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.

        The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.  The two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!  # noqa: E501

        :param node_hash: The node_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._node_hash = node_hash

    @property
    def row(self):
        """Gets the row of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        The visual \"row\" where the node should be shown in the UI. If negative, then the node is hidden.  # noqa: E501

        :return: The row of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this DestinyDefinitionsDestinyTalentNodeDefinition.

        The visual \"row\" where the node should be shown in the UI. If negative, then the node is hidden.  # noqa: E501

        :param row: The row of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._row = row

    @property
    def column(self):
        """Gets the column of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        The visual \"column\" where the node should be shown in the UI. If negative, the node is hidden.  # noqa: E501

        :return: The column of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this DestinyDefinitionsDestinyTalentNodeDefinition.

        The visual \"column\" where the node should be shown in the UI. If negative, the node is hidden.  # noqa: E501

        :param column: The column of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._column = column

    @property
    def prerequisite_node_indexes(self):
        """Gets the prerequisite_node_indexes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.  I would have liked to change this to hashes for Destiny 2, but we have run out of time.  # noqa: E501

        :return: The prerequisite_node_indexes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._prerequisite_node_indexes

    @prerequisite_node_indexes.setter
    def prerequisite_node_indexes(self, prerequisite_node_indexes):
        """Sets the prerequisite_node_indexes of this DestinyDefinitionsDestinyTalentNodeDefinition.

        Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.  I would have liked to change this to hashes for Destiny 2, but we have run out of time.  # noqa: E501

        :param prerequisite_node_indexes: The prerequisite_node_indexes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: list[int]
        """

        self._prerequisite_node_indexes = prerequisite_node_indexes

    @property
    def binary_pair_node_index(self):
        """Gets the binary_pair_node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        At one point, Talent Nodes supported the idea of \"Binary Pairs\": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.  If this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.  # noqa: E501

        :return: The binary_pair_node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._binary_pair_node_index

    @binary_pair_node_index.setter
    def binary_pair_node_index(self, binary_pair_node_index):
        """Sets the binary_pair_node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.

        At one point, Talent Nodes supported the idea of \"Binary Pairs\": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.  If this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.  # noqa: E501

        :param binary_pair_node_index: The binary_pair_node_index of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._binary_pair_node_index = binary_pair_node_index

    @property
    def auto_unlocks(self):
        """Gets the auto_unlocks of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.  # noqa: E501

        :return: The auto_unlocks of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._auto_unlocks

    @auto_unlocks.setter
    def auto_unlocks(self, auto_unlocks):
        """Sets the auto_unlocks of this DestinyDefinitionsDestinyTalentNodeDefinition.

        If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.  # noqa: E501

        :param auto_unlocks: The auto_unlocks of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._auto_unlocks = auto_unlocks

    @property
    def last_step_repeats(self):
        """Gets the last_step_repeats of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times.   This is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.  # noqa: E501

        :return: The last_step_repeats of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._last_step_repeats

    @last_step_repeats.setter
    def last_step_repeats(self, last_step_repeats):
        """Sets the last_step_repeats of this DestinyDefinitionsDestinyTalentNodeDefinition.

        At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times.   This is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.  # noqa: E501

        :param last_step_repeats: The last_step_repeats of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._last_step_repeats = last_step_repeats

    @property
    def is_random(self):
        """Gets the is_random of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        If this is true, the node's step is determined randomly rather than the first step being chosen.  # noqa: E501

        :return: The is_random of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_random

    @is_random.setter
    def is_random(self, is_random):
        """Sets the is_random of this DestinyDefinitionsDestinyTalentNodeDefinition.

        If this is true, the node's step is determined randomly rather than the first step being chosen.  # noqa: E501

        :param is_random: The is_random of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._is_random = is_random

    @property
    def random_activation_requirement(self):
        """Gets the random_activation_requirement of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        At one point, you were going to be able to repurchase talent nodes that had random steps, to \"re-roll\" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.  The system still exists to do this, as far as I know, so it may yet come back around!  # noqa: E501

        :return: The random_activation_requirement of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: object
        """
        return self._random_activation_requirement

    @random_activation_requirement.setter
    def random_activation_requirement(self, random_activation_requirement):
        """Sets the random_activation_requirement of this DestinyDefinitionsDestinyTalentNodeDefinition.

        At one point, you were going to be able to repurchase talent nodes that had random steps, to \"re-roll\" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.  The system still exists to do this, as far as I know, so it may yet come back around!  # noqa: E501

        :param random_activation_requirement: The random_activation_requirement of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: object
        """

        self._random_activation_requirement = random_activation_requirement

    @property
    def is_random_repurchasable(self):
        """Gets the is_random_repurchasable of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        If this is true, the node can be \"re-rolled\" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.  # noqa: E501

        :return: The is_random_repurchasable of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_random_repurchasable

    @is_random_repurchasable.setter
    def is_random_repurchasable(self, is_random_repurchasable):
        """Sets the is_random_repurchasable of this DestinyDefinitionsDestinyTalentNodeDefinition.

        If this is true, the node can be \"re-rolled\" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.  # noqa: E501

        :param is_random_repurchasable: The is_random_repurchasable of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._is_random_repurchasable = is_random_repurchasable

    @property
    def steps(self):
        """Gets the steps of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        At this point, \"steps\" have been obfuscated into conceptual entities, aggregating the underlying notions of \"properties\" and \"true steps\".  If you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the \"realSteps\" property below.  # noqa: E501

        :return: The steps of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: list[DestinyDefinitionsDestinyNodeStepDefinition]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this DestinyDefinitionsDestinyTalentNodeDefinition.

        At this point, \"steps\" have been obfuscated into conceptual entities, aggregating the underlying notions of \"properties\" and \"true steps\".  If you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the \"realSteps\" property below.  # noqa: E501

        :param steps: The steps of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: list[DestinyDefinitionsDestinyNodeStepDefinition]
        """

        self._steps = steps

    @property
    def exclusive_with_node_hashes(self):
        """Gets the exclusive_with_node_hashes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        The nodeHash values for nodes that are in an Exclusive Set with this node.  See DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.  Again, note that these are nodeHashes and *not* nodeIndexes.  # noqa: E501

        :return: The exclusive_with_node_hashes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._exclusive_with_node_hashes

    @exclusive_with_node_hashes.setter
    def exclusive_with_node_hashes(self, exclusive_with_node_hashes):
        """Sets the exclusive_with_node_hashes of this DestinyDefinitionsDestinyTalentNodeDefinition.

        The nodeHash values for nodes that are in an Exclusive Set with this node.  See DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.  Again, note that these are nodeHashes and *not* nodeIndexes.  # noqa: E501

        :param exclusive_with_node_hashes: The exclusive_with_node_hashes of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: list[int]
        """

        self._exclusive_with_node_hashes = exclusive_with_node_hashes

    @property
    def random_start_progression_bar_at_progression(self):
        """Gets the random_start_progression_bar_at_progression of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.  # noqa: E501

        :return: The random_start_progression_bar_at_progression of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._random_start_progression_bar_at_progression

    @random_start_progression_bar_at_progression.setter
    def random_start_progression_bar_at_progression(self, random_start_progression_bar_at_progression):
        """Sets the random_start_progression_bar_at_progression of this DestinyDefinitionsDestinyTalentNodeDefinition.

        If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.  # noqa: E501

        :param random_start_progression_bar_at_progression: The random_start_progression_bar_at_progression of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._random_start_progression_bar_at_progression = random_start_progression_bar_at_progression

    @property
    def layout_identifier(self):
        """Gets the layout_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.  # noqa: E501

        :return: The layout_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._layout_identifier

    @layout_identifier.setter
    def layout_identifier(self, layout_identifier):
        """Sets the layout_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.

        A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.  # noqa: E501

        :param layout_identifier: The layout_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: str
        """

        self._layout_identifier = layout_identifier

    @property
    def group_hash(self):
        """Gets the group_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        As of Destiny 2, nodes can exist as part of \"Exclusive Groups\". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause \"opposing\" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.  See DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one.  # noqa: E501

        :return: The group_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._group_hash

    @group_hash.setter
    def group_hash(self, group_hash):
        """Sets the group_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.

        As of Destiny 2, nodes can exist as part of \"Exclusive Groups\". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause \"opposing\" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.  See DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one.  # noqa: E501

        :param group_hash: The group_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._group_hash = group_hash

    @property
    def lore_hash(self):
        """Gets the lore_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.  # noqa: E501

        :return: The lore_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._lore_hash

    @lore_hash.setter
    def lore_hash(self, lore_hash):
        """Sets the lore_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.

        Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.  # noqa: E501

        :param lore_hash: The lore_hash of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: int
        """

        self._lore_hash = lore_hash

    @property
    def node_style_identifier(self):
        """Gets the node_style_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.  # noqa: E501

        :return: The node_style_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._node_style_identifier

    @node_style_identifier.setter
    def node_style_identifier(self, node_style_identifier):
        """Sets the node_style_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.

        Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.  # noqa: E501

        :param node_style_identifier: The node_style_identifier of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: str
        """

        self._node_style_identifier = node_style_identifier

    @property
    def ignore_for_completion(self):
        """Gets the ignore_for_completion of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501

        Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.  # noqa: E501

        :return: The ignore_for_completion of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_for_completion

    @ignore_for_completion.setter
    def ignore_for_completion(self, ignore_for_completion):
        """Sets the ignore_for_completion of this DestinyDefinitionsDestinyTalentNodeDefinition.

        Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.  # noqa: E501

        :param ignore_for_completion: The ignore_for_completion of this DestinyDefinitionsDestinyTalentNodeDefinition.  # noqa: E501
        :type: bool
        """

        self._ignore_for_completion = ignore_for_completion

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
        if not isinstance(other, DestinyDefinitionsDestinyTalentNodeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
