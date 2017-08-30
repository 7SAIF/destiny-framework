# DestinyDefinitionsDestinyNodeStepDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_index** | **int** | The index of this step in the list of Steps on the Talent Node.  Unfortunately, this is the closest thing we have to an identifier for the Step:steps are not provided a content version agnostic identifier.  This means that,when you are dealing with talent nodes, you will need to first ensure that you havethe latest version of content. | [optional] 
**node_step_hash** | **int** | The hash of this node step.  Unfortunately, while it can be used to uniquely identifythe step within a node, it is also content version dependent and should not be relied onwithout ensuring you have the latest vesion of content. | [optional] 
**interaction_description** | **str** | If you can interact with this node in some way, this is the localized descriptionof that interaction. | [optional] 
**damage_type_hash** | **int** | If the step provides a damage type, this will be the hash identifier used to look upthe damage type&#39;s DestinyDamageTypeDefinition. | [optional] 
**can_activate_next_step** | **bool** | There was a time when talent nodes could be activated multiple times, andthe effects of subsequent Steps would be compounded on each other, essentially\&quot;upgrading\&quot; the node.  We have moved away from this, but theoretically the capabilitystill exists.  I continue to return this in case it is used in the future: if true andthis step is the current step in the node, you are allowed to activate the nodea second time to receive the benefits of the next step in the node, which will thenbecome the active step. | [optional] 
**next_step_index** | **int** | The stepIndex of the next step in the talent node, or -1 if this is the last step or ifthe next step to be chosen is random.  This doesn&#39;t really matter anymore unless canActivateNextStep begins to be used again. | [optional] 
**is_next_step_random** | **bool** | If true, the next step to be chosen is random, and if you&#39;re allowed to activate thenext step. (if canActivateNextStep &#x3D; true) | [optional] 
**perk_hashes** | **list[int]** | The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are appliedwhen this step is active.  Perks provide a variety of benefits and modifications - examineDestinySandboxPerkDefinition to learn more. | [optional] 
**start_progression_bar_at_progress** | **int** | When the Talent Grid&#39;s progression reaches this value, the circular \&quot;progress bar\&quot; thatsurrounds the talent node should be shown.  This also indicates the lower bound of saidprogress bar, with the upper bound being the progress required to reach activationRequirement.gridLevel. (at some point I should precalculate the upper bound and putit in the definition to save people time) | [optional] 
**stat_hashes** | **list[int]** | When the step provides stat benefits on the item or character, this is the list of hash identifiersfor stats (DestinyStatDefinition) that are provided. | [optional] 
**affects_quality** | **bool** | If this is true, the step affects the item&#39;s Quality in some way.  See DestinyInventoryItemDefinitionfor more information about the meaning of Quality.  I already made a joke about Zen and the Art ofMotorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again.  Oops too late | [optional] 
**affects_level** | **bool** | If true, this step can affect the level of the item.  See DestinyInventoryItemDefintion for moreinformation about item levels and their effect on stats. | [optional] 
**socket_replacements** | [**list[DestinyDefinitionsDestinyNodeSocketReplaceResponse]**](DestinyDefinitionsDestinyNodeSocketReplaceResponse.md) | If this step is activated, this will be a list of information used to replace socket itemswith new Plugs.  See DestinyInventoryItemDefinition for more information about sockets and plugs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


