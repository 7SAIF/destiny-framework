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


class DestinyDefinitionsDestinyTalentExclusiveGroup(object):
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
        'group_hash': 'int',
        'lore_hash': 'int',
        'node_hashes': 'list[int]',
        'opposing_group_hashes': 'list[int]',
        'opposing_node_hashes': 'list[int]'
    }

    attribute_map = {
        'group_hash': 'groupHash',
        'lore_hash': 'loreHash',
        'node_hashes': 'nodeHashes',
        'opposing_group_hashes': 'opposingGroupHashes',
        'opposing_node_hashes': 'opposingNodeHashes'
    }

    def __init__(self, group_hash=None, lore_hash=None, node_hashes=None, opposing_group_hashes=None, opposing_node_hashes=None):
        """
        DestinyDefinitionsDestinyTalentExclusiveGroup - a model defined in Swagger
        """

        self._group_hash = None
        self._lore_hash = None
        self._node_hashes = None
        self._opposing_group_hashes = None
        self._opposing_node_hashes = None

        if group_hash is not None:
          self.group_hash = group_hash
        if lore_hash is not None:
          self.lore_hash = lore_hash
        if node_hashes is not None:
          self.node_hashes = node_hashes
        if opposing_group_hashes is not None:
          self.opposing_group_hashes = opposing_group_hashes
        if opposing_node_hashes is not None:
          self.opposing_node_hashes = opposing_node_hashes

    @property
    def group_hash(self):
        """
        Gets the group_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        The identifier for this exclusive group.  Only guaranteed unique within the talent grid, not globally.

        :return: The group_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :rtype: int
        """
        return self._group_hash

    @group_hash.setter
    def group_hash(self, group_hash):
        """
        Sets the group_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        The identifier for this exclusive group.  Only guaranteed unique within the talent grid, not globally.

        :param group_hash: The group_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :type: int
        """

        self._group_hash = group_hash

    @property
    def lore_hash(self):
        """
        Gets the lore_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.

        :return: The lore_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :rtype: int
        """
        return self._lore_hash

    @lore_hash.setter
    def lore_hash(self, lore_hash):
        """
        Sets the lore_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.

        :param lore_hash: The lore_hash of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :type: int
        """

        self._lore_hash = lore_hash

    @property
    def node_hashes(self):
        """
        Gets the node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of the talent nodes that are part of this group, by their Talent Node hashes.  (See DestinyTalentNodeDefinition.nodeHash)

        :return: The node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :rtype: list[int]
        """
        return self._node_hashes

    @node_hashes.setter
    def node_hashes(self, node_hashes):
        """
        Sets the node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of the talent nodes that are part of this group, by their Talent Node hashes.  (See DestinyTalentNodeDefinition.nodeHash)

        :param node_hashes: The node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :type: list[int]
        """

        self._node_hashes = node_hashes

    @property
    def opposing_group_hashes(self):
        """
        Gets the opposing_group_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.

        :return: The opposing_group_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :rtype: list[int]
        """
        return self._opposing_group_hashes

    @opposing_group_hashes.setter
    def opposing_group_hashes(self, opposing_group_hashes):
        """
        Sets the opposing_group_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.

        :param opposing_group_hashes: The opposing_group_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :type: list[int]
        """

        self._opposing_group_hashes = opposing_group_hashes

    @property
    def opposing_node_hashes(self):
        """
        Gets the opposing_node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of Nodes that will be deactivated if any node in this group is activated, by  their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)

        :return: The opposing_node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :rtype: list[int]
        """
        return self._opposing_node_hashes

    @opposing_node_hashes.setter
    def opposing_node_hashes(self, opposing_node_hashes):
        """
        Sets the opposing_node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        A quick reference of Nodes that will be deactivated if any node in this group is activated, by  their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)

        :param opposing_node_hashes: The opposing_node_hashes of this DestinyDefinitionsDestinyTalentExclusiveGroup.
        :type: list[int]
        """

        self._opposing_node_hashes = opposing_node_hashes

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
        if not isinstance(other, DestinyDefinitionsDestinyTalentExclusiveGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
