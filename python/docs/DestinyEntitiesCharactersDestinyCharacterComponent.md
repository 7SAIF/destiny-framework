# DestinyEntitiesCharactersDestinyCharacterComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | Every Destiny Profile has a membershipId.  This is provided on the character as well for convenience. | [optional] 
**character_id** | **int** | The unique identifier for the character. | [optional] 
**date_last_played** | **datetime** | The last date that the user played Destiny. | [optional] 
**minutes_played_this_session** | **int** | If the user is currently playing, this is how long they&#39;ve been playing. | [optional] 
**minutes_played_total** | **int** | If this value is 525,600, then they played Destiny for a year.  Or they&#39;re a very dedicated Rent fan.Note that this includes idle time, not just time spent actually in activities shooting things. | [optional] 
**light** | **int** | The user&#39;s calculated \&quot;Light Level\&quot;.  Light level is an indicator of your power that mostly matters inthe end game, once you&#39;ve reached the maximum character level: it&#39;s a level that&#39;s dependent on the averageAttack/Defense power of your items. | [optional] 
**stats** | **dict(str, int)** | Your character&#39;s stats, such as Agility, Resilience, etc... *not* historical stats.  You&#39;ll have to call a different endpoint for those. | [optional] 
**race_hash** | **int** | Use this hash to look up the character&#39;s DestinyRaceDefinition. | [optional] 
**gender_hash** | **int** | Use this hash to look up the character&#39;s DestinyGenderDefinition. | [optional] 
**class_hash** | **int** | Use this hash to look up the character&#39;s DestinyClassDefinition. | [optional] 
**emblem_path** | **str** | A shortcut path to the user&#39;s currently equipped emblem image.  If you&#39;re just showing summaryinfo for a user, this is more convenient than examining their equipped emblem and looking up the definition. | [optional] 
**emblem_background_path** | **str** | A shortcut path to the user&#39;s currently equipped emblem background image.  If you&#39;re just showing summaryinfo for a user, this is more convenient than examining their equipped emblem and looking up the definition. | [optional] 
**emblem_hash** | **int** | The hash of the currently equipped emblem for the user.  Can be used to look up the DestinyInventoryItemDefinition. | [optional] 
**base_character_level** | **int** | The \&quot;base\&quot; level of your character, not accounting for any light level. | [optional] 
**percent_to_next_level** | **float** | A number between 0 and 100, indicating the whole and fractional % remaining to get tothe next character level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


