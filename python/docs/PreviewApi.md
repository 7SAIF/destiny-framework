# swagger_client.PreviewApi

All URIs are relative to *https://bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destiny2_activate_talent_node**](PreviewApi.md#destiny2_activate_talent_node) | **POST** /Destiny2/Actions/Items/ActivateTalentNode/ | 
[**destiny2_get_activity_history**](PreviewApi.md#destiny2_get_activity_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
[**destiny2_get_clan_aggregate_stats**](PreviewApi.md#destiny2_get_clan_aggregate_stats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
[**destiny2_get_clan_leaderboards**](PreviewApi.md#destiny2_get_clan_leaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
[**destiny2_get_destiny_aggregate_activity_stats**](PreviewApi.md#destiny2_get_destiny_aggregate_activity_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
[**destiny2_get_historical_stats**](PreviewApi.md#destiny2_get_historical_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
[**destiny2_get_historical_stats_for_account**](PreviewApi.md#destiny2_get_historical_stats_for_account) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
[**destiny2_get_leaderboards**](PreviewApi.md#destiny2_get_leaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
[**destiny2_get_leaderboards_for_character**](PreviewApi.md#destiny2_get_leaderboards_for_character) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**destiny2_get_unique_weapon_history**](PreviewApi.md#destiny2_get_unique_weapon_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
[**destiny2_get_vendor**](PreviewApi.md#destiny2_get_vendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
[**destiny2_get_vendors**](PreviewApi.md#destiny2_get_vendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
[**destiny2_insert_socket_plug**](PreviewApi.md#destiny2_insert_socket_plug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
[**destiny2_search_destiny_entities**](PreviewApi.md#destiny2_search_destiny_entities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 


# **destiny2_activate_talent_node**
> InlineResponse20020 destiny2_activate_talent_node()



Activate a Talent Node.  Chill out, everyone: we haven't decided yet whether this will be able to activate nodes with costs, but if we do it will require special scope permission for an application attempting to do so.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.  PREVIEW: This service is not actually implemented yet, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

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
api_instance = swagger_client.PreviewApi()

try: 
    api_response = api_instance.destiny2_activate_talent_node()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_activate_talent_node: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_activity_history**
> InlineResponse20029 destiny2_get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)



Gets activity history stats for indicated character.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The id of the character to retrieve.
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
count = 56 # int | Number of rows to return (optional)
mode = 56 # int | A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. (optional)
page = 56 # int | Page number to return, starting with 0. (optional)

try: 
    api_response = api_instance.destiny2_get_activity_history(character_id, destiny_membership_id, membership_type, count=count, mode=mode, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_activity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **count** | **int**| Number of rows to return | [optional] 
 **mode** | **int**| A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. | [optional] 
 **page** | **int**| Page number to return, starting with 0. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_clan_aggregate_stats**
> InlineResponse20025 destiny2_get_clan_aggregate_stats(group_id, modes=modes)



Gets aggregated stats for a clan using the same categories as the clan leaderboards.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
group_id = 789 # int | Group ID of the clan whose leaderboards you wish to fetch.
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)

try: 
    api_response = api_instance.destiny2_get_clan_aggregate_stats(group_id, modes=modes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_clan_aggregate_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_clan_leaderboards**
> InlineResponse20024 destiny2_get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
group_id = 789 # int | Group ID of the clan whose leaderboards you wish to fetch.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_response = api_instance.destiny2_get_clan_leaderboards(group_id, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_clan_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_destiny_aggregate_activity_stats**
> InlineResponse20031 destiny2_get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)



Gets all activities the character has participated in together with aggregate statistics for those activities.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The specific character whose activities should be returned.
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.

try: 
    api_response = api_instance.destiny2_get_destiny_aggregate_activity_stats(character_id, destiny_membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_destiny_aggregate_activity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The specific character whose activities should be returned. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_historical_stats**
> InlineResponse20027 destiny2_get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)



Gets historical stats for indicated character.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
dayend = '2013-10-20T19:20:30+01:00' # datetime | Last day to return when daily stats are requested.  Use the format YYYY-MM-DD. (optional)
daystart = '2013-10-20T19:20:30+01:00' # datetime | First day to return when daily stats are requested. Use the format YYYY-MM-DD (optional)
groups = [swagger_client.DestinyHistoricalStatsDefinitionsDestinyStatsGroupType()] # list[DestinyHistoricalStatsDefinitionsDestinyStatsGroupType] | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals (optional)
modes = [swagger_client.DestinyHistoricalStatsDefinitionsDestinyActivityModeType()] # list[DestinyHistoricalStatsDefinitionsDestinyActivityModeType] | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
period_type = 56 # int | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity (optional)

try: 
    api_response = api_instance.destiny2_get_historical_stats(character_id, destiny_membership_id, membership_type, dayend=dayend, daystart=daystart, groups=groups, modes=modes, period_type=period_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_historical_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **dayend** | **datetime**| Last day to return when daily stats are requested.  Use the format YYYY-MM-DD. | [optional] 
 **daystart** | **datetime**| First day to return when daily stats are requested. Use the format YYYY-MM-DD | [optional] 
 **groups** | [**list[DestinyHistoricalStatsDefinitionsDestinyStatsGroupType]**](DestinyHistoricalStatsDefinitionsDestinyStatsGroupType.md)| Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals | [optional] 
 **modes** | [**list[DestinyHistoricalStatsDefinitionsDestinyActivityModeType]**](DestinyHistoricalStatsDefinitionsDestinyActivityModeType.md)| Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **period_type** | **int**| Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_historical_stats_for_account**
> InlineResponse20028 destiny2_get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)



Gets aggregate historical stats organized around each character for a given account.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
groups = [swagger_client.DestinyHistoricalStatsDefinitionsDestinyStatsGroupType()] # list[DestinyHistoricalStatsDefinitionsDestinyStatsGroupType] | Groups of stats to include, otherwise only general stats are returned.  Comma separated list is allowed. Values: General, Weapons, Medals. (optional)

try: 
    api_response = api_instance.destiny2_get_historical_stats_for_account(destiny_membership_id, membership_type, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_historical_stats_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **groups** | [**list[DestinyHistoricalStatsDefinitionsDestinyStatsGroupType]**](DestinyHistoricalStatsDefinitionsDestinyStatsGroupType.md)| Groups of stats to include, otherwise only general stats are returned.  Comma separated list is allowed. Values: General, Weapons, Medals. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_leaderboards**
> InlineResponse20024 destiny2_get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint has not yet been implemented.  It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_response = api_instance.destiny2_get_leaderboards(destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_leaderboards_for_character**
> InlineResponse20024 destiny2_get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)



Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The specific character to build the leaderboard around for the provided Destiny Membership.
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.
maxtop = 56 # int | Maximum number of top players to return. Use a large number to get entire leaderboard. (optional)
modes = 'modes_example' # str | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. (optional)
statid = 'statid_example' # str | ID of stat to return rather than returning all Leaderboard stats. (optional)

try: 
    api_response = api_instance.destiny2_get_leaderboards_for_character(character_id, destiny_membership_id, membership_type, maxtop=maxtop, modes=modes, statid=statid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_leaderboards_for_character: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The specific character to build the leaderboard around for the provided Destiny Membership. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **maxtop** | **int**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **str**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **str**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_unique_weapon_history**
> InlineResponse20030 destiny2_get_unique_weapon_history(character_id, destiny_membership_id, membership_type)



Gets details about unique weapon usage, including all exotic weapons.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is in final form, but there may be bugs that prevent desirable operation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The id of the character to retrieve.
destiny_membership_id = 789 # int | The Destiny membershipId of the user to retrieve.
membership_type = 56 # int | A valid non-BungieNet membership type.

try: 
    api_response = api_instance.destiny2_get_unique_weapon_history(character_id, destiny_membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_unique_weapon_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The id of the character to retrieve. | 
 **destiny_membership_id** | **int**| The Destiny membershipId of the user to retrieve. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_vendor**
> InlineResponse20019 destiny2_get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)



Get the details of a specific Vendor.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 789 # int | Destiny membership ID of another user. You may be denied.
membership_type = 56 # int | A valid non-BungieNet membership type.
vendor_hash = 56 # int | The Hash identifier of the Vendor to be returned.
components = [swagger_client.DestinyDestinyComponentType()] # list[DestinyDestinyComponentType] | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_response = api_instance.destiny2_get_vendor(character_id, destiny_membership_id, membership_type, vendor_hash, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **int**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **vendor_hash** | **int**| The Hash identifier of the Vendor to be returned. | 
 **components** | [**list[DestinyDestinyComponentType]**](DestinyDestinyComponentType.md)| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_get_vendors**
> InlineResponse20018 destiny2_get_vendors(character_id, destiny_membership_id, membership_type, components=components)



Get currently available vendors.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
character_id = 789 # int | The Destiny Character ID of the character for whom we're getting vendor info.
destiny_membership_id = 789 # int | Destiny membership ID of another user. You may be denied.
membership_type = 56 # int | A valid non-BungieNet membership type.
components = [swagger_client.DestinyDestinyComponentType()] # list[DestinyDestinyComponentType] | A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. (optional)

try: 
    api_response = api_instance.destiny2_get_vendors(character_id, destiny_membership_id, membership_type, components=components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destiny_membership_id** | **int**| Destiny membership ID of another user. You may be denied. | 
 **membership_type** | **int**| A valid non-BungieNet membership type. | 
 **components** | [**list[DestinyDestinyComponentType]**](DestinyDestinyComponentType.md)| A comma separated list of components to return (as strings or numeric values).  See the DestinyComponentType enum for valid components to request.  You must request at least one component to receive results. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_insert_socket_plug**
> InlineResponse20020 destiny2_insert_socket_plug()



Insert a plug into a socketed item.  I know how it sounds, but I assure you it's much more G-rated than you might be guessing.  We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so.  You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.  PREVIEW: This service is not yet active, but we are returning the planned schema of the endpoint for review, comment, and preparation for its eventual implementation.

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
api_instance = swagger_client.PreviewApi()

try: 
    api_response = api_instance.destiny2_insert_socket_plug()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_insert_socket_plug: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destiny2_search_destiny_entities**
> InlineResponse20026 destiny2_search_destiny_entities(search_term, type, page=page)



Gets a page list of Destiny items.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreviewApi()
search_term = 'search_term_example' # str | The string to use when searching for Destiny entities.
type = 'type_example' # str | The type of entity for whom you would like results.  These correspond to the entity's definition contract name.  For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
page = 56 # int | Page number to return, starting with 0. (optional)

try: 
    api_response = api_instance.destiny2_search_destiny_entities(search_term, type, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreviewApi->destiny2_search_destiny_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The string to use when searching for Destiny entities. | 
 **type** | **str**| The type of entity for whom you would like results.  These correspond to the entity&#39;s definition contract name.  For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;.  PREVIEW: This endpoint is still in beta, and may experience rough edges.  The schema is tentatively in final form, but there may be bugs that prevent desirable operation. | 
 **page** | **int**| Page number to return, starting with 0. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

