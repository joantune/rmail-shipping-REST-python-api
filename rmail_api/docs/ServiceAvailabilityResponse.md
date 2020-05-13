# ServiceAvailabilityResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight_unit_of_measure** | **str** | Weight Unit of Measure&lt;br /&gt;The unit of measure used for the Max Weights.&lt;br /&gt;Will be the same as the Weight Unit of Measure received. | [optional] 
**options** | [**list[ServiceAvailabilityOption]**](ServiceAvailabilityOption.md) | Service Options&lt;br /&gt;The available service options that can be used for the details provided.&lt;br /&gt;Populated for successful responses only. | [optional] 
**http_status_code** | **int** | HTTP Status Code | 
**http_status_description** | **str** | HTTP Status Description | 
**message** | **str** | Message&lt;br /&gt;Successful response may include a success message.&lt;br /&gt;Failure responses will have general reason as to why. Further details may be contained in the list of errors. | [optional] 
**errors** | [**list[ErrorDetail]**](ErrorDetail.md) | Errors&lt;br /&gt;Details about why a request failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

