# DestinyMilestonesDestinyMilestoneActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_hash** | **int** | The hash of an arbitrarily chosen variant of this activity.  We&#39;ll go ahead andcall that the \&quot;canonical\&quot; activity, because if you&#39;re using this value you shouldonly use it for properties that are common across the variants: things like thename of the activity, it&#39;s location, etc...Use this hash to look up the DestinyActivityDefinition of this activity for rendering data. | [optional] 
**modifier_hashes** | **list[int]** | If the activity has modifiers, this will be the list of modifiers that all variantshave in common.  Perform lookups againstDestinyActivityModifierDefinition which defines the modifier being applied to getat the modifier data.Note that, in the DestiyActivityDefinition, you will see many more modifiers than thisbeing referred to: those are all *possible* modifiers for the activity, not the active ones.Use only the active ones to match what&#39;s really live. | [optional] 
**variants** | [**list[DestinyMilestonesDestinyMilestoneActivityVariant]**](DestinyMilestonesDestinyMilestoneActivityVariant.md) | If you want more than just name/location/etc... you&#39;re going to have to dig intoand show the variants of the conceptual activity.  These will differ in seeminglyarbitrary ways, like difficulty level and modifiers applied.  Show it in whateverway tickles your fancy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


