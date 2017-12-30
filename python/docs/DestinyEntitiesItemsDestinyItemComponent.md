# DestinyEntitiesItemsDestinyItemComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_hash** | **int** | The identifier for the item&#39;s definition, which is where most of the useful static information for the item can be found. | [optional] 
**item_instance_id** | **int** | If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size. | [optional] 
**quantity** | **int** | The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it) | [optional] 
**bind_status** | **object** | If the item is bound to a location, it will be specified in this enum. | [optional] 
**location** | **object** | An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items. | [optional] 
**bucket_hash** | **int** | The hash identifier for the specific inventory bucket in which the item is located. | [optional] 
**transfer_status** | **object** | If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer). | [optional] 
**lockable** | **bool** | If the item can be locked, this will indicate that state. | [optional] 
**state** | **object** | A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it&#39;s tracked or locked for example, or whether it has a masterwork plug inserted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


