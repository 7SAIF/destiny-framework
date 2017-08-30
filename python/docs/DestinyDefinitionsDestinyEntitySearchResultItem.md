# DestinyDefinitionsDestinyEntitySearchResultItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **int** | The hash identifier of the entity.  You will use this to look up the DestinyDefinitionrelevant for the entity found. | [optional] 
**entity_type** | **str** | The type of entity, returned as a string matching the DestinyDefinition&#39;s contract class name.You&#39;ll have to have your own mapping from class names to actually looking up those definitionsin the manifest databases. | [optional] 
**weight** | **float** | The ranking value for sorting that we calculated using our relevance formula.  Thiswill hopefully get better with time and iteration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


