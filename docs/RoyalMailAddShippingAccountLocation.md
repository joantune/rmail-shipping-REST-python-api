# RoyalMailAddShippingAccountLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_location_id** | **str** | Shipping Location Identifier &lt;br /&gt;PRO SHIPPING Shipping Location Id(assigned by PRO SHIPPING) or Alias(assigned by you). &lt;br /&gt; &lt;br /&gt;Link an existing location to this account. &lt;br /&gt;Either a Shipping Location Id must be provided, or the details of a new shipping location provided. | [optional] 
**shipping_location** | [**AddShippingAccountLocationNewLocation**](AddShippingAccountLocationNewLocation.md) |  | [optional] 
**posting_location_code** | **str** | Posting Location Code &lt;br /&gt;The number assigned to this Location by Royal Mail. | 
**oba_access_code** | **str** | OBA Access Code &lt;br /&gt;A password for the account to access the OBA services. &lt;br /&gt;A Royal Mail shipping account cannot be active unless the OBA Access code has been provided. | [optional] 
**receiving_hub_code** | **str** | Receiving Hub Code &lt;br /&gt;Receiving Hub/Regional Distribution Center used for this Shipping Location. &lt;br /&gt;Must be an existing receiving hub code. &lt;br /&gt;Please refer to Royal Mail ReceivingHubs for a list of possible receiving hubs. &lt;br /&gt;If the receiving hub is not provided, we will match it to the one that corresponds to the postcode of the location&#x27;s address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

