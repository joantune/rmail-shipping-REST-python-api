# RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consignment_shipment_id** | **str** | Consignment Shipment Id &lt;br /&gt;Only populated if the service is a consignment service. | [optional] 
**consignment_tracking_number** | **str** | Consignment Tracking Number &lt;br /&gt;Only populated if the service is a consignment service | [optional] 
**consignment_carrier_tracking_url** | **str** | Consignment Carrier Tracking URL &lt;br /&gt;Only populated if the service is a consignment service and is available | [optional] 
**labels** | **str** | Labels &lt;br /&gt;Populated if requested Action was &#x27;Process&#x27; | [optional] 
**label_format** | [**RoyalMailLabelFormat**](RoyalMailLabelFormat.md) |  | [optional] 
**packages** | [**list[RoyalMailShipmentResponseCarrierSpecificsPackageResponse]**](RoyalMailShipmentResponseCarrierSpecificsPackageResponse.md) | Packages &lt;br /&gt;The details of each package. | [optional] 
**documents** | **str** | Customs Documents &lt;br /&gt;Populated if requested Action was &#x27;Process&#x27; and shipment is dutiable | [optional] 
**document_format** | [**DocumentFormat**](DocumentFormat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

