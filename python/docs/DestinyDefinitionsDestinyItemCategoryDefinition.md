# DestinyDefinitionsDestinyItemCategoryDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_properties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**visible** | **bool** | If True, this category should be visible in UI.  Sometimes we make categories that we  don&#39;t think are interesting externally.  It&#39;s up to you if you want to skip on showing them. | [optional] 
**short_title** | **str** | A shortened version of the title.  The reason why we have this is because the Armory in German  had titles that were too long to display in our UI, so these were localized abbreviated versions  of those categories.  The property still exists today, even though the Armory doesn&#39;t exist for D2... yet. | [optional] 
**item_type_regex** | **str** | The janky regular expression we used against the item type to try and discern whether  the item belongs to this category. | [optional] 
**item_type_regex_not** | **str** | If the item type matches this janky regex, it does *not* belong to this category. | [optional] 
**origin_bucket_identifier** | **str** | If the item belongs to this bucket, it does belong to this category. | [optional] 
**grouped_category_hashes** | **list[int]** | If this category is a \&quot;parent\&quot; category of other categories, those children will have their  hashes listed in rendering order here, and can be looked up using these hashes against  DestinyItemCategoryDefinition.    In this way, you can build up a visual hierarchy of item categories.  That&#39;s what we did,  and you can do it too.  I believe in you.  Yes, you, Carl.    (I hope someone named Carl reads this someday) | [optional] 
**hash** | **int** | The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.    When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **int** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **bool** | If this is true, then there is an entity with this identifier/type combination, but BNet is  not yet allowed to show it.  Sorry! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


