# RecipientAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building_name** | **str** | This field will be used if supplied but is not necessary to process a shipment. It does not replace the need for a full addressLine1 input. | [optional] 
**building_number** | **str** | This field will be used if supplied but is not necessary to process a shipment. It does not replace the need for a full addressLine1 input. | [optional] 
**address_line1** | **str** | First line of the address. | 
**address_line2** | **str** | Second line of the address | [optional] 
**address_line3** | **str** | Third line of the address | [optional] 
**state_or_province** | **str** | State or Province | [optional] 
**post_town** | **str** | Town or City. The postTown will be updated to match the postTown resolved postcode. | 
**county** | **str** | County of address. Mandatory for state &amp; provinces in the US, Canada or Australia. | [optional] 
**post_code** | **str** | Mandatory for UK addresses.  | 
**country** | **str** | Recipient 2-digit ISO country code. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

