# ShippingLocationAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | First Line Address &lt;br /&gt;Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 40 characters | 
**line2** | **str** | Second Line Address, if applicable &lt;br /&gt;Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 40 characters | [optional] 
**line3** | **str** | Third Line Address, if applicable &lt;br /&gt;Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 40 characters | [optional] 
**town** | **str** | Town &lt;br /&gt;Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 40 characters | 
**postcode** | **str** | Postcode / Zip &lt;br /&gt;Required for United Kingdom addresses and some international addresses. &lt;br /&gt;The Countries API can be used to check whether postcode/zip code is required for a country. &lt;br /&gt;Up to 20 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 10 characters | [optional] 
**county** | **str** | County / State / Province &lt;br /&gt;May be required depending on the country. &lt;br /&gt;USA, Australia and Canada all require a valid state code or name. &lt;br /&gt;The Countries API can be used to check whether county/state is required for a country. &lt;br /&gt;Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.&lt;br&gt;Royal Mail: 40 characters | [optional] 
**country_code** | **str** | Country Code &lt;br /&gt;2 Digit ISO Country Code, per ISO 3166 Standard. | 
**what3_words** | **str** | The what3words identifier for this address. | [optional] 
**contact_phone** | **str** | Contact Phone Number &lt;br /&gt;If provided, and the shipper address is not provided for a create shipment request, this will be used as the shipper&#x27;s contact phone number for this location, instead of the shipping account&#x27;s contact phone number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

