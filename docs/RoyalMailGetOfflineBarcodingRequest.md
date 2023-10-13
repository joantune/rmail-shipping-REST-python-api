# RoyalMailGetOfflineBarcodingRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_location_id** | **str** | This can be populated with either the Shipping Location ID assigned by PRO SHIPPING or the Shipping Location Alias set when the Shipping Location was created. Optional if the shipping account only has one Shipping Location assigned. If the Shipping Account has multiple Shipping Locations, then this field must be populated. | [optional] 
**shipping_account_id** | **str** | Shipping Account the number range is being requested for. This can be populated with either the Shipping Account ID assigned by PRO SHIPPING or the Shipping Account Alias set when the Shipping Account was created. | 
**service_code** | **str** | Service Code | 
**service_level** | **str** | The Royal Mail service level of the service specified in the ServiceCode field. &lt;br /&gt;Valid values are 01-99. | 
**service_enhancement_code** | [**RoyalMailOfflineBarcodingEnhancementCode**](RoyalMailOfflineBarcodingEnhancementCode.md) |  | [optional] 
**channel_id** | **str** | The Channel ID agreed with Royal Mail for the offline barcodes. If no value is sent in the request then the Channel ID assigned in PRO SHIPPING will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

