# ShipmentItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item ID&lt;br /&gt;If supplied all item fields except Item Quantity will be populated from the stored item record. | [optional] 
**quantity** | **int** | Item Quantity&lt;br /&gt;The quantity of items of this type. | 
**description** | **str** | Item Description&lt;br /&gt;Required if an Item Id is not supplied. | [optional] 
**value** | **float** | Item Value&lt;br /&gt;Individual item value (use same currency as shipment currency).&lt;br /&gt;Required if an Item Id is not supplied. | [optional] 
**weight** | **float** | Item Weight&lt;br /&gt;Individual item weight. | [optional] 
**package_occurrence** | **int** | Package Occurrence&lt;br /&gt;Optional Package Occurrence used to indicate which package the item has been packed into. | [optional] 
**hs_code** | **str** | HS Code&lt;br /&gt;The [standardised commodity code](https://www.gov.uk/trade-tariff). It must be 6-12 digits only.&lt;br /&gt;Used by Customs to calculate potential duties / taxes. | [optional] 
**sku_code** | **str** | SKU Code.&lt;br /&gt;Used by Customs to calculate potential duties / taxes. | [optional] 
**country_of_origin** | **str** | Country of Origin&lt;br /&gt;[ISO Alpha-2 Country Code](https://www.nationsonline.org/oneworld/country_code_list.htm) of item country of origin, per ISO 3166 Standard | [optional] 
**image_url** | **str** | Image URL&lt;br /&gt;Used to save a link to an image of the item with the shipment details, so that this can be used in the Returns&lt;br /&gt;system for consumers to see an image of the item when selecting items for return.&lt;br /&gt;URL must be a publicly accessible image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

