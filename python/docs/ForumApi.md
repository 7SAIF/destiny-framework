# swagger_client.ForumApi

All URIs are relative to *https://https://bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forum_approve_fireteam_thread**](ForumApi.md#forum_approve_fireteam_thread) | **POST** /Forum/Recruit/Approve/{topicId}/ | 
[**forum_get_core_topics_paged**](ForumApi.md#forum_get_core_topics_paged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ | 
[**forum_get_forum_tag_suggestions**](ForumApi.md#forum_get_forum_tag_suggestions) | **GET** /Forum/GetForumTagSuggestions/ | 
[**forum_get_poll**](ForumApi.md#forum_get_poll) | **GET** /Forum/Poll/{topicId}/ | 
[**forum_get_post_and_parent**](ForumApi.md#forum_get_post_and_parent) | **GET** /Forum/GetPostAndParent/{childPostId}/ | 
[**forum_get_post_and_parent_awaiting_approval**](ForumApi.md#forum_get_post_and_parent_awaiting_approval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ | 
[**forum_get_posts_threaded_paged**](ForumApi.md#forum_get_posts_threaded_paged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ | 
[**forum_get_posts_threaded_paged_from_child**](ForumApi.md#forum_get_posts_threaded_paged_from_child) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ | 
[**forum_get_recruitment_thread_summaries**](ForumApi.md#forum_get_recruitment_thread_summaries) | **POST** /Forum/Recruit/Summaries/ | 
[**forum_get_topic_for_content**](ForumApi.md#forum_get_topic_for_content) | **GET** /Forum/GetTopicForContent/{contentId}/ | 
[**forum_get_topics_paged**](ForumApi.md#forum_get_topics_paged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ | 
[**forum_join_fireteam_thread**](ForumApi.md#forum_join_fireteam_thread) | **POST** /Forum/Recruit/Join/{topicId}/ | 
[**forum_kick_ban_fireteam_applicant**](ForumApi.md#forum_kick_ban_fireteam_applicant) | **POST** /Forum/Recruit/KickBan/{topicId}/{targetMembershipId}/ | 
[**forum_leave_fireteam_thread**](ForumApi.md#forum_leave_fireteam_thread) | **POST** /Forum/Recruit/Leave/{topicId}/ | 


# **forum_approve_fireteam_thread**
> InlineResponse20010 forum_approve_fireteam_thread(topic_id)



Allows the owner of a fireteam thread to approve all joined members and start a private message conversation with them.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 789 # int | The post id of the recruitment topic to approve.

try: 
    api_response = api_instance.forum_approve_fireteam_thread(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_approve_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| The post id of the recruitment topic to approve. | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_core_topics_paged**
> InlineResponse2006 forum_get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)



Gets a listing of all topics marked as part of the core group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
category_filter = 'category_filter_example' # str | The category filter.
page = 56 # int | Zero base page
quick_date = 'quick_date_example' # str | The date filter.
sort = 'sort_example' # str | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)

try: 
    api_response = api_instance.forum_get_core_topics_paged(category_filter, page, quick_date, sort, locales=locales)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_core_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **str**| The category filter. | 
 **page** | **int**| Zero base page | 
 **quick_date** | **str**| The date filter. | 
 **sort** | **str**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_forum_tag_suggestions**
> InlineResponse2008 forum_get_forum_tag_suggestions(partialtag=partialtag)



Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
partialtag = 'partialtag_example' # str | The partial tag input to generate suggestions from. (optional)

try: 
    api_response = api_instance.forum_get_forum_tag_suggestions(partialtag=partialtag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_forum_tag_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partialtag** | **str**| The partial tag input to generate suggestions from. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_poll**
> InlineResponse2006 forum_get_poll(topic_id)



Gets the specified forum poll.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 789 # int | The post id of the topic that has the poll.

try: 
    api_response = api_instance.forum_get_poll(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| The post id of the topic that has the poll. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_post_and_parent**
> InlineResponse2006 forum_get_post_and_parent(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_response = api_instance.forum_get_post_and_parent(child_post_id, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_post_and_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_post_and_parent_awaiting_approval**
> InlineResponse2006 forum_get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)



Returns the post specified and its immediate parent of posts that are awaiting approval.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 56 # int | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_response = api_instance.forum_get_post_and_parent_awaiting_approval(child_post_id, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_post_and_parent_awaiting_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_posts_threaded_paged**
> InlineResponse2006 forum_get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
get_parent_post = true # bool | 
page = 56 # int | 
page_size = 56 # int | 
parent_post_id = 56 # int | 
reply_size = 56 # int | 
root_thread_mode = true # bool | 
sort_mode = 'sort_mode_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_response = api_instance.forum_get_posts_threaded_paged(get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_posts_threaded_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_parent_post** | **bool**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 
 **parent_post_id** | **int**|  | 
 **reply_size** | **int**|  | 
 **root_thread_mode** | **bool**|  | 
 **sort_mode** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_posts_threaded_paged_from_child**
> InlineResponse2006 forum_get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)



Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
child_post_id = 56 # int | 
page = 56 # int | 
page_size = 56 # int | 
reply_size = 56 # int | 
root_thread_mode = true # bool | 
sort_mode = 'sort_mode_example' # str | 
showbanned = 'showbanned_example' # str | If this value is not null or empty, banned posts are requested to be returned (optional)

try: 
    api_response = api_instance.forum_get_posts_threaded_paged_from_child(child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=showbanned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_posts_threaded_paged_from_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_post_id** | **int**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 
 **reply_size** | **int**|  | 
 **root_thread_mode** | **bool**|  | 
 **sort_mode** | **str**|  | 
 **showbanned** | **str**| If this value is not null or empty, banned posts are requested to be returned | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_recruitment_thread_summaries**
> InlineResponse20011 forum_get_recruitment_thread_summaries()



Allows the caller to get a list of to 25 recruitment thread summary information objects.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()

try: 
    api_response = api_instance.forum_get_recruitment_thread_summaries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_recruitment_thread_summaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_topic_for_content**
> InlineResponse2007 forum_get_topic_for_content(content_id)



Gets the post Id for the given content item's comments, if it exists.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
content_id = 789 # int | 

try: 
    api_response = api_instance.forum_get_topic_for_content(content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_topic_for_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **int**|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_get_topics_paged**
> InlineResponse2006 forum_get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)



Get topics from any forum.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ForumApi()
category_filter = 'category_filter_example' # str | A category filter
group = 789 # int | The group, if any.
page = 56 # int | Zero paged page number
page_size = 56 # int | Unused
quick_date = 'quick_date_example' # str | A date filter.
sort = 'sort_example' # str | The sort mode.
locales = 'locales_example' # str | Comma seperated list of locales posts must match to return in the result list. Default 'en' (optional)
tagstring = 'tagstring_example' # str | The tags to search, if any. (optional)

try: 
    api_response = api_instance.forum_get_topics_paged(category_filter, group, page, page_size, quick_date, sort, locales=locales, tagstring=tagstring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_get_topics_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_filter** | **str**| A category filter | 
 **group** | **int**| The group, if any. | 
 **page** | **int**| Zero paged page number | 
 **page_size** | **int**| Unused | 
 **quick_date** | **str**| A date filter. | 
 **sort** | **str**| The sort mode. | 
 **locales** | **str**| Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39; | [optional] 
 **tagstring** | **str**| The tags to search, if any. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_join_fireteam_thread**
> InlineResponse2009 forum_join_fireteam_thread(topic_id)



Allows a user to slot themselves into a recuritment thread fireteam slot. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 789 # int | The post id of the recruitment topic you wish to join.

try: 
    api_response = api_instance.forum_join_fireteam_thread(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_join_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| The post id of the recruitment topic you wish to join. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_kick_ban_fireteam_applicant**
> InlineResponse2009 forum_kick_ban_fireteam_applicant(target_membership_id, topic_id)



Allows a recruitment thread owner to kick a join user from the fireteam. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ForumApi()
target_membership_id = 789 # int | The id of the user you wish to kick.
topic_id = 789 # int | The post id of the recruitment topic you wish to join.

try: 
    api_response = api_instance.forum_kick_ban_fireteam_applicant(target_membership_id, topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_kick_ban_fireteam_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_membership_id** | **int**| The id of the user you wish to kick. | 
 **topic_id** | **int**| The post id of the recruitment topic you wish to join. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forum_leave_fireteam_thread**
> InlineResponse2009 forum_leave_fireteam_thread(topic_id)



Allows a user to remove themselves from a recuritment thread fireteam slot. Returns the new state of the fireteam.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ForumApi()
topic_id = 789 # int | The post id of the recruitment topic you wish to leave.

try: 
    api_response = api_instance.forum_leave_fireteam_thread(topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForumApi->forum_leave_fireteam_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| The post id of the recruitment topic you wish to leave. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

