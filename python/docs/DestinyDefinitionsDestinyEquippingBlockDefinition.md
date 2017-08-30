# DestinyDefinitionsDestinyEquippingBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gearset_item_hash** | **int** | If the item is part of a gearset, this is a reference to that gearset item. | [optional] 
**unique_label** | **str** | If defined, this is the label used to check if the item has other items ofmatching types already equipped.    For instance, when you aren&#39;t allowed toequip more than one Exotic Weapon, that&#39;s because all exotic weapons haveidentical uniqueLabels and the game checks the to-be-equipped item&#39;s uniqueLabelvs. all other already equipped items (other than the item in the slot that&#39;sabout to be occupied). | [optional] 
**unique_label_hash** | **int** | The hash of that unique label.  Does not point to a specific definition. | [optional] 
**equipment_slot_type_hash** | **int** | An equipped item *must* be equipped in an Equipment Slot.  This is the hash identifierof the DestinyEquipmentSlotDefinition into which it must be equipped. | [optional] 
**display_strings** | **list[str]** | These are strings that represent the possible Game/Account/Character state failure conditionsthat can occur when trying to equip the item.  They match up one-to-one with requiredUnlockExpressions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


