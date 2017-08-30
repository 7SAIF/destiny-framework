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


class DestinyDefinitionsDestinyEquippingBlockDefinition(object):
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
        'gearset_item_hash': 'int',
        'unique_label': 'str',
        'unique_label_hash': 'int',
        'equipment_slot_type_hash': 'int',
        'display_strings': 'list[str]'
    }

    attribute_map = {
        'gearset_item_hash': 'gearsetItemHash',
        'unique_label': 'uniqueLabel',
        'unique_label_hash': 'uniqueLabelHash',
        'equipment_slot_type_hash': 'equipmentSlotTypeHash',
        'display_strings': 'displayStrings'
    }

    def __init__(self, gearset_item_hash=None, unique_label=None, unique_label_hash=None, equipment_slot_type_hash=None, display_strings=None):
        """
        DestinyDefinitionsDestinyEquippingBlockDefinition - a model defined in Swagger
        """

        self._gearset_item_hash = None
        self._unique_label = None
        self._unique_label_hash = None
        self._equipment_slot_type_hash = None
        self._display_strings = None

        if gearset_item_hash is not None:
          self.gearset_item_hash = gearset_item_hash
        if unique_label is not None:
          self.unique_label = unique_label
        if unique_label_hash is not None:
          self.unique_label_hash = unique_label_hash
        if equipment_slot_type_hash is not None:
          self.equipment_slot_type_hash = equipment_slot_type_hash
        if display_strings is not None:
          self.display_strings = display_strings

    @property
    def gearset_item_hash(self):
        """
        Gets the gearset_item_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        If the item is part of a gearset, this is a reference to that gearset item.

        :return: The gearset_item_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :rtype: int
        """
        return self._gearset_item_hash

    @gearset_item_hash.setter
    def gearset_item_hash(self, gearset_item_hash):
        """
        Sets the gearset_item_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        If the item is part of a gearset, this is a reference to that gearset item.

        :param gearset_item_hash: The gearset_item_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :type: int
        """

        self._gearset_item_hash = gearset_item_hash

    @property
    def unique_label(self):
        """
        Gets the unique_label of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        If defined, this is the label used to check if the item has other items of  matching types already equipped.      For instance, when you aren't allowed to  equip more than one Exotic Weapon, that's because all exotic weapons have  identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel  vs. all other already equipped items (other than the item in the slot that's  about to be occupied).

        :return: The unique_label of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :rtype: str
        """
        return self._unique_label

    @unique_label.setter
    def unique_label(self, unique_label):
        """
        Sets the unique_label of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        If defined, this is the label used to check if the item has other items of  matching types already equipped.      For instance, when you aren't allowed to  equip more than one Exotic Weapon, that's because all exotic weapons have  identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel  vs. all other already equipped items (other than the item in the slot that's  about to be occupied).

        :param unique_label: The unique_label of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :type: str
        """

        self._unique_label = unique_label

    @property
    def unique_label_hash(self):
        """
        Gets the unique_label_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        The hash of that unique label.  Does not point to a specific definition.

        :return: The unique_label_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :rtype: int
        """
        return self._unique_label_hash

    @unique_label_hash.setter
    def unique_label_hash(self, unique_label_hash):
        """
        Sets the unique_label_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        The hash of that unique label.  Does not point to a specific definition.

        :param unique_label_hash: The unique_label_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :type: int
        """

        self._unique_label_hash = unique_label_hash

    @property
    def equipment_slot_type_hash(self):
        """
        Gets the equipment_slot_type_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        An equipped item *must* be equipped in an Equipment Slot.  This is the hash identifier  of the DestinyEquipmentSlotDefinition into which it must be equipped.

        :return: The equipment_slot_type_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :rtype: int
        """
        return self._equipment_slot_type_hash

    @equipment_slot_type_hash.setter
    def equipment_slot_type_hash(self, equipment_slot_type_hash):
        """
        Sets the equipment_slot_type_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        An equipped item *must* be equipped in an Equipment Slot.  This is the hash identifier  of the DestinyEquipmentSlotDefinition into which it must be equipped.

        :param equipment_slot_type_hash: The equipment_slot_type_hash of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :type: int
        """

        self._equipment_slot_type_hash = equipment_slot_type_hash

    @property
    def display_strings(self):
        """
        Gets the display_strings of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        These are strings that represent the possible Game/Account/Character state failure conditions  that can occur when trying to equip the item.  They match up one-to-one with requiredUnlockExpressions.

        :return: The display_strings of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :rtype: list[str]
        """
        return self._display_strings

    @display_strings.setter
    def display_strings(self, display_strings):
        """
        Sets the display_strings of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        These are strings that represent the possible Game/Account/Character state failure conditions  that can occur when trying to equip the item.  They match up one-to-one with requiredUnlockExpressions.

        :param display_strings: The display_strings of this DestinyDefinitionsDestinyEquippingBlockDefinition.
        :type: list[str]
        """

        self._display_strings = display_strings

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
        if not isinstance(other, DestinyDefinitionsDestinyEquippingBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
