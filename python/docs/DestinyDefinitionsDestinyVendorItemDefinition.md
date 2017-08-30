# DestinyDefinitionsDestinyVendorItemDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_item_index** | **int** | The index into the DestinyVendorDefinition.saleList.  This is what we use to refer to items  being sold throughout live and definition data. | [optional] 
**item_hash** | **int** | The hash identifier of the item being sold (DestinyInventoryItemDefinition).    Note that a vendor can sell the same item in multiple ways, so don&#39;t assume that itemHash is  a unique identifier for this entity. | [optional] 
**quantity** | **int** | The amount you will recieve of the item described in itemHash if you make the purchase. | [optional] 
**failure_indexes** | **list[int]** | An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating  the possible failure strings that can be relevant for this item. | [optional] 
**currencies** | [**list[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place  to check for what the purchaser must pay for the item.  Use this instead of trying to piece together  the price separately. | [optional] 
**refund_time_limit** | **int** | The amount of time before refundability of the newly purchased item will expire. | [optional] 
**creation_levels** | [**list[DestinyDefinitionsDestinyItemCreationEntryLevelDefinition]**](DestinyDefinitionsDestinyItemCreationEntryLevelDefinition.md) | The Default level at which the item will spawn.  Almost always driven by an adjusto these days.  Ideally should be singular.  It&#39;s a long story how this ended up as a list, but there is always either  going to be 0:1 of these entities. | [optional] 
**display_category_index** | **int** | This is an index specifically into the display category, as opposed to the server-side Categories  (which do not need to match or pair with each other in any way: server side categories are really just  structures for common validation.  Display Category will let us more easily categorize items visually) | [optional] 
**category_index** | **int** | The index into the DestinyVendorDefinition.categories array, so you can find the category associated with  this item. | [optional] 
**original_category_index** | **int** | Same as above, but for the original category indexes. | [optional] 
**minimum_level** | **int** | The minimum character level at which this item is available for sale. | [optional] 
**maximum_level** | **int** | The maximum character level at which this item is available for sale. | [optional] 
**display_category** | **str** | The string identifier for the category selling this item. | [optional] 
**inventory_bucket_hash** | **int** | The inventory bucket into which this item will be placed upon purchase. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


