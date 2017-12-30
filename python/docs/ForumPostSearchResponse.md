# ForumPostSearchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_posts** | [**list[ForumPostResponse]**](ForumPostResponse.md) |  | [optional] 
**authors** | [**list[UserGeneralUser]**](UserGeneralUser.md) |  | [optional] 
**groups** | [**list[GroupsV2GroupResponse]**](GroupsV2GroupResponse.md) |  | [optional] 
**searched_tags** | [**list[TagsModelsContractsTagResponse]**](TagsModelsContractsTagResponse.md) |  | [optional] 
**polls** | [**list[ForumPollResponse]**](ForumPollResponse.md) |  | [optional] 
**recruitment_details** | [**list[ForumForumRecruitmentDetail]**](ForumForumRecruitmentDetail.md) |  | [optional] 
**available_pages** | **int** |  | [optional] 
**results** | [**list[ForumPostResponse]**](ForumPostResponse.md) |  | [optional] 
**total_results** | **int** |  | [optional] 
**has_more** | **bool** |  | [optional] 
**query** | [**QueriesPagedQuery**](QueriesPagedQuery.md) |  | [optional] 
**replacement_continuation_token** | **str** |  | [optional] 
**use_total_results** | **bool** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


