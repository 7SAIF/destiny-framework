# DestinyEntitiesItemsDestinyItemComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_hash** | **int** | The identifier for the item&#39;s definition, which is where most of the useful static information for the itemcan be found. | [optional] 
**item_instance_id** | **int** | If the item is instanced, it will have an instance ID.  Lack of an instance ID impliesthat the item has no distinct local qualities aside from stack size. | [optional] 
**quantity** | **int** | The quantity of the item in this stack.  Note that Instanced items cannot stack.If an instanced item, this value will always be 1 (as the stack has exactly one item in it) | [optional] 
**bucket_hash** | **int** | The hash identifier for the specific inventory bucket in which the item is located. | [optional] 
**lockable** | **bool** | If the item can be locked, this will indicate that state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


