# DestinyDefinitionsDestinyVendorItemDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_item_index** | **int** | The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data. | [optional] 
**item_hash** | **int** | The hash identifier of the item being sold (DestinyInventoryItemDefinition).  Note that a vendor can sell the same item in multiple ways, so don&#39;t assume that itemHash is a unique identifier for this entity. | [optional] 
**quantity** | **int** | The amount you will recieve of the item described in itemHash if you make the purchase. | [optional] 
**failure_indexes** | **list[int]** | An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item. | [optional] 
**currencies** | [**list[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.  JUST KIDDING HA this never got populated, who&#39;s the idiot now? Hint: Me. Now they&#39;ll actually be populated [amola, 2017-11-12] | [optional] 
**refund_policy** | **object** | If this item can be refunded, this is the policy for what will be refundd, how, and in what time period. | [optional] 
**refund_time_limit** | **int** | The amount of time before refundability of the newly purchased item will expire. | [optional] 
**creation_levels** | [**list[DestinyDefinitionsDestinyItemCreationEntryLevelDefinition]**](DestinyDefinitionsDestinyItemCreationEntryLevelDefinition.md) | The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It&#39;s a long story how this ended up as a list, but there is always either going to be 0:1 of these entities. | [optional] 
**display_category_index** | **int** | This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually) | [optional] 
**category_index** | **int** | The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item. | [optional] 
**original_category_index** | **int** | Same as above, but for the original category indexes. | [optional] 
**minimum_level** | **int** | The minimum character level at which this item is available for sale. | [optional] 
**maximum_level** | **int** | The maximum character level at which this item is available for sale. | [optional] 
**action** | **object** | The action to be performed when purchasing the item, if it&#39;s not just \&quot;buy\&quot;. | [optional] 
**display_category** | **str** | The string identifier for the category selling this item. | [optional] 
**inventory_bucket_hash** | **int** | The inventory bucket into which this item will be placed upon purchase. | [optional] 
**visibility_scope** | **object** | The most restrictive scope that determines whether the item is available in the Vendor&#39;s inventory. See DestinyGatingScope&#39;s documentation for more information.  This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties). | [optional] 
**purchasable_scope** | **object** | Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.  See DestinyGatingScope&#39;s documentation for more information. | [optional] 
**exclusivity** | **object** | If this item can only be purchased by a given platform, this indicates the platform to which it is restricted. | [optional] 
**is_offer** | **bool** | If this sale can only be performed as the result of an offer check, this is true. | [optional] 
**is_crm** | **bool** | If this sale can only be performed as the result of receiving a CRM offer, this is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


