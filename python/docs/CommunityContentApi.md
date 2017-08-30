# swagger_client.CommunityContentApi

All URIs are relative to *https://https://bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**community_content_get_community_content**](CommunityContentApi.md#community_content_get_community_content) | **GET** /CommunityContent/Get/{sort}/{mediaFilter}/{page}/ | 
[**community_content_get_community_live_statuses**](CommunityContentApi.md#community_content_get_community_live_statuses) | **GET** /CommunityContent/Live/All/{partnershipType}/{sort}/{page}/ | 
[**community_content_get_community_live_statuses_for_clanmates**](CommunityContentApi.md#community_content_get_community_live_statuses_for_clanmates) | **GET** /CommunityContent/Live/Clan/{partnershipType}/{sort}/{page}/ | 
[**community_content_get_community_live_statuses_for_friends**](CommunityContentApi.md#community_content_get_community_live_statuses_for_friends) | **GET** /CommunityContent/Live/Friends/{partnershipType}/{sort}/{page}/ | 
[**community_content_get_featured_community_live_statuses**](CommunityContentApi.md#community_content_get_featured_community_live_statuses) | **GET** /CommunityContent/Live/Featured/{partnershipType}/{sort}/{page}/ | 
[**community_content_get_streaming_status_for_member**](CommunityContentApi.md#community_content_get_streaming_status_for_member) | **GET** /CommunityContent/Live/Users/{partnershipType}/{membershipType}/{membershipId}/ | 


# **community_content_get_community_content**
> InlineResponse2006 community_content_get_community_content(media_filter, page, sort)



Returns community content.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
media_filter = 'media_filter_example' # str | The type of media to get
page = 56 # int | Zero based page
sort = 'sort_example' # str | The sort mode.

try: 
    api_response = api_instance.community_content_get_community_content(media_filter, page, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_community_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_filter** | **str**| The type of media to get | 
 **page** | **int**| Zero based page | 
 **sort** | **str**| The sort mode. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_content_get_community_live_statuses**
> InlineResponse20032 community_content_get_community_live_statuses(page, partnership_type, sort, mode_hash=mode_hash, stream_locale=stream_locale)



Returns info about community members who are live streaming.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
page = 56 # int | Zero based page.
partnership_type = 'partnership_type_example' # str | The type of partnership for which the status should be returned.
sort = 'sort_example' # str | The sort mode.
mode_hash = 56 # int | The hash of the Activity Mode for which streams should be retrieved.  Don't pass it in or pass 0 to not filter by mode. (optional)
stream_locale = 'stream_locale_example' # str | The locale for streams you'd like to see.  Don't pass this to fall back on your BNet locale.  Pass 'ALL' to not filter by locale. (optional)

try: 
    api_response = api_instance.community_content_get_community_live_statuses(page, partnership_type, sort, mode_hash=mode_hash, stream_locale=stream_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_community_live_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **str**| The type of partnership for which the status should be returned. | 
 **sort** | **str**| The sort mode. | 
 **mode_hash** | **int**| The hash of the Activity Mode for which streams should be retrieved.  Don&#39;t pass it in or pass 0 to not filter by mode. | [optional] 
 **stream_locale** | **str**| The locale for streams you&#39;d like to see.  Don&#39;t pass this to fall back on your BNet locale.  Pass &#39;ALL&#39; to not filter by locale. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_content_get_community_live_statuses_for_clanmates**
> InlineResponse20032 community_content_get_community_live_statuses_for_clanmates(page, partnership_type, sort)



Returns info about community members who are live streaming in your clans.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
page = 56 # int | Zero based page.
partnership_type = 'partnership_type_example' # str | The type of partnership for which the status should be returned.
sort = 'sort_example' # str | The sort mode.

try: 
    api_response = api_instance.community_content_get_community_live_statuses_for_clanmates(page, partnership_type, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_community_live_statuses_for_clanmates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **str**| The type of partnership for which the status should be returned. | 
 **sort** | **str**| The sort mode. | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_content_get_community_live_statuses_for_friends**
> InlineResponse20032 community_content_get_community_live_statuses_for_friends(page, partnership_type, sort)



Returns info about community members who are live streaming among your friends.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
page = 56 # int | Zero based page.
partnership_type = 'partnership_type_example' # str | The type of partnership for which the status should be returned.
sort = 'sort_example' # str | The sort mode.

try: 
    api_response = api_instance.community_content_get_community_live_statuses_for_friends(page, partnership_type, sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_community_live_statuses_for_friends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **str**| The type of partnership for which the status should be returned. | 
 **sort** | **str**| The sort mode. | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_content_get_featured_community_live_statuses**
> InlineResponse20032 community_content_get_featured_community_live_statuses(page, partnership_type, sort, stream_locale=stream_locale)



Returns info about Featured live streams.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
page = 56 # int | Zero based page.
partnership_type = 'partnership_type_example' # str | The type of partnership for which the status should be returned.
sort = 'sort_example' # str | The sort mode.
stream_locale = 'stream_locale_example' # str | The locale for streams you'd like to see.  Don't pass this to fall back on your BNet locale.  Pass 'ALL' to not filter by locale. (optional)

try: 
    api_response = api_instance.community_content_get_featured_community_live_statuses(page, partnership_type, sort, stream_locale=stream_locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_featured_community_live_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero based page. | 
 **partnership_type** | **str**| The type of partnership for which the status should be returned. | 
 **sort** | **str**| The sort mode. | 
 **stream_locale** | **str**| The locale for streams you&#39;d like to see.  Don&#39;t pass this to fall back on your BNet locale.  Pass &#39;ALL&#39; to not filter by locale. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **community_content_get_streaming_status_for_member**
> InlineResponse20033 community_content_get_streaming_status_for_member(membership_id, membership_type, partnership_type)



Gets the Live Streaming status of a particular Account and Membership Type.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
membership_id = 789 # int | The membershipId related to that type.
membership_type = 'membership_type_example' # str | The type of account for which info will be extracted.
partnership_type = 'partnership_type_example' # str | The type of partnership for which info will be extracted.

try: 
    api_response = api_instance.community_content_get_streaming_status_for_member(membership_id, membership_type, partnership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_streaming_status_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The membershipId related to that type. | 
 **membership_type** | **str**| The type of account for which info will be extracted. | 
 **partnership_type** | **str**| The type of partnership for which info will be extracted. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

