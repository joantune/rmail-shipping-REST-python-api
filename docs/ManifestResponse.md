# ManifestResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_number** | **int** | The batch number of the manifest. It is a sequentially allocated number. Used in subsequent call to the create manifest label operation. | [optional] 
**count** | **int** | Total number of shipments on this manifest | [optional] 
**manifest** | **str** | Customer Collection Receipt in PDF format - Base64 encoded for transfer. Returned here when &#x27;Include the Manifest Image in &#x27;createManifest&#x27; response&#x27; is enabled in Pro Shipping GUI. | [optional] 
**shipments** | [**ManifestShipments**](ManifestShipments.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

