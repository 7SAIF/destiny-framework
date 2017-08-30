# DestinyDefinitionsDestinyStatDisplayDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_hash** | **int** | The hash identifier for the stat being transformed into a Display stat.  Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition&#39;sstats property. | [optional] 
**maximum_value** | **int** | Regardless of the output of interpolation, this is the maximum possible valuethat the stat can be.  It should also be used as the upper boundfor displaying the stat as a progress bar (the minimum always being 0) | [optional] 
**display_as_numeric** | **bool** | If this is true, the stat should be displayed as a number.  Otherwise, display it asa progress bar.  Or, you know, do whatever you want.  There&#39;s no displayAsNumericpolice. | [optional] 
**display_interpolation** | [**list[InterpolationInterpolationPoint]**](InterpolationInterpolationPoint.md) | The interpolation table representing how the Investment Stat is transformed intoa Display Stat.    See DestinyStatDefinition for a description of the stages ofstat transformation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


