# PreAllocateTrackingNumberRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_location_id** | **str** | Shipping Location the shipment is being shipped from. This can be populated with either the Shipping Location ID assigned by PRO SHIPPING or the Shipping Location Alias set when the Shipping Location was created. Both can be viewed in the Shipping Location GUI. &lt;br /&gt;Mandatory if there is more than one Shipping Location available for the Shipping Account | [optional] 
**shipping_account_id** | **str** | Shipping Account the shipment is being created for. This can be populated with either the Shipping Account ID assigned by PRO SHIPPING Shipping Account ID or the Shipping Account Alias set when the Shipping Account was created.Both can be viewed in the Shipping Account GUI. | 
**service_code** | **str** | The code of the shipping service used to deliver the shipment. | 
**service_level** | **str** | The Royal Mail service level of the service specified in the ServiceCode field. &lt;br /&gt;Valid values are 01-99. &lt;br /&gt;Defaults to lowest service level available for the specified service if not provided. | [optional] 
**service_enhancement_code** | [**RoyalMailPreAllocatedTrackingNumberEnhancementCode**](RoyalMailPreAllocatedTrackingNumberEnhancementCode.md) |  | [optional] 
**destination** | [**DestinationDetails**](DestinationDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

