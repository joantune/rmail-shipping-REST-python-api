# PackageResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_occurance** | **int** | Package Occurence&lt;br /&gt;Unique package number within this shipment | 
**unique_id** | **str** | Unique Shipment ID&lt;br /&gt;All shipments are assigned a unique Shipment ID. | [optional] 
**tracking_number** | **str** | Shipment Tracking Number&lt;br /&gt;Final Mile carrier tracking number.&lt;br /&gt;Only populated for services that support tracking numbers. | [optional] 
**tracking_url** | **str** | Tracking URL&lt;br /&gt;Final Mile Tracking, if available. | [optional] 
**carrier_code** | **str** | Carrier Code&lt;br /&gt;The allocated carrier. | [optional] 
**primary2_d_barcode_image** | **str** | Primary 2D Barcode Image&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Base64 Encoded PNG Image of the 2D data matrix barcode. | [optional] 
**primary2_d_barcode_data** | **str** | Primary 2D Barcode Data - Base 64 Encoded&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Data required to create your own 2D data matrix barcode. Please decode before use. | [optional] 
**formatted_unique_id** | **str** | Formatted Unique Id&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Label for 2D data matrix barcode. | [optional] 
**high_volume_barcode_data** | **str** | High Volume Barcode Data&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Data required to create your own High Volume barcode. | [optional] 
**high_volume_barcode_image** | **str** | High Volume Barcode Image&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Base64 Encoded PNG Image of the High Volume barcode. | [optional] 
**high_volume_sort_code** | **str** | High Volume Sort Code&lt;br /&gt;Only populated for Data Stream response where the service requires the sort code on the label. | [optional] 
**primary1_d_barcode_data** | **str** | Primary 1D Barcode Data&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Data required to create your own 1D barcode. | [optional] 
**primary1_d_barcode_image** | **str** | Primary 1D Barcode Image&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Base64 Encoded PNG Image of the 1D barcode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

