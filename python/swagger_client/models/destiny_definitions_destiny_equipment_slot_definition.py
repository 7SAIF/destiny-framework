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


class DestinyDefinitionsDestinyEquipmentSlotDefinition(object):
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
        'equipment_category_hash': 'int',
        'bucket_type_hash': 'int',
        'apply_custom_art_dyes': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'equipment_category_hash': 'equipmentCategoryHash',
        'bucket_type_hash': 'bucketTypeHash',
        'apply_custom_art_dyes': 'applyCustomArtDyes',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, equipment_category_hash=None, bucket_type_hash=None, apply_custom_art_dyes=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyDefinitionsDestinyEquipmentSlotDefinition - a model defined in Swagger"""  # noqa: E501

        self._display_properties = None
        self._equipment_category_hash = None
        self._bucket_type_hash = None
        self._apply_custom_art_dyes = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if equipment_category_hash is not None:
            self.equipment_category_hash = equipment_category_hash
        if bucket_type_hash is not None:
            self.bucket_type_hash = bucket_type_hash
        if apply_custom_art_dyes is not None:
            self.apply_custom_art_dyes = apply_custom_art_dyes
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501


        :return: The display_properties of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyDefinitionsDestinyEquipmentSlotDefinition.


        :param display_properties: The display_properties of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def equipment_category_hash(self):
        """Gets the equipment_category_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        These technically point to \"Equipment Category Definitions\". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed.  # noqa: E501

        :return: The equipment_category_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: int
        """
        return self._equipment_category_hash

    @equipment_category_hash.setter
    def equipment_category_hash(self, equipment_category_hash):
        """Sets the equipment_category_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        These technically point to \"Equipment Category Definitions\". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed.  # noqa: E501

        :param equipment_category_hash: The equipment_category_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: int
        """

        self._equipment_category_hash = equipment_category_hash

    @property
    def bucket_type_hash(self):
        """Gets the bucket_type_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        The inventory bucket that owns this equipment slot.  # noqa: E501

        :return: The bucket_type_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: int
        """
        return self._bucket_type_hash

    @bucket_type_hash.setter
    def bucket_type_hash(self, bucket_type_hash):
        """Sets the bucket_type_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        The inventory bucket that owns this equipment slot.  # noqa: E501

        :param bucket_type_hash: The bucket_type_hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: int
        """

        self._bucket_type_hash = bucket_type_hash

    @property
    def apply_custom_art_dyes(self):
        """Gets the apply_custom_art_dyes of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot.  # noqa: E501

        :return: The apply_custom_art_dyes of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._apply_custom_art_dyes

    @apply_custom_art_dyes.setter
    def apply_custom_art_dyes(self, apply_custom_art_dyes):
        """Sets the apply_custom_art_dyes of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot.  # noqa: E501

        :param apply_custom_art_dyes: The apply_custom_art_dyes of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: bool
        """

        self._apply_custom_art_dyes = apply_custom_art_dyes

    @property
    def hash(self):
        """Gets the hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyDefinitionsDestinyEquipmentSlotDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyDefinitionsDestinyEquipmentSlotDefinition.  # noqa: E501
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
        if not isinstance(other, DestinyDefinitionsDestinyEquipmentSlotDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
