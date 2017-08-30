# DestinyDefinitionsDestinyVendorCategoryEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_index** | **int** | The index of the category in the original category definitions for the vendor. | [optional] 
**category_id** | **str** | The string identifier of the category. | [optional] 
**category_hash** | **int** | The hashed identifier for the category.  (note that this is NOT pointing to a DestinyVendorCategoryDefinition,it&#39;s confusing but this is a sale item category in a vendor, not a categorization of vendors themselves) | [optional] 
**quantity_available** | **int** | The amount of items that will be available when this category is shown. | [optional] 
**show_unavailable_items** | **bool** | If items aren&#39;t up for sale in this category, should we still show them (greyed out)? | [optional] 
**hide_if_no_currency** | **bool** | If you don&#39;t have the currency required to buy items from this category, should the items be hidden? | [optional] 
**hide_from_regular_purchase** | **bool** | True if this category doesn&#39;t allow purchases. | [optional] 
**buy_string_override** | **str** | The localized string for making purchases from this category, if it is different from the vendor&#39;s string for purchasing. | [optional] 
**disabled_description** | **str** | If the category is disabled, this is the localized description to show. | [optional] 
**display_title** | **str** | The localized title of the category. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


