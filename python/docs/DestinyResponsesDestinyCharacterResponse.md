# DestinyResponsesDestinyCharacterResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | **object** | The character-level non-equipped inventory items.  COMPONENT TYPE: CharacterInventories | [optional] 
**character** | **object** | Base information about the character in question.  COMPONENT TYPE: Characters | [optional] 
**progressions** | **object** | Character progression data, including Milestones.  COMPONENT TYPE: CharacterProgressions | [optional] 
**render_data** | **object** | Character rendering data - a minimal set of information about equipment and dyes used for rendering.  COMPONENT TYPE: CharacterRenderData | [optional] 
**activities** | **object** | Activity data - info about current activities available to the player.  COMPONENT TYPE: CharacterActivities | [optional] 
**equipment** | **object** | Equipped items on the character.  COMPONENT TYPE: CharacterEquipment | [optional] 
**kiosks** | **object** | Items available from Kiosks that are available to this specific character.   COMPONENT TYPE: Kiosks | [optional] 
**item_components** | **object** | The set of components belonging to the player&#39;s instanced items.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


