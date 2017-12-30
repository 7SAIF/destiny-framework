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


class DestinyEntitiesVendorsDestinyVendorComponent(object):
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
        'vendor_hash': 'int',
        'next_refresh_date': 'datetime',
        'enabled': 'bool',
        'can_purchase': 'bool',
        'progression': 'object'
    }

    attribute_map = {
        'vendor_hash': 'vendorHash',
        'next_refresh_date': 'nextRefreshDate',
        'enabled': 'enabled',
        'can_purchase': 'canPurchase',
        'progression': 'progression'
    }

    def __init__(self, vendor_hash=None, next_refresh_date=None, enabled=None, can_purchase=None, progression=None):  # noqa: E501
        """DestinyEntitiesVendorsDestinyVendorComponent - a model defined in Swagger"""  # noqa: E501

        self._vendor_hash = None
        self._next_refresh_date = None
        self._enabled = None
        self._can_purchase = None
        self._progression = None
        self.discriminator = None

        if vendor_hash is not None:
            self.vendor_hash = vendor_hash
        if next_refresh_date is not None:
            self.next_refresh_date = next_refresh_date
        if enabled is not None:
            self.enabled = enabled
        if can_purchase is not None:
            self.can_purchase = can_purchase
        if progression is not None:
            self.progression = progression

    @property
    def vendor_hash(self):
        """Gets the vendor_hash of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501

        The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.  # noqa: E501

        :return: The vendor_hash of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :rtype: int
        """
        return self._vendor_hash

    @vendor_hash.setter
    def vendor_hash(self, vendor_hash):
        """Sets the vendor_hash of this DestinyEntitiesVendorsDestinyVendorComponent.

        The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.  # noqa: E501

        :param vendor_hash: The vendor_hash of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :type: int
        """

        self._vendor_hash = vendor_hash

    @property
    def next_refresh_date(self):
        """Gets the next_refresh_date of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501

        The date when this vendor's inventory will next rotate/refresh.  # noqa: E501

        :return: The next_refresh_date of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :rtype: datetime
        """
        return self._next_refresh_date

    @next_refresh_date.setter
    def next_refresh_date(self, next_refresh_date):
        """Sets the next_refresh_date of this DestinyEntitiesVendorsDestinyVendorComponent.

        The date when this vendor's inventory will next rotate/refresh.  # noqa: E501

        :param next_refresh_date: The next_refresh_date of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :type: datetime
        """

        self._next_refresh_date = next_refresh_date

    @property
    def enabled(self):
        """Gets the enabled of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501

        If True, the Vendor is currently accessible.   If False, they may not actually be visible in the world at the moment.  # noqa: E501

        :return: The enabled of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DestinyEntitiesVendorsDestinyVendorComponent.

        If True, the Vendor is currently accessible.   If False, they may not actually be visible in the world at the moment.  # noqa: E501

        :param enabled: The enabled of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def can_purchase(self):
        """Gets the can_purchase of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501

        If True, you can purchase from the Vendor.  Theoretically, Vendors can be restricted from selling items. In practice, none do that (yet?).  # noqa: E501

        :return: The can_purchase of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :rtype: bool
        """
        return self._can_purchase

    @can_purchase.setter
    def can_purchase(self, can_purchase):
        """Sets the can_purchase of this DestinyEntitiesVendorsDestinyVendorComponent.

        If True, you can purchase from the Vendor.  Theoretically, Vendors can be restricted from selling items. In practice, none do that (yet?).  # noqa: E501

        :param can_purchase: The can_purchase of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :type: bool
        """

        self._can_purchase = can_purchase

    @property
    def progression(self):
        """Gets the progression of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501

        If the Vendor has a related Reputation, this is the Progression data that represents the character's Reputation level with this Vendor.  # noqa: E501

        :return: The progression of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :rtype: object
        """
        return self._progression

    @progression.setter
    def progression(self, progression):
        """Sets the progression of this DestinyEntitiesVendorsDestinyVendorComponent.

        If the Vendor has a related Reputation, this is the Progression data that represents the character's Reputation level with this Vendor.  # noqa: E501

        :param progression: The progression of this DestinyEntitiesVendorsDestinyVendorComponent.  # noqa: E501
        :type: object
        """

        self._progression = progression

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
        if not isinstance(other, DestinyEntitiesVendorsDestinyVendorComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
