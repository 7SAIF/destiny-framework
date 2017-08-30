# DestinyDefinitionsDestinyItemQualityBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_levels** | **list[int]** | The \&quot;base\&quot; defined level of an item.  This is a list because, in theory,each Expansion could define its own base level for an item.  In practice, not only was that never done in Destiny 1, but now thisisn&#39;t even populated at all.  When it&#39;s not populated, the level at whichit spawns has to be inferred by Reward information, of which BNet receives an imperfectview and will only be reliable on instanced data as a result. | [optional] 
**quality_level** | **int** | qualityLevel is used in combination with the item&#39;s level to calculate stats likeAttack and Defense.  It plays a role in that calculation, but not nearly as large asitemLevel does. | [optional] 
**infusion_category_name** | **str** | The string identifier for this item&#39;s \&quot;infusability\&quot;, if any.    Items that match the same infusionCategoryName are allowed to infuse with each other. | [optional] 
**infusion_category_hash** | **int** | The hash identifier for the infusion.  It does not map to a Definition entity. | [optional] 
**progression_level_requirement_hash** | **int** | An item can refer to pre-set level requirements.  They are defined in DestinyProgressionLevelRequirementDefinition,and you can use this hash to find the appropriate definition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


