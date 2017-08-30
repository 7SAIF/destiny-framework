# DestinyDefinitionsDestinyVendorAcceptedItemDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_inventory_bucket_hash** | **int** | The \&quot;source\&quot; bucket for a transfer.  When a user wants to transfer an item, the appropriate DestinyVendorDefinition&#39;sacceptedItems property is evaluated, looking for an entry where acceptedInventoryBucketHash matchesthe bucket that the item being transferred is currently located.  If it exists, the item will betransferred into whatever bucket is defined by destinationInventoryBucketHash. | [optional] 
**destination_inventory_bucket_hash** | **int** | This is the bucket where the item being transferred will be put, given that it was beingtransferred *from* the bucket defined in acceptedInventoryBucketHash. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


