# RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_information** | [**RoyalMailLabelFormatShipmentInformation**](RoyalMailLabelFormatShipmentInformation.md) |  | 
**shipper** | [**Shipper**](Shipper.md) |  | 
**destination** | [**Destination**](Destination.md) |  | 
**carrier_specifics** | [**RoyalMailShipmentRequestCarrierSpecifics**](RoyalMailShipmentRequestCarrierSpecifics.md) |  | [optional] 
**packages** | [**list[RoyalMailPackage]**](RoyalMailPackage.md) | Shipment Packages &lt;br /&gt;The packages that are being sent in this shipment. &lt;br /&gt;There must be at least 1 package. &lt;br /&gt;A maximum of 99 packages is allowed. | 
**items** | [**list[Item]**](Item.md) | Shipment Items &lt;br /&gt;The items contained in the shipment, i.e. the goods/products being shipped  &lt;br /&gt;Item information is required for dutiable shipments for customs purposes. &lt;br /&gt;Non-Dutiable shipments and &#x27;Documents Only&#x27; (DOX) shipments do not require item information. &lt;br /&gt;If Item Verification check on shipment creation is enabled, the maximum number of distinct items that will be verified in one shipment is 15. | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**return_to_sender** | [**ReturnToSender**](ReturnToSender.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

