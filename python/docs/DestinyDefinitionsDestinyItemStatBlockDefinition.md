# DestinyDefinitionsDestinyItemStatBlockDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_group_hash** | **int** | If the item&#39;s stats are meant to be modified by a DestinyStatGroupDefinition, this willbe the identifier for that definition.  If you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.statsproperty, you don&#39;t have to worry about statGroupHash and how it alters stats: the already alteredstats are provided to you.  But if you want to see how the sausage gets made, or perform computationsyourself, this is valuable information. | [optional] 
**stats** | [**dict(str, DestinyDefinitionsDestinyInventoryItemStatDefinition)**](DestinyDefinitionsDestinyInventoryItemStatDefinition.md) | If you are looking for precomputed values for the stats on a weapon, this is where they are stored.Technically these are the \&quot;Display\&quot; stat values.  Please see DestinyStatsDefinition for whatDisplay Stat Values means, it&#39;s a very long story... but essentially these are the closest valuesBNet can get to the item stats that you see in-game.  These stats are keyed by the DestinyStatDefinition&#39;s hash identifier for the statthat&#39;s found on the item. | [optional] 
**has_displayable_stats** | **bool** | A quick and lazy way to determine whether any stat other than the \&quot;primary\&quot; stat is actuallyvisible on the item.  Items often have stats that we return in case people find them useful, butthey&#39;re not part of the \&quot;Stat Group\&quot; and thus we wouldn&#39;t display them in our UI.  If this is False,then we&#39;re not going to display any of these stats other than the primary one. | [optional] 
**primary_base_stat_hash** | **int** | This stat is determined to be the \&quot;primary\&quot; stat, and can be looked up in the stats or anyother stat collection related to the item.  Use this hash to look up the stat&#39;s value using DestinyInventoryItemDefinition.stats.stats,and the renderable data for the primary stat in the related DestinyStatDefinition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


