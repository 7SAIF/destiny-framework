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

from swagger_client.models.destiny_entities_vendors_destiny_vendor_sale_item_component import DestinyEntitiesVendorsDestinyVendorSaleItemComponent  # noqa: F401,E501


class DestinyComponentsVendorsDestinyVendorSaleItemSetComponent(object):
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
        'sale_items': 'dict(str, DestinyEntitiesVendorsDestinyVendorSaleItemComponent)'
    }

    attribute_map = {
        'sale_items': 'saleItems'
    }

    def __init__(self, sale_items=None):  # noqa: E501
        """DestinyComponentsVendorsDestinyVendorSaleItemSetComponent - a model defined in Swagger"""  # noqa: E501

        self._sale_items = None
        self.discriminator = None

        if sale_items is not None:
            self.sale_items = sale_items

    @property
    def sale_items(self):
        """Gets the sale_items of this DestinyComponentsVendorsDestinyVendorSaleItemSetComponent.  # noqa: E501

        The items being sold by this vendor, keyed by the vendorItemIndex of the item being sold. (because showing sale items depends on the ordering dictated by the categories being shown - see DestinyVendorCategoryComponent - this is a dictionary for quick lookup capability.)  # noqa: E501

        :return: The sale_items of this DestinyComponentsVendorsDestinyVendorSaleItemSetComponent.  # noqa: E501
        :rtype: dict(str, DestinyEntitiesVendorsDestinyVendorSaleItemComponent)
        """
        return self._sale_items

    @sale_items.setter
    def sale_items(self, sale_items):
        """Sets the sale_items of this DestinyComponentsVendorsDestinyVendorSaleItemSetComponent.

        The items being sold by this vendor, keyed by the vendorItemIndex of the item being sold. (because showing sale items depends on the ordering dictated by the categories being shown - see DestinyVendorCategoryComponent - this is a dictionary for quick lookup capability.)  # noqa: E501

        :param sale_items: The sale_items of this DestinyComponentsVendorsDestinyVendorSaleItemSetComponent.  # noqa: E501
        :type: dict(str, DestinyEntitiesVendorsDestinyVendorSaleItemComponent)
        """

        self._sale_items = sale_items

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
        if not isinstance(other, DestinyComponentsVendorsDestinyVendorSaleItemSetComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other