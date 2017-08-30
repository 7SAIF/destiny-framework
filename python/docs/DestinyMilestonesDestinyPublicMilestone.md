# DestinyMilestonesDestinyPublicMilestone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milestone_hash** | **int** | The hash identifier for the milestone.  Use it to look up the DestinyMilestoneDefinition forstatic data about the Milestone. | [optional] 
**available_quests** | [**list[DestinyMilestonesDestinyPublicMilestoneQuest]**](DestinyMilestonesDestinyPublicMilestoneQuest.md) | A milestone not need have even a single quest, but if there are active quests they will be returned here. | [optional] 
**vendor_hashes** | **list[int]** | Sometimes milestones - or activities active in milestones - will have relevant vendors.These are the vendors that are currently relevant. | [optional] 
**start_date** | **datetime** | If known, this is the date when the Milestone started/became active. | [optional] 
**end_date** | **datetime** | If known, this is the date when the Milestone will expire/recycle/end. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


