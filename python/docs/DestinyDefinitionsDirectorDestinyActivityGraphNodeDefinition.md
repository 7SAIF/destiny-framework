# DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph. | [optional] 
**featuring_states** | [**list[DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition]**](DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition.md) | The node may have various visual accents placed on it, or styles applied.  These are the list of possible stylesthat the Node can have.  The game iterates through each, looking for the first one that passes a check of the requiredgame/character/account state in order to show that style, and then renders the node in that style. | [optional] 
**activities** | [**list[DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition]**](DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.md) | The node may have various possible activities that could be active for it, however only one may be activeat a time.  See the DestinyActivityGraphNodeActivityDefinition for details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


