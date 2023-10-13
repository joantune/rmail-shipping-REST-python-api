# RoyalMailPackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_occurrence** | **int** | Used to match a returned Package ID to this package. &lt;br /&gt;Can also be used to assign items to this package. &lt;br /&gt;If provided, each package occurrence must be unique. &lt;br /&gt;Note: For dutiable multi-package shipments that are not using a consignment service, items must be assigned to a package so that accurate customs information is given. &lt;br /&gt;Therefore, if the shipment contains more than one package, and it isn&#x27;t using a consignment service, then Package Occurrence is required. | [optional] 
**package_type** | [**RoyalMailPackageTypeCode**](RoyalMailPackageTypeCode.md) |  | [optional] 
**declared_weight** | **float** | The total weight of this package in the unit of measure specified by WeightUnitOfMeasure (defaults to KG). &lt;br /&gt;The minimum weight allowed is 1 gram. &lt;br /&gt;The maximum weight is dependent on the carrier / service / destination. &lt;br /&gt;Mandatory for shipments using non-consignment services. | [optional] 
**declared_value** | **float** | The declared value of the total package in the currency specified. &lt;br /&gt;If provided, the value must be equal or greater than the sum of all item values assigned to this package. &lt;br /&gt;If not provided it defaults to the sum of all item values. &lt;br /&gt;Used for shipment using non-consignment services, but not mandatory. | [optional] 
**dimensions** | [**Dimensions**](Dimensions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

