# DestinyDefinitionsDestinyActivityRewardDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_text** | **str** | The header for the reward set, if any. | [optional] 
**reward_items** | [**list[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | The \&quot;Items provided\&quot; in the reward.  This is almost always a pointer to a DestinyInventoryItemDefintionfor an item that you can&#39;t actually earn in-game, but that has name/description/icon information forthe vague concept of the rewards you will receive.  This is because the actual reward generation isnon-deterministic and extremely complicated, so the best the game can do is tell you what you&#39;ll getin vague terms.  And so too shall we.  Interesting trivia: you actually *do* earn these items when you complete the activity.  They go into a single-slotbucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that matchthese \&quot;dummy\&quot; items.  You can even see them if you look at the last one you earned in yourprofile-level inventory through the BNet API!  Who said reading documentation is a waste of time? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


