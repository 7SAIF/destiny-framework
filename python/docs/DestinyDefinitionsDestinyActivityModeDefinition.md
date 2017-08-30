# DestinyDefinitionsDestinyActivityModeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**pgcr_image** | **str** |  | [optional] 
**mode_type** | [**DestinyHistoricalStatsDefinitionsDestinyActivityModeType**](DestinyHistoricalStatsDefinitionsDestinyActivityModeType.md) |  | [optional] 
**activity_mode_category** | [**DestinyDestinyActivityModeCategory**](DestinyDestinyActivityModeCategory.md) |  | [optional] 
**parent_hashes** | **list[int]** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**activity_mode_mappings** | [**dict(str, DestinyHistoricalStatsDefinitionsDestinyActivityModeType)**](DestinyHistoricalStatsDefinitionsDestinyActivityModeType.md) |  | [optional] 
**display** | **bool** | If FALSE, we want to ignore this type when we&#39;re showing activity modes in BNet UI.  It will still be returned in case3rd parties want to use it for any purpose. | [optional] 
**order** | **int** | The relative ordering of activity modes. | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


