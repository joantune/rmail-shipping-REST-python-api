# Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_code** | **str** | Stock Keeping Unit number of the item. | [optional] 
**package_occurrence** | **int** | Used to assign this item to a specific package. &lt;br /&gt;The Package Occurrence provided here must exist on one of the packages in the Package element.        &lt;br /&gt;Note: For dutiable multi-package shipments that are not using a consignment service, items must be assigned to a package so that accurate customs information is given. &lt;br /&gt;Therefore, if the shipment contains more than one package, and it isn&#x27;t using a consignment service, then Package Occurrence is required. | [optional] 
**quantity** | **int** | The quantity of these items in the package. | 
**description** | **str** | Description of the item. This must describe the specific item being shipped rather than the general nature of the goods e.g. &#x27;skirt&#x27; instead of &#x27;ladies clothing&#x27;. | [optional] 
**value** | **float** | The value of a single instance of the item, in the currency provided for the shipment in the CurrencyCode field. | [optional] 
**weight** | **float** | The weight of a single instance of the item, in the unit of measure provided in the WeightUnitOfMeasure element (defaults to KG). &lt;br /&gt;Required for dutiable shipments.  &lt;br /&gt;For non-dutiable shipments, a weight of 0 is accepted. For dutiable shipments, an item weight of 1 gram or greater must be provided.  &lt;br /&gt;The maximum weight accepted is 1000 KG. | [optional] 
**hs_code** | **str** | The Harmonized Commodity Description and Coding System Code. &lt;br /&gt;Used by Customs to calculate potential duties and taxes. &lt;br /&gt;May be required for dutiable shipments, depending on the carrier and destination country. &lt;br /&gt;The number of characters required for the HS Code may vary depending on the service and destination country. &lt;br /&gt;Dots and spaces in the HS Code are accepted. &lt;br /&gt;For more information on HS Codes and to find the correct HS Codes for your items, see https://www.gov.uk/trade-tariff | [optional] 
**country_of_origin** | **str** | Country the item was produced/manufactured in.  &lt;br /&gt;2 Digit ISO Country Code, per ISO 3166 Standard. &lt;br /&gt;May be required on dutiable shipments, depending on the carrier and destination country. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

