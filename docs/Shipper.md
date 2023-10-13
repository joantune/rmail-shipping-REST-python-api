# Shipper

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_account_id** | **str** | Shipping Account the shipment is being created for. This can be populated with either the Shipping Account ID assigned by PRO SHIPPING Shipping Account ID or the Shipping Account Alias set when the Shipping Account was created. Both can be viewed in the Shipping Account GUI. | 
**shipping_location_id** | **str** | Shipping Location the shipment is being shipped from. This can be populated with either the Shipping Location ID assigned by PRO SHIPPING or the Shipping Location Alias set when the Shipping Location was created.Both can be viewed in the Shipping Location GUI. &lt;br /&gt;Mandatory if there is more than one Shipping Location available for the Shipping Account. | [optional] 
**reference1** | **str** | The shipper&#x27;s reference for this shipment - this is usually the shipper&#x27;s order number that was provided to the consumer at the time the order was made. | [optional] 
**reference2** | **str** | Optional second reference for this shipment. | [optional] 
**department_number** | **str** | Department Number &lt;br /&gt;If provided for a Royal Mail shipment, Department Number must be exactly 10 characters and must be an existing Department Number that has been setup with Royal Mail. | [optional] 
**eori_number** | **str** | Shipper&#x27;s Economic Operators and Registration Identification (EORI) number. If a Shipper EORI number is used for the shipment, it must be provided here and not in the Customs element.  &lt;br /&gt;Shipper&#x27;s EORI number starts with the ISO Alpha-2 Country Code followed by a maximum 15 characters. For Northern Ireland starts with XI | [optional] 
**vat_number** | **str** | Shipper&#x27;s Value Added Tax (VAT) Number. If a Shipper VAT number is used for the shipment, it must be provided here and not in the Customs element. | [optional] 
**address** | [**ShipperAddress**](ShipperAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

