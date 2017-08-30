# DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_entry_hash** | **int** | The identifier for this reward entry.  Runtime data will refer to reward entriesby this hash.  Only guaranteed unique within the specific Milestone. | [optional] 
**reward_entry_identifier** | **str** | The string identifier, if you care about it.  Only guaranteed unique within the specific Milestone. | [optional] 
**items** | [**list[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | The items you will get as rewards, and how much of it you&#39;ll get. | [optional] 
**vendor_hash** | **int** | If this reward is redeemed at a Vendor, this is the hash of the Vendor to go to in orderto redeem the reward.  Use this hash to look up the DestinyVendorDefinition. | [optional] 
**order** | **int** | If you want to follow BNet&#39;s ordering of these rewards, use this number within a given categoryto order the rewards.  Yeah, I know.  I feel dirty too. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


