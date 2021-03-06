# GroupsV2GroupResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**GroupsV2GroupV2**](GroupsV2GroupV2.md) |  | [optional] 
**founder** | [**GroupsV2GroupMember**](GroupsV2GroupMember.md) |  | [optional] 
**allied_ids** | **list[int]** |  | [optional] 
**parent_group** | [**GroupsV2GroupV2**](GroupsV2GroupV2.md) |  | [optional] 
**alliance_status** | [**GroupsV2GroupAllianceStatus**](GroupsV2GroupAllianceStatus.md) |  | [optional] 
**group_join_invite_count** | **int** |  | [optional] 
**current_user_member_map** | [**dict(str, GroupsV2GroupMember)**](GroupsV2GroupMember.md) | This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available. | [optional] 
**current_user_potential_member_map** | [**dict(str, GroupsV2GroupPotentialMember)**](GroupsV2GroupPotentialMember.md) | This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


