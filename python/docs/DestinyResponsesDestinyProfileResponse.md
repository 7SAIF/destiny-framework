# DestinyResponsesDestinyProfileResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_receipts** | **object** | Recent, refundable purchases you have made from vendors. When will you use it? Couldn&#39;t say...  COMPONENT TYPE: VendorReceipts | [optional] 
**profile_inventory** | **object** | The profile-level inventory of the Destiny Profile.  COMPONENT TYPE: ProfileInventories | [optional] 
**profile_currencies** | **object** | The profile-level currencies owned by the Destiny Profile.  COMPONENT TYPE: ProfileCurrencies | [optional] 
**profile** | **object** | The basic information about the Destiny Profile (formerly \&quot;Account\&quot;).  COMPONENT TYPE: Profiles | [optional] 
**profile_kiosks** | **object** | Items available from Kiosks that are available Profile-wide (i.e. across all characters)  This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.  COMPONENT TYPE: Kiosks | [optional] 
**characters** | **object** | Basic information about each character, keyed by the CharacterId.  COMPONENT TYPE: Characters | [optional] 
**character_inventories** | **object** | The character-level non-equipped inventory items, keyed by the Character&#39;s Id.  COMPONENT TYPE: CharacterInventories | [optional] 
**character_progressions** | **object** | Character-level progression data, keyed by the Character&#39;s Id.  COMPONENT TYPE: CharacterProgressions | [optional] 
**character_render_data** | **object** | Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character&#39;s Id.  COMPONENT TYPE: CharacterRenderData | [optional] 
**character_activities** | **object** | Character activity data - the activities available to this character and its status, keyed by the Character&#39;s Id.  COMPONENT TYPE: CharacterActivities | [optional] 
**character_equipment** | **object** | The character&#39;s equipped items, keyed by the Character&#39;s Id.  COMPONENT TYPE: CharacterEquipment | [optional] 
**character_kiosks** | **object** | Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character&#39;s available items to check out of a kiosk.  This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.  COMPONENT TYPE: Kiosks | [optional] 
**item_components** | **object** | Information about instanced items across all returned characters, keyed by the item&#39;s instance ID.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


