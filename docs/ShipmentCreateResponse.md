# ShipmentCreateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consignment_number** | **str** | Consignment Number&lt;br /&gt;Only populated for services that support Multi-Packages | [optional] 
**consignment_tracking_url** | **str** | Consignment Tracking URL&lt;br /&gt;Only populated for services that support Multi-Packages | [optional] 
**packages** | [**list[PackageResponse]**](PackageResponse.md) | Packages&lt;br /&gt;Details each package tracking information and Unique Id. | [optional] 
**routing** | [**RoutingResponse**](RoutingResponse.md) |  | [optional] 
**label_image_format** | **str** | Label Image Format | [optional] 
**label_images** | **str** | Label Images&lt;br /&gt;Any labels that have been created as a result of the request.&lt;br /&gt;Depends on Label Image Format.&lt;br /&gt;            &lt;br /&gt;**PDF**&lt;br /&gt;Base 64 encoded PDF&lt;br /&gt;            &lt;br /&gt;**PNG**&lt;br /&gt;Base 64 encoded PNG&lt;br /&gt;            &lt;br /&gt;**ZPL 300 / 203 dpi**&lt;br /&gt;Base 64 encoded PRN (text file)&lt;br /&gt;            &lt;br /&gt;**Data stream**&lt;br /&gt;Not Included - see Packages for Data Stream responses | [optional] 
**customs_documents** | **str** | Customs Documents&lt;br /&gt;Base 64 encoded PDF&lt;br /&gt;Any customs documents that have been created as a result of the request. | [optional] 
**return_label_image_format** | **str** | Return Label Image Format | [optional] 
**return_label_images** | **str** | Return Label Images&lt;br /&gt;Any return labels that have been created as a result of the request and label option settings.&lt;br /&gt;Depends on ReturnLabelImageFormat.&lt;br /&gt;            &lt;br /&gt;**PDF**&lt;br /&gt;Base 64 encoded PDF&lt;br /&gt;            &lt;br /&gt;**PNG**&lt;br /&gt;Base 64 encoded PNG&lt;br /&gt;            &lt;br /&gt;**ZPL 300 / 203 dpi**&lt;br /&gt;Base 64 encoded PRN (text file) | [optional] 
**http_status_code** | **int** | HTTP Status Code | 
**http_status_description** | **str** | HTTP Status Description | 
**message** | **str** | Message&lt;br /&gt;Successful response may include a success message.&lt;br /&gt;Failure responses will have general reason as to why. Further details may be contained in the list of errors. | [optional] 
**errors** | [**list[ErrorDetail]**](ErrorDetail.md) | Errors&lt;br /&gt;Details about why a request failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

