# PrintLabelResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | Shipment Id&lt;br /&gt;Tracking Number or Unique Id of the shipment involved. | [optional] 
**label_image** | **str** | Label Image&lt;br /&gt;Depends on Label Image Format&lt;br /&gt;            &lt;br /&gt;**PDF**&lt;br /&gt;Base 64 encoded PDF&lt;br /&gt;            &lt;br /&gt;**PNG**&lt;br /&gt;Base 64 encoded PNG&lt;br /&gt;            &lt;br /&gt;**ZPL 300 / 203 dpi**&lt;br /&gt;Base 64 encoded PRN (text file)&lt;br /&gt;            &lt;br /&gt;**Data stream**&lt;br /&gt;Not Included | [optional] 
**label_image_format** | **str** | Label Image Format | [optional] 
**tracking_number** | **str** | Shipment Tracking Number&lt;br /&gt;Final Mile carrier tracking number | [optional] 
**unique_id** | **str** | Unique Shipment ID | [optional] 
**tracking_url** | **str** | Tracking URL&lt;br /&gt;Final Mile Tracking, if available | [optional] 
**carrier_code** | **str** | Carrier Code&lt;br /&gt;The allocated carrier. | [optional] 
**primary2_d_barcode_image** | **str** | Primary 2D Barcode Image&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Base64 Encoded PNG Image of the 2D data matrix barcode. | [optional] 
**primary2_d_barcode_data** | **str** | Primary 2D Barcode Data - Base 64 Encoded&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Data required to create your own 2D data matrix barcode. Please decode before use. | [optional] 
**formatted_unique_id** | **str** | Formatted Unique Id&lt;br /&gt;Only populated for Data Stream response.&lt;br /&gt;Label for 2D data matrix barcode. | [optional] 
**high_volume_barcode_data** | **str** | High Volume Barcode Data&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Data required to create your own High Volume barcode. | [optional] 
**high_volume_barcode_image** | **str** | High Volume Barcode Image&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Base64 Encoded PNG Image of the High Volume barcode. | [optional] 
**high_volume_sort_code** | **str** | High Volume Sort Code&lt;br /&gt;Only populated for Data Stream response where the service requires the sort code on the label. | [optional] 
**primary1_d_barcode_data** | **str** | Primary 1D Barcode Data&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Data required to create your own 1D barcode. | [optional] 
**primary1_d_barcode_image** | **str** | Primary 1D Barcode Image&lt;br /&gt;Only populated for Data Stream response where the service requires the barcode on the label.&lt;br /&gt;Base64 Encoded PNG Image of the 1D barcode. | [optional] 
**return_label_image_format** | **str** | Return Label Image Format | [optional] 
**return_label_image** | **str** | Return Label Image&lt;br /&gt;Any return label that have been created as a result of the request and label option settings.&lt;br /&gt;Depends on ReturnLabelImageFormat.&lt;br /&gt;            &lt;br /&gt;**PDF**&lt;br /&gt;Base 64 encoded PDF&lt;br /&gt;            &lt;br /&gt;**PNG**&lt;br /&gt;Base 64 encoded PNG&lt;br /&gt;            &lt;br /&gt;**ZPL 300 / 203 dpi**&lt;br /&gt;Base 64 encoded PRN (text file) | [optional] 
**http_status_code** | **int** | HTTP Status Code | 
**http_status_description** | **str** | HTTP Status Description | 
**message** | **str** | Message&lt;br /&gt;Successful response may include a success message.&lt;br /&gt;Failure responses will have general reason as to why. Further details may be contained in the list of errors. | [optional] 
**errors** | [**list[ErrorDetail]**](ErrorDetail.md) | Errors&lt;br /&gt;Details about why a request failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

