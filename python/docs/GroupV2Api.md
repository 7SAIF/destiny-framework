# swagger_client.GroupV2Api

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_v2_abdicate_foundership**](GroupV2Api.md#group_v2_abdicate_foundership) | **POST** /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/ | 
[**group_v2_add_optional_conversation**](GroupV2Api.md#group_v2_add_optional_conversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Add/ | 
[**group_v2_approve_all_pending**](GroupV2Api.md#group_v2_approve_all_pending) | **POST** /GroupV2/{groupId}/Members/ApproveAll/ | 
[**group_v2_approve_pending**](GroupV2Api.md#group_v2_approve_pending) | **POST** /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/ | 
[**group_v2_approve_pending_for_list**](GroupV2Api.md#group_v2_approve_pending_for_list) | **POST** /GroupV2/{groupId}/Members/ApproveList/ | 
[**group_v2_ban_member**](GroupV2Api.md#group_v2_ban_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/ | 
[**group_v2_create_group**](GroupV2Api.md#group_v2_create_group) | **POST** /GroupV2/Create/ | 
[**group_v2_deny_all_pending**](GroupV2Api.md#group_v2_deny_all_pending) | **POST** /GroupV2/{groupId}/Members/DenyAll/ | 
[**group_v2_deny_pending_for_list**](GroupV2Api.md#group_v2_deny_pending_for_list) | **POST** /GroupV2/{groupId}/Members/DenyList/ | 
[**group_v2_edit_clan_banner**](GroupV2Api.md#group_v2_edit_clan_banner) | **POST** /GroupV2/{groupId}/EditClanBanner/ | 
[**group_v2_edit_founder_options**](GroupV2Api.md#group_v2_edit_founder_options) | **POST** /GroupV2/{groupId}/EditFounderOptions/ | 
[**group_v2_edit_group**](GroupV2Api.md#group_v2_edit_group) | **POST** /GroupV2/{groupId}/Edit/ | 
[**group_v2_edit_group_membership**](GroupV2Api.md#group_v2_edit_group_membership) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/ | 
[**group_v2_edit_optional_conversation**](GroupV2Api.md#group_v2_edit_optional_conversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/ | 
[**group_v2_get_admins_and_founder_of_group**](GroupV2Api.md#group_v2_get_admins_and_founder_of_group) | **GET** /GroupV2/{groupId}/AdminsAndFounder/ | 
[**group_v2_get_available_avatars**](GroupV2Api.md#group_v2_get_available_avatars) | **GET** /GroupV2/GetAvailableAvatars/ | 
[**group_v2_get_available_themes**](GroupV2Api.md#group_v2_get_available_themes) | **GET** /GroupV2/GetAvailableThemes/ | 
[**group_v2_get_banned_members_of_group**](GroupV2Api.md#group_v2_get_banned_members_of_group) | **GET** /GroupV2/{groupId}/Banned/ | 
[**group_v2_get_group**](GroupV2Api.md#group_v2_get_group) | **GET** /GroupV2/{groupId}/ | 
[**group_v2_get_group_by_name**](GroupV2Api.md#group_v2_get_group_by_name) | **GET** /GroupV2/Name/{groupName}/{groupType}/ | 
[**group_v2_get_group_optional_conversations**](GroupV2Api.md#group_v2_get_group_optional_conversations) | **GET** /GroupV2/{groupId}/OptionalConversations/ | 
[**group_v2_get_groups_for_member**](GroupV2Api.md#group_v2_get_groups_for_member) | **GET** /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**group_v2_get_invited_individuals**](GroupV2Api.md#group_v2_get_invited_individuals) | **GET** /GroupV2/{groupId}/Members/InvitedIndividuals/ | 
[**group_v2_get_members_of_group**](GroupV2Api.md#group_v2_get_members_of_group) | **GET** /GroupV2/{groupId}/Members/ | 
[**group_v2_get_pending_memberships**](GroupV2Api.md#group_v2_get_pending_memberships) | **GET** /GroupV2/{groupId}/Members/Pending/ | 
[**group_v2_get_potential_groups_for_member**](GroupV2Api.md#group_v2_get_potential_groups_for_member) | **GET** /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**group_v2_get_recommended_groups**](GroupV2Api.md#group_v2_get_recommended_groups) | **POST** /GroupV2/Recommended/{groupType}/{createDateRange}/ | 
[**group_v2_get_user_clan_invite_setting**](GroupV2Api.md#group_v2_get_user_clan_invite_setting) | **GET** /GroupV2/GetUserClanInviteSetting/{mType}/ | 
[**group_v2_group_search**](GroupV2Api.md#group_v2_group_search) | **POST** /GroupV2/Search/ | 
[**group_v2_individual_group_invite**](GroupV2Api.md#group_v2_individual_group_invite) | **POST** /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/ | 
[**group_v2_individual_group_invite_cancel**](GroupV2Api.md#group_v2_individual_group_invite_cancel) | **POST** /GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/ | 
[**group_v2_kick_member**](GroupV2Api.md#group_v2_kick_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/ | 
[**group_v2_request_group_membership**](GroupV2Api.md#group_v2_request_group_membership) | **POST** /GroupV2/{groupId}/Members/Apply/{membershipType}/ | 
[**group_v2_rescind_group_membership**](GroupV2Api.md#group_v2_rescind_group_membership) | **POST** /GroupV2/{groupId}/Members/Rescind/{membershipType}/ | 
[**group_v2_set_user_clan_invite_setting**](GroupV2Api.md#group_v2_set_user_clan_invite_setting) | **POST** /GroupV2/SetUserClanInviteSetting/{mType}/{allowInvites}/ | 
[**group_v2_unban_member**](GroupV2Api.md#group_v2_unban_member) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/ | 


# **group_v2_abdicate_foundership**
> InlineResponse20014 group_v2_abdicate_foundership(founder_id_new, group_id, membership_type)



An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
founder_id_new = 789 # int | The new founder for this group. Must already be a group admin.
group_id = 789 # int | The target group id.
membership_type = 56 # int | Membership type of the provided founderIdNew.

try:
    api_response = api_instance.group_v2_abdicate_foundership(founder_id_new, group_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_abdicate_foundership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **founder_id_new** | **int**| The new founder for this group. Must already be a group admin. | 
 **group_id** | **int**| The target group id. | 
 **membership_type** | **int**| Membership type of the provided founderIdNew. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_add_optional_conversation**
> InlineResponse2007 group_v2_add_optional_conversation(group_id)



Add a new optional conversation/chat channel. Requires admin permissions to the group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID of the group to edit.

try:
    api_response = api_instance.group_v2_add_optional_conversation(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_add_optional_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_approve_all_pending**
> InlineResponse20026 group_v2_approve_all_pending(group_id)



Approve all of the pending users for the given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_approve_all_pending(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_approve_all_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_approve_pending**
> InlineResponse20014 group_v2_approve_pending(group_id, membership_id, membership_type)



Approve the given membershipId to join the group/clan as long as they have applied.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.
membership_id = 789 # int | The membership id being approved.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.group_v2_approve_pending(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_approve_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **membership_id** | **int**| The membership id being approved. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_approve_pending_for_list**
> InlineResponse20026 group_v2_approve_pending_for_list(group_id)



Approve all of the pending users for the given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_approve_pending_for_list(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_approve_pending_for_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_ban_member**
> InlineResponse20015 group_v2_ban_member(group_id, membership_id, membership_type)



Bans the requested member from the requested group for the specified period of time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID that has the member to ban.
membership_id = 789 # int | Membership ID of the member to ban from the group.
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.group_v2_ban_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_ban_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID that has the member to ban. | 
 **membership_id** | **int**| Membership ID of the member to ban from the group. | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_create_group**
> InlineResponse20020 group_v2_create_group()



Create a new group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.group_v2_create_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_create_group: %s\n" % e)
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

# **group_v2_deny_all_pending**
> InlineResponse20026 group_v2_deny_all_pending(group_id)



Deny all of the pending users for the given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_deny_all_pending(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_deny_all_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_deny_pending_for_list**
> InlineResponse20026 group_v2_deny_pending_for_list(group_id)



Deny all of the pending users for the given group that match the passed-in .

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_deny_pending_for_list(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_deny_pending_for_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_edit_clan_banner**
> InlineResponse20015 group_v2_edit_clan_banner(group_id)



Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID of the group to edit.

try:
    api_response = api_instance.group_v2_edit_clan_banner(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_edit_clan_banner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_edit_founder_options**
> InlineResponse20015 group_v2_edit_founder_options(group_id)



Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID of the group to edit.

try:
    api_response = api_instance.group_v2_edit_founder_options(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_edit_founder_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_edit_group**
> InlineResponse20015 group_v2_edit_group(group_id)



Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID of the group to edit.

try:
    api_response = api_instance.group_v2_edit_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_edit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID of the group to edit. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_edit_group_membership**
> InlineResponse20015 group_v2_edit_group_membership(group_id, membership_id, membership_type, member_type)



Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group to which the member belongs.
membership_id = 789 # int | Membership ID to modify.
membership_type = 56 # int | Membership type of the provide membership ID.
member_type = 56 # int | New membertype for the specified member.

try:
    api_response = api_instance.group_v2_edit_group_membership(group_id, membership_id, membership_type, member_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_edit_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group to which the member belongs. | 
 **membership_id** | **int**| Membership ID to modify. | 
 **membership_type** | **int**| Membership type of the provide membership ID. | 
 **member_type** | **int**| New membertype for the specified member. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_edit_optional_conversation**
> InlineResponse2007 group_v2_edit_optional_conversation(conversation_id, group_id)



Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
conversation_id = 789 # int | Conversation Id of the channel being edited.
group_id = 789 # int | Group ID of the group to edit.

try:
    api_response = api_instance.group_v2_edit_optional_conversation(conversation_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_edit_optional_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **int**| Conversation Id of the channel being edited. | 
 **group_id** | **int**| Group ID of the group to edit. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_admins_and_founder_of_group**
> InlineResponse20021 group_v2_get_admins_and_founder_of_group(currentpage, group_id)



Get the list of members in a given group who are of admin level or higher.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 789 # int | The ID of the group.

try:
    api_response = api_instance.group_v2_get_admins_and_founder_of_group(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_admins_and_founder_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| The ID of the group. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_available_avatars**
> InlineResponse20012 group_v2_get_available_avatars()



Returns a list of all available group avatars for the signed-in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()

try:
    api_response = api_instance.group_v2_get_available_avatars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_available_avatars: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_available_themes**
> InlineResponse20013 group_v2_get_available_themes()



Returns a list of all available group themes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()

try:
    api_response = api_instance.group_v2_get_available_themes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_available_themes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_banned_members_of_group**
> InlineResponse20023 group_v2_get_banned_members_of_group(currentpage, group_id)



Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 entries.
group_id = 789 # int | Group ID whose banned members you are fetching

try:
    api_response = api_instance.group_v2_get_banned_members_of_group(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_banned_members_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 entries. | 
 **group_id** | **int**| Group ID whose banned members you are fetching | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_group**
> InlineResponse20018 group_v2_get_group(group_id)



Get information about a specific group of the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
group_id = 789 # int | Requested group's id.

try:
    api_response = api_instance.group_v2_get_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Requested group&#39;s id. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_group_by_name**
> InlineResponse20018 group_v2_get_group_by_name(group_name, group_type)



Get information about a specific group with the given name and type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
group_name = 'group_name_example' # str | Exact name of the group to find.
group_type = 56 # int | Type of group to find.

try:
    api_response = api_instance.group_v2_get_group_by_name(group_name, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_group_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Exact name of the group to find. | 
 **group_type** | **int**| Type of group to find. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_group_optional_conversations**
> InlineResponse20019 group_v2_get_group_optional_conversations(group_id)



Gets a list of available optional conversation channels and their settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
group_id = 789 # int | Requested group's id.

try:
    api_response = api_instance.group_v2_get_group_optional_conversations(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_group_optional_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Requested group&#39;s id. | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_groups_for_member**
> InlineResponse20027 group_v2_get_groups_for_member(filter, group_type, membership_id, membership_type)



Get information about the groups that a given member has joined.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
filter = 56 # int | Filter apply to list of joined groups.
group_type = 56 # int | Type of group the supplied member founded.
membership_id = 789 # int | Membership ID to for which to find founded groups.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.group_v2_get_groups_for_member(filter, group_type, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_groups_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Filter apply to list of joined groups. | 
 **group_type** | **int**| Type of group the supplied member founded. | 
 **membership_id** | **int**| Membership ID to for which to find founded groups. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_invited_individuals**
> InlineResponse20025 group_v2_get_invited_individuals(currentpage, group_id)



Get the list of users who have been invited into the group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_get_invited_individuals(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_invited_individuals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_members_of_group**
> InlineResponse20021 group_v2_get_members_of_group(currentpage, group_id, member_type=member_type, name_search=name_search)



Get the list of members in a given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 789 # int | The ID of the group.
member_type = 56 # int | Filter out other member types. Use None for all members. (optional)
name_search = 'name_search_example' # str | The name fragment upon which a search should be executed for members with matching display or unique names. (optional)

try:
    api_response = api_instance.group_v2_get_members_of_group(currentpage, group_id, member_type=member_type, name_search=name_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_members_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| The ID of the group. | 
 **member_type** | **int**| Filter out other member types. Use None for all members. | [optional] 
 **name_search** | **str**| The name fragment upon which a search should be executed for members with matching display or unique names. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_pending_memberships**
> InlineResponse20025 group_v2_get_pending_memberships(currentpage, group_id)



Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
currentpage = 56 # int | Page number (starting with 1). Each page has a fixed size of 50 items per page.
group_id = 789 # int | ID of the group.

try:
    api_response = api_instance.group_v2_get_pending_memberships(currentpage, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_pending_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentpage** | **int**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **group_id** | **int**| ID of the group. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_potential_groups_for_member**
> InlineResponse20028 group_v2_get_potential_groups_for_member(filter, group_type, membership_id, membership_type)



Get information about the groups that a given member has applied to or been invited to.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()
filter = 56 # int | Filter apply to list of potential joined groups.
group_type = 56 # int | Type of group the supplied member applied.
membership_id = 789 # int | Membership ID to for which to find applied groups.
membership_type = 56 # int | Membership type of the supplied membership ID.

try:
    api_response = api_instance.group_v2_get_potential_groups_for_member(filter, group_type, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_potential_groups_for_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Filter apply to list of potential joined groups. | 
 **group_type** | **int**| Type of group the supplied member applied. | 
 **membership_id** | **int**| Membership ID to for which to find applied groups. | 
 **membership_type** | **int**| Membership type of the supplied membership ID. | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_recommended_groups**
> InlineResponse20016 group_v2_get_recommended_groups(create_date_range, group_type)



Gets groups recommended for you based on the groups to whom those you follow belong.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
create_date_range = 56 # int | Requested range in which to pull recommended groups
group_type = 56 # int | Type of groups requested

try:
    api_response = api_instance.group_v2_get_recommended_groups(create_date_range, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_recommended_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_date_range** | **int**| Requested range in which to pull recommended groups | 
 **group_type** | **int**| Type of groups requested | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_get_user_clan_invite_setting**
> InlineResponse20014 group_v2_get_user_clan_invite_setting(m_type)



Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
m_type = 56 # int | The Destiny membership type of the account we wish to access settings.

try:
    api_response = api_instance.group_v2_get_user_clan_invite_setting(m_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_get_user_clan_invite_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **m_type** | **int**| The Destiny membership type of the account we wish to access settings. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_group_search**
> InlineResponse20017 group_v2_group_search()



Search for Groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupV2Api()

try:
    api_response = api_instance.group_v2_group_search()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_group_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_individual_group_invite**
> InlineResponse20024 group_v2_individual_group_invite(group_id, membership_id, membership_type)



Invite a user to join this group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group you would like to join.
membership_id = 789 # int | Membership id of the account being invited.
membership_type = 56 # int | MembershipType of the account being invited.

try:
    api_response = api_instance.group_v2_individual_group_invite(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_individual_group_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group you would like to join. | 
 **membership_id** | **int**| Membership id of the account being invited. | 
 **membership_type** | **int**| MembershipType of the account being invited. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_individual_group_invite_cancel**
> InlineResponse20024 group_v2_individual_group_invite_cancel(group_id, membership_id, membership_type)



Cancels a pending invitation to join a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group you would like to join.
membership_id = 789 # int | Membership id of the account being cancelled.
membership_type = 56 # int | MembershipType of the account being cancelled.

try:
    api_response = api_instance.group_v2_individual_group_invite_cancel(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_individual_group_invite_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group you would like to join. | 
 **membership_id** | **int**| Membership id of the account being cancelled. | 
 **membership_type** | **int**| MembershipType of the account being cancelled. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_kick_member**
> InlineResponse20022 group_v2_kick_member(group_id, membership_id, membership_type)



Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | Group ID to kick the user from.
membership_id = 789 # int | Membership ID to kick.
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.group_v2_kick_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_kick_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID to kick the user from. | 
 **membership_id** | **int**| Membership ID to kick. | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_request_group_membership**
> InlineResponse20024 group_v2_request_group_membership(group_id, membership_type)



Request permission to join the given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group you would like to join.
membership_type = 56 # int | MembershipType of the account to use when joining.

try:
    api_response = api_instance.group_v2_request_group_membership(group_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_request_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group you would like to join. | 
 **membership_type** | **int**| MembershipType of the account to use when joining. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_rescind_group_membership**
> InlineResponse20022 group_v2_rescind_group_membership(group_id, membership_type)



Rescind your application to join the given group or leave the group if you are already a member..

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | ID of the group.
membership_type = 56 # int | MembershipType of the account to leave.

try:
    api_response = api_instance.group_v2_rescind_group_membership(group_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_rescind_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the group. | 
 **membership_type** | **int**| MembershipType of the account to leave. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_set_user_clan_invite_setting**
> InlineResponse20015 group_v2_set_user_clan_invite_setting(allow_invites, m_type)



Sets the state of the user's clan invite preferences - true if they wish to be invited to clans, false otherwise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
allow_invites = true # bool | True to allow invites of this user to clans, false otherwise.
m_type = 56 # int | The Destiny membership type of linked account we are manipulating.

try:
    api_response = api_instance.group_v2_set_user_clan_invite_setting(allow_invites, m_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_set_user_clan_invite_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_invites** | **bool**| True to allow invites of this user to clans, false otherwise. | 
 **m_type** | **int**| The Destiny membership type of linked account we are manipulating. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_v2_unban_member**
> InlineResponse20015 group_v2_unban_member(group_id, membership_id, membership_type)



Unbans the requested member, allowing them to re-apply for membership.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GroupV2Api(swagger_client.ApiClient(configuration))
group_id = 789 # int | 
membership_id = 789 # int | Membership ID of the member to unban from the group
membership_type = 56 # int | Membership type of the provided membership ID.

try:
    api_response = api_instance.group_v2_unban_member(group_id, membership_id, membership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupV2Api->group_v2_unban_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **membership_id** | **int**| Membership ID of the member to unban from the group | 
 **membership_type** | **int**| Membership type of the provided membership ID. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

