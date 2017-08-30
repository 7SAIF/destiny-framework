# DestinyEntitiesItemsDestinyItemInstanceComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage_type_hash** | **int** | The current damage type&#39;s hash, so you can look up localized info and icons for it. | [optional] 
**item_level** | **int** | The Item&#39;s \&quot;Level\&quot; has the most significant bearing on its stats, such as Light and Power. | [optional] 
**quality** | **int** | The \&quot;Quality\&quot; of the item has a lesser - but still impactful - bearing on stats like Light and Power. | [optional] 
**is_equipped** | **bool** | Is the item currently equipped on the given character? | [optional] 
**can_equip** | **bool** | If this is an equippable item, you can check it here.  There are permanent as well as transitory reasonswhy an item might not be able to be equipped: check cannotEquipReason for details. | [optional] 
**equip_required_level** | **int** | If the item cannot be equipped until you reach a certain level, that level will be reflected here. | [optional] 
**unlock_hashes_required_to_equip** | **list[int]** | Sometimes, there are limitations to equipping that are represented by character-level flags called \&quot;unlocks\&quot;.  This is a list of flags that they need in order to equip the item that the character has not met.Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


