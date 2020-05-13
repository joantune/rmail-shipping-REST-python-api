# ManifestResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posting_location** | **str** | Posting Location.&lt;br /&gt;The Posting Location manifested | 
**manifests** | [**list[Manifest]**](Manifest.md) | The Created Manifests&lt;br /&gt;Only populated if the request was successful. | [optional] 
**http_status_code** | **int** | HTTP Status Code | 
**http_status_description** | **str** | HTTP Status Description | 
**message** | **str** | Message&lt;br /&gt;Successful response may include a success message.&lt;br /&gt;Failure responses will have general reason as to why. Further details may be contained in the list of errors. | [optional] 
**errors** | [**list[ErrorDetail]**](ErrorDetail.md) | Errors&lt;br /&gt;Details about why a request failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

