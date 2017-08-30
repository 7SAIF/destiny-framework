# DestinyDefinitionsDestinyObjectiveDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_value** | **int** | The value that the unlock value defined in unlockValueHash must reach in order forthe objective to be considered Completed.  Used in calculating progress and completion status. | [optional] 
**location_hash** | **int** | OPTIONAL: a hash identifier for the location at which this objective must be accomplished,if there is a location defined.  Look up the DestinyLocationDefinition for this hash for thatadditional location info. | [optional] 
**allow_negative_value** | **bool** | If true, the value is allowed to go negative. | [optional] 
**allow_value_change_when_completed** | **bool** | If true, you can effectively \&quot;un-complete\&quot; this objective if you lose progress aftercrossing the completion threshold.    If False, once you complete the task it will remaincompleted forever by locking the value. | [optional] 
**is_counting_downward** | **bool** | If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue. | [optional] 
**progress_description** | **str** | Text to describe the progress bar. | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


