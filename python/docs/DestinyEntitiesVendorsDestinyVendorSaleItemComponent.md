# DestinyEntitiesVendorsDestinyVendorSaleItemComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_item_index** | **int** | The index into the DestinyVendorDefinition.itemList property.  Note that this means Vendor data*is* Content Version dependent: make sure you have the latest content before you use Vendor data,or these indexes may mismatch.    Most systems avoid this problem, but Vendors is one area where weare unable to reasonably avoid content dependency at the moment. | [optional] 
**item_hash** | **int** | The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinitionof the sale item. | [optional] 
**costs** | [**list[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | A summary of the current costs of the item. | [optional] 
**required_unlocks** | **list[int]** | If you can&#39;t buy the item due to a complex character state, these will be hashes forDestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlockshave human readable information: it is not guaranteed that Unlocks will have human readable strings, andyour application will have to handle that)  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes. | [optional] 
**unlock_statuses** | [**list[DestinyDestinyUnlockStatus]**](DestinyDestinyUnlockStatus.md) | If any complex unlock states are checked in determining purchasability, these willbe returned here along with the status of the unlock check.  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes. | [optional] 
**failure_indexes** | **list[int]** | Indexes in to the \&quot;failureStrings\&quot; lookup table in DestinyVendorDefinition for the given Vendor.Gives some more reliable failure information for why you can&#39;t purchase an item.  It is preferred to use these over requiredUnlocks and unlockStatuses: the latter are providedmostly in case someone can do something interesting with it that I didn&#39;t anticipate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


