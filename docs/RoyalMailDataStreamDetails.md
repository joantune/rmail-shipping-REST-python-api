# RoyalMailDataStreamDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary2_d_barcode_image** | **str** | Primary 2D Barcode Image &lt;br /&gt;Base64 Encoded PNG Image of the 2D data matrix barcode. | 
**primary2_d_barcode_data** | **str** | Primary 2D Barcode Data - Base 64 Encoded &lt;br /&gt;Data required to create your own 2D data matrix barcode. Please decode before use. | 
**formatted_unique_id** | **str** | Formatted Unique Id &lt;br /&gt;Label for 2D data matrix barcode. | 
**gazetteer_codes** | [**RoyalMailGazetteerCodes**](RoyalMailGazetteerCodes.md) |  | [optional] 
**primary1_d_barcode_image** | **str** | Primary 1D Barcode Image &lt;br /&gt;Only populated where the service requires the barcode on the label. &lt;br /&gt;Base64 Encoded PNG Image of the barcode. | [optional] 
**primary1_d_barcode_data** | **str** | Primary 1D Barcode Data &lt;br /&gt;Only populated where the service requires the barcode on the label. &lt;br /&gt;Data required to create your own barcode. | [optional] 
**high_volume_barcode_image** | **str** | High Volume Barcode Image &lt;br /&gt;Only populated where the service (Tracked High Volume) requires the barcode on the label. &lt;br /&gt;Base64 Encoded PNG Image of the barcode. | [optional] 
**high_volume_barcode_data** | **str** | High Volume Barcode Data &lt;br /&gt;Only populated where the service (Tracked High Volume) requires the barcode on the label. &lt;br /&gt;Data required to create your own barcode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

