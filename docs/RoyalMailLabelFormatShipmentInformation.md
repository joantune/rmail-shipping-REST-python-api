# RoyalMailLabelFormatShipmentInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**CreateShipmentAction**](CreateShipmentAction.md) |  | [optional] 
**label_format** | [**RoyalMailLabelFormat**](RoyalMailLabelFormat.md) |  | [optional] 
**content_type** | [**ContentType**](ContentType.md) |  | 
**service_code** | **str** | The code of the shipping service used to deliver the shipment. | 
**description_of_goods** | **str** | A general description of the type of goods being sent. | 
**business_transaction_type** | [**BusinessTransactionType**](BusinessTransactionType.md) |  | [optional] 
**shipment_date** | **date** | The date the shipment packages will be shipped. &lt;br /&gt;Shipment Date cannot be in the past and cannot be more than 28 days in the future. &lt;br /&gt;Defaults to the current date if not populated. &lt;br /&gt;Accepted Format: YYYY-MM-DD | [optional] 
**declared_value** | **float** | The declared value of the total shipment in the currency specified. &lt;br /&gt;If provided, the value must be equal to or greater than the sum of all item values. &lt;br /&gt;If not provided it defaults to the sum of all item values. &lt;br /&gt;Ignored for Non-Consignment Services where multiple packages are declared - use the Declared Value at package level instead. | [optional] 
**declared_weight** | **float** | The declared weight of the total shipment in the unit of measure specified by WeightUnitOfMeasure (defaults to KG). &lt;br /&gt;The minimum weight allowed is 1 gram. &lt;br /&gt;The maximum weight is dependent on the carrier / service / destination. &lt;br /&gt;The weight must be equal to or greater than the sum of all package weights and/or item weights. &lt;br /&gt;Required for Consignment Services. &lt;br /&gt;Ignored for Non-Consignment Services - use the Declared Weight at package level instead. | [optional] 
**currency_code** | **str** | The currency code used for any monetary value related to the shipment. &lt;br /&gt;3 letter ISO Currency Code. &lt;br /&gt;*Required if any monetary values other than zero are provided.* | [optional] 
**weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**dimensions_unit_of_measure** | [**DimensionsUnitOfMeasure**](DimensionsUnitOfMeasure.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

