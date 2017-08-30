# DestinyEntitiesVendorsDestinyVendorComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_hash** | **int** | The unique identifier for the vendor.  Use it to look up their DestinyVendorDefinition. | [optional] 
**next_refresh_date** | **datetime** | The date when this vendor&#39;s inventory will next rotate/refresh. | [optional] 
**enabled** | **bool** | If True, the Vendor is currently accessible.    If False, they may not actually be visible in the world at the moment. | [optional] 
**can_purchase** | **bool** | If True, you can purchase from the Vendor.  Theoretically, Vendors can be restricted from selling items.  In practice, none do that (yet?). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


