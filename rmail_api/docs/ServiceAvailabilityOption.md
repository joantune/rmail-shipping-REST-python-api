# ServiceAvailabilityOption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code** | **str** | Service Code&lt;br /&gt;Customer Mapped Service Code or System Service Code for this service. | 
**service_name** | **str** | Service Name | 
**transit_days** | **int** | Estimated Transit Days | 
**is_tracked** | **bool** | Is Tracked&lt;br /&gt;If true, the service is a tracked service. | 
**signature_included** | **bool** | Signature Included&lt;br /&gt;If true, a signature required on delivery is included with the service. | 
**recorded_signed_for_available** | **bool** | Recorded Signed For Enhancement Available&lt;br /&gt;If true, the recorded signed for enhancement can be used with this service. | 
**safeplace_available** | **bool** | Safe Place Enhancement Available&lt;br /&gt;If true, the safe place enhancement can be used with this service. | 
**local_collect_available** | **bool** | Local Collect Enhancement Available&lt;br /&gt;If true, the local collect enhancement can be used with this service. | 
**saturday_guaranteed_available** | **bool** | Saturday Guaranteed Enhancement Available&lt;br /&gt;If true, the saturday guaranteed enhancement can be used with this service. | 
**consequential_loss_available** | **bool** | Consequential Loss Enhancement Available&lt;br /&gt;If true, the consequential loss enhancement can be used with this service. | 
**formats_available** | [**list[ServiceAvailabilityFormat]**](ServiceAvailabilityFormat.md) | Formats Available&lt;br /&gt;All formats that are available for this service for the given weight, including the maximum weight possible for each format. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

