# DestinyDefinitionsDestinyVendorInteractionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replies** | [**list[DestinyDefinitionsDestinyVendorInteractionReplyDefinition]**](DestinyDefinitionsDestinyVendorInteractionReplyDefinition.md) | The potential replies that the user can make to the interaction. | [optional] 
**vendor_category_index** | **int** | If &gt;&#x3D; 0, this is the category of sale items to show along with this interaction dialog. | [optional] 
**questline_item_hash** | **int** | If this interaction dialog is about a quest, this is the questline related to the interaction.You can use this to show the quest overview, or even the character&#39;s status with the quest ifyou use it to find the character&#39;s current Quest Step by checking their inventory against this questlineItemHash&#39;sDestinyInventoryItemDefinition.setData. | [optional] 
**sack_interaction_list** | [**list[DestinyDefinitionsDestinyVendorInteractionSackEntryDefinition]**](DestinyDefinitionsDestinyVendorInteractionSackEntryDefinition.md) | If this interaction is meant to show you sacks, this is the list of types of sacks to be shown.If empty, the interaction is not meant to show sacks. | [optional] 
**ui_interaction_type** | **int** | A UI hint for the behavior of the interaction screen.  BNet doesn&#39;t use this, but you can choose to. | [optional] 
**reward_block_label** | **str** | If this interaction is displaying rewards, this is the text to use for the header of thereward-displaying section of the interaction. | [optional] 
**reward_vendor_category_index** | **int** | If the vendor&#39;s reward list is sourced from one of his categories, this is the index intothe category array of items to show. | [optional] 
**flavor_line_one** | **str** | If the vendor interaction has flavor text, this is some of it. | [optional] 
**flavor_line_two** | **str** | If the vendor interaction has flavor text, this is the rest of it. | [optional] 
**instructions** | **str** | The localized text telling the player what to do when they see this dialog. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


