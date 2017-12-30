# swagger_client.TrendingApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trending_get_trending_categories**](TrendingApi.md#trending_get_trending_categories) | **GET** /Trending/Categories/ | 
[**trending_get_trending_category**](TrendingApi.md#trending_get_trending_category) | **GET** /Trending/Categories/{categoryId}/{pageNumber}/ | 
[**trending_get_trending_entry_detail**](TrendingApi.md#trending_get_trending_entry_detail) | **GET** /Trending/Details/{trendingEntryType}/{identifier}/ | 


# **trending_get_trending_categories**
> InlineResponse20053 trending_get_trending_categories()



Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrendingApi()

try:
    api_response = api_instance.trending_get_trending_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->trending_get_trending_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_get_trending_category**
> InlineResponse20054 trending_get_trending_category(category_id, page_number)



Returns paginated lists of trending items for a category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrendingApi()
category_id = 'category_id_example' # str | The ID of the category for whom you want additional results.
page_number = 56 # int | The page # of results to return.

try:
    api_response = api_instance.trending_get_trending_category(category_id, page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->trending_get_trending_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**| The ID of the category for whom you want additional results. | 
 **page_number** | **int**| The page # of results to return. | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_get_trending_entry_detail**
> InlineResponse20055 trending_get_trending_entry_detail(identifier, trending_entry_type)



Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrendingApi()
identifier = 'identifier_example' # str | The identifier for the entity to be returned.
trending_entry_type = 56 # int | The type of entity to be returned.

try:
    api_response = api_instance.trending_get_trending_entry_detail(identifier, trending_entry_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrendingApi->trending_get_trending_entry_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The identifier for the entity to be returned. | 
 **trending_entry_type** | **int**| The type of entity to be returned. | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

