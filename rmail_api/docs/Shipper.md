# Shipper

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | Shipper Address Id&lt;br /&gt;If supplied all shipper address fields will be ignored and the address from the Address Book will be used. | [optional] 
**shipper_reference** | **str** | Shipper Reference&lt;br /&gt;Your reference for this shipment.&lt;br /&gt;This field is used for Returns processing and is usually the shippers order number provided to the consumer. | [optional] 
**shipper_department** | **str** | Shipper Department Code&lt;br /&gt;For Royal Mail shipments, this code must be a valid 10-digit OBA department code. | [optional] 
**company_name** | **str** | Company Name | [optional] 
**contact_name** | **str** | Contact Name | [optional] 
**address_line1** | **str** | Address Line 1&lt;br /&gt;Populate with Shipper&#x27;s address if provided. | [optional] 
**address_line2** | **str** | Address Line 2 | [optional] 
**address_line3** | **str** | Address Line 3 | [optional] 
**town** | **str** | Town&lt;br /&gt;Required if address is populated. | [optional] 
**county** | **str** | County / State / Province&lt;br /&gt;Whether this is required or not is dependent on the country settings. | [optional] 
**country_code** | **str** | Country Code&lt;br /&gt;[ISO Alpha-2 Country Code](https://www.nationsonline.org/oneworld/country_code_list.htm) per ISO 3166 Standard.&lt;br /&gt;Required if address is populated.&lt;br /&gt;Must be GB, IM, GG or JE. | [optional] 
**postcode** | **str** | Postcode / Zip&lt;br /&gt;Mandatory for all domestic addresses and some international shipments if address is populated. | [optional] 
**phone_number** | **str** | Contact Phone Number&lt;br /&gt;Must be a valid phone number. | [optional] 
**email_address** | **str** | Contact Email Address&lt;br /&gt;Must be a valid email address. | [optional] 
**vat_number** | **str** | VAT Number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

