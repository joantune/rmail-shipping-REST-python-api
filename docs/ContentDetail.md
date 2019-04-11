# ContentDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_manufacture_code** | **str** | 2-digit country ISO code representing the country in which the goods where manufactured. Note that this field is case sensitive. For the list of allowable values, please go to API Shipping V2 page on the Royal Mail API (Developer) Portal and refer to API Shipping Reference Data. | 
**manufacturers_name** | **str** | Name of manufacturer of goods in the shipment. | [optional] 
**description** | **str** | Description of goods being delivered. | [optional] 
**unit_weight** | [**Measurement**](Measurement.md) |  | [optional] 
**unit_quantity** | **int** | Quantity of content items within the shipment. | 
**unit_value** | [**BigDecimal**](BigDecimal.md) | Value of content items within the shipment. | 
**currency_code** | **str** | 3-digit ISO currency code for value of content item within the shipment. | 
**tariff_code** | [**BigDecimal**](BigDecimal.md) | Tariff code for content item within the shipment. See https&amp;#58;//www.gov.uk/trade-tariff. | [optional] 
**tariff_description** | **str** | Description that compliments the tariff code supplied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

