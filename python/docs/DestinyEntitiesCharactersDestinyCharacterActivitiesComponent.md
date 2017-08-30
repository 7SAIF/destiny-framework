# DestinyEntitiesCharactersDestinyCharacterActivitiesComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_activity_started** | **datetime** | The last date that the user started playing an activity. | [optional] 
**available_activities** | [**list[DestinyDestinyActivity]**](DestinyDestinyActivity.md) | The list of activities that the user can play. | [optional] 
**current_activity_hash** | **int** | If the user is in an activity, this will be the hash of the Activity being played.Note that you must combine this info with currentActivityModeHash to get a real picture of whatthe user is doing right now.  For instance, PVP \&quot;Activities\&quot; are just maps: it&#39;s the ActivityModethat determines what type of PVP game they&#39;re playing. | [optional] 
**current_activity_mode_hash** | **int** | If the user is in an activity, this will be the hash of the activity mode being played.Combine with currentActivityHash to give a person a full picture of what they&#39;re doing right now. | [optional] 
**last_completed_story_hash** | **int** | This will have the activity hash of the last completed story/campaign mission, in case you care about that. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


