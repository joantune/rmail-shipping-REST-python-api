# Address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building_name** | **str** | This field will be used if supplied but is not necessary to process a shipment. It does not replace the need for a full addressLine1 input. | [optional] 
**building_number** | **str** | This field will be used if supplied but is not necessary to process a shipment. It does not replace the need for a full addressLine1 input. | [optional] 
**address_line1** | **str** | First line of the address. | 
**address_line2** | **str** | Second line of the address | [optional] 
**address_line3** | **str** | Third line of the address | [optional] 
**post_town** | **str** | Town or City. The postTown will be updated to match the postTown resolved postcode. | 
**county** | **str** | County of address. Mandatory for state &amp; provinces in the US, Canada or Australia. | [optional] 
**post_code** | **str** | Mandatory for UK addresses. If the Shipment Type is “Return” then this must match the postcode of the registered return address. | 
**country_code** | **str** | The relevant country&#x27;s 2-digit ISO code for the address. Note that this field is case sensitive.   Optional for domestic shipments.    - If supplied, must be UK country code. One of GB,JE,GE or JM.  Mandatory for international shipments.    - DO NOT USE UK country codes. For the list of allowable values, please go to API Shipping V2 page on the Royal Mail API (Developer) Portal and refer to API Shipping Reference Data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

