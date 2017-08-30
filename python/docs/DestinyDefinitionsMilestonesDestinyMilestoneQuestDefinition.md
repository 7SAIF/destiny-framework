# DestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quest_item_hash** | **int** | The item representing this Milestone quest.  Use this hash to look up the DestinyInventoryItemDefinitionfor the quest to find its steps and human readable data. | [optional] 
**override_image** | **str** | If populated, this image can be shown instead of the generic milestone&#39;s image when this quest is live,or it can be used to show a background image for the quest itself that differs from that of the Activityor the Milestone. | [optional] 
**activities** | [**dict(str, DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition)**](DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition.md) | The full set of all possible \&quot;conceptual activities\&quot; that are related to this Milestone.Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities.Keyed by the Conceptual Activity Hash.  Use the key to look up DestinyActivityDefinition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


