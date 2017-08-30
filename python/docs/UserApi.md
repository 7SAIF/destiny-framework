# swagger_client.UserApi

All URIs are relative to *https://https://bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_available_themes**](UserApi.md#user_get_available_themes) | **GET** /User/GetAvailableThemes/ | 
[**user_get_bungie_net_user_by_id**](UserApi.md#user_get_bungie_net_user_by_id) | **GET** /User/GetBungieNetUserById/{id}/ | 
[**user_get_membership_data_by_id**](UserApi.md#user_get_membership_data_by_id) | **GET** /User/GetMembershipsById/{membershipId}/{membershipType}/ | 
[**user_get_membership_data_for_current_user**](UserApi.md#user_get_membership_data_for_current_user) | **GET** /User/GetMembershipsForCurrentUser/ | 
[**user_get_partnerships**](UserApi.md#user_get_partnerships) | **GET** /User/{membershipId}/Partnerships/ | 
[**user_get_user_aliases**](UserApi.md#user_get_user_aliases) | **GET** /User/GetUserAliases/{id}/ | 
[**user_search_users**](UserApi.md#user_search_users) | **GET** /User/SearchUsers/ | 


# **user_get_available_themes**
> InlineResponse2003 user_get_available_themes()



Returns a list of all available user themes.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try: 
    api_response = api_instance.user_get_available_themes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_available_themes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_bungie_net_user_by_id**
> InlineResponse200 user_get_bungie_net_user_by_id(id)



Loads a bungienet user by membership id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 789 # int | The requested Bungie.net membership id.

try: 
    api_response = api_instance.user_get_bungie_net_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_bungie_net_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The requested Bungie.net membership id. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_membership_data_by_id**
> InlineResponse2004 user_get_membership_data_by_id(membership_id, membership_type)



Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
membership_id = 789 # int | The membership ID of the target user.
membership_type = 'membership_type_example' # str | Type of the supplied membership ID.

try: 
    api_response = api_instance.user_get_membership_data_by_id(membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_membership_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The membership ID of the target user. | 
 **membership_type** | **str**| Type of the supplied membership ID. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_membership_data_for_current_user**
> InlineResponse2004 user_get_membership_data_for_current_user()



Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

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
api_instance = swagger_client.UserApi()

try: 
    api_response = api_instance.user_get_membership_data_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_membership_data_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_partnerships**
> InlineResponse2005 user_get_partnerships(membership_id)



Returns a user's linked Partnerships.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
membership_id = 789 # int | The ID of the member for whom partnerships should be returned.

try: 
    api_response = api_instance.user_get_partnerships(membership_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_partnerships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **int**| The ID of the member for whom partnerships should be returned. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_user_aliases**
> InlineResponse2001 user_get_user_aliases(id)



Loads aliases of a bungienet membership id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 789 # int | The requested Bungie.net membership id.

try: 
    api_response = api_instance.user_get_user_aliases(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_user_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The requested Bungie.net membership id. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search_users**
> InlineResponse2002 user_search_users(search, q=q)



Returns a list of possible users based on the search string

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
search = 'search_example' # str | The search string.
q = 'q_example' # str |  (optional)

try: 
    api_response = api_instance.user_search_users(search, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| The search string. | 
 **q** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

