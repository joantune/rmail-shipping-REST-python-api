# RoyalMailShipmentRequestCarrierSpecifics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_level** | **str** | The Royal Mail service level of the service specified in the ServiceCode field.  &lt;br /&gt;Valid values are 01-99. &lt;br /&gt;Defaults to lowest service level available for the specified service if not provided. | [optional] 
**ebay_vtn** | **str** | The eBay Virtual Tracking Number. This should be provided for all shipments that relate to orders created on eBay, so that the shipment tracking data can be made available on eBay. | [optional] 
**service_enhancements** | [**list[RoyalMailServiceEnhancement]**](RoyalMailServiceEnhancement.md) | Service Enhancements &lt;br /&gt;Any enhancements that you would like to add to the requested service. &lt;br /&gt;A maximum of 4 service enhancements can be used per shipment. | [optional] 
**offline_barcode** | [**RoyalMailOfflineBarcode**](RoyalMailOfflineBarcode.md) |  | [optional] 
**pre_allocated_tracking_number** | **str** | The pre-allocated tracking number to use for the shipment. Shipping Account, Shipping Location, Service Code, Destination Country and Postcode where required for the Country of Destination must match the one sent when the pre-allocation barcode was requested. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

