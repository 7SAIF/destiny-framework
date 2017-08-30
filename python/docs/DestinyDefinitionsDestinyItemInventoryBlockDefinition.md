# DestinyDefinitionsDestinyItemInventoryBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_unique_label** | **str** | If this string is populated, you can&#39;t have more than one stack with this label in a given inventory.Note that this is different from the equipping block&#39;s unique label, which is used for equipping uniqueness. | [optional] 
**max_stack_size** | **int** | The maximum quantity of this item that can exist in a stack. | [optional] 
**bucket_type_hash** | **int** | The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs.I should have named this \&quot;bucketHash\&quot;, but too many things refer to it now.  Sigh. | [optional] 
**recovery_bucket_type_hash** | **int** | If the item is picked up by the lost loot queue, this is the hash identifierfor the DestinyInventoryBucketDefinition into which it will be placed.Again, I should have named this recoveryBucketHash instead. | [optional] 
**tier_type_hash** | **int** | The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinitionif you need to show localized data for the item&#39;s tier. | [optional] 
**is_instance_item** | **bool** | If TRUE, this item is instanced.  Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer). | [optional] 
**tier_type_name** | **str** | The localized name of the tier type, which is a useful shortcut so you don&#39;t have to look up the definition every time.  However, it&#39;s mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


