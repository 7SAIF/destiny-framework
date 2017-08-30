# DestinyDefinitionsDestinyItemSocketEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**socket_type_hash** | **int** | All sockets have a type, and this is the hash identifier for this particular type.Use it to look up the DestinySocketTypeDefinition: read there for more information onhow socket types affect the behavior of the socket. | [optional] 
**single_initial_item_hash** | **int** | If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinitionrepresenting the Plug that will be initially inserted into the item on item creation.Otherwise, this Socket will either start without a plug inserted, or will have one randomlyinserted. | [optional] 
**reusable_plug_items** | [**list[DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition]**](DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition.md) | This is a list of pre-determined plugs that can *always* be plugged into this socket, withoutthe character having the plug in their inventory.  If this list is populated, you will not be allowed to plug an arbitrary item in the socket: youwill only be able to choose from one of these reusable plugs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


