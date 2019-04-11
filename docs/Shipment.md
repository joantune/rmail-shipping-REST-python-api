# Shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_type** | **str** | Specifies whether the shipment being created is a standard delivery service or a returns service. Accepted values are ‘Delivery’ and ‘Return’. Please note that this field is not case sensitive. | 
**service** | [**Service**](Service.md) |  | 
**shipping_date** | **str** | This is the date that the item will be physically sent (in the format YYYY-MM-DD). This may be up to 28 days in the future. Please note that for returns a Shipping date must be provided. | [optional] 
**items** | [**list[ShipmentRequestItem]**](ShipmentRequestItem.md) |  | [optional] 
**recipient_contact** | [**Contact**](Contact.md) |  | 
**recipient_address** | [**Address**](Address.md) |  | 
**sender_reference** | **str** | This field allows the user to supply their own reference number. Where supported (e.g. Tracked Returns) this number will appear on the label. | [optional] 
**department_reference** | **str** | This is the department reference code that customers can define in OBA. | [optional] 
**customer_reference** | **str** | This field allows customers to supply a reference that applies to multiple shipments and is included to mirror the functionality offered by the Customer Reference field in OBA, whereby a reference can be associated to a group of items. For references that apply to a single shipment, the senderReference field should be used. **Warning** Misuse of this field may result in incorrect billing. | [optional] 
**safe_place** | **str** | For Tracked non-signature service offerings only; this field allows a string that gives details of the recipient’s designated safeplace (e.g. “inside the porch”). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

