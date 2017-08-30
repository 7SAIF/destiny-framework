# DestinyDefinitionsDestinySandboxPerkDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perk_identifier** | **str** | The string identifier for the perk. | [optional] 
**is_displayable** | **bool** | If true, you can actually show the perk in the UI.  Otherwise, it doesn&#39;thave useful player-facing information. | [optional] 
**damage_type_hash** | **int** | The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.  This is preferred over using the damageType enumeration value, which has been left purely because it isoccasionally convenient. | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


