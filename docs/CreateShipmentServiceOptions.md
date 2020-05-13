# CreateShipmentServiceOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posting_location** | **str** | Posting Location.&lt;br /&gt;Optional if you only have 1 Posting Location. | 
**service_level** | **str** | Service Level&lt;br /&gt;Valid values are 01-99.&lt;br /&gt;Defaults to lowest service level if not provided. | [optional] 
**service_format** | **str** | Service Format&lt;br /&gt;            &lt;br /&gt;**L** - Letter&lt;br /&gt;**F** - Large Letter&lt;br /&gt;**P** - Parcel&lt;br /&gt;**S** - Printed Papers - International Services Only | [optional] 
**safeplace** | **str** | Safe Place Enhancement&lt;br /&gt;Free text to describe a safe place to leave the parcel.&lt;br /&gt;Returns an error if the service does not allow Safeplace. | [optional] 
**saturday_guaranteed** | **bool** | Saturday Guaranteed Enhancement&lt;br /&gt;Available for Domestic Special Delivery Services Only&lt;br /&gt;Returns an error if requested and the service does not allow it. | [optional] 
**consequential_loss** | **str** | Consequential Loss Enhancement&lt;br /&gt;Available for Domestic Special Delivery Services Only.&lt;br /&gt;            &lt;br /&gt;**Level1** - £1,000&lt;br /&gt;**Level2** - £2,500&lt;br /&gt;**Level3** - £5,000&lt;br /&gt;**Level4** - £7,500&lt;br /&gt;**Level5** - £10,000&lt;br /&gt;            &lt;br /&gt;Returns an error if requested and the service does not allow it. | [optional] 
**local_collect** | **bool** | Local Collect Enhancement&lt;br /&gt;Available for Domestic Special Delivery and Domestic Tracked services only.&lt;br /&gt;Returns an error if requested and the service does not allow it. | [optional] 
**tracking_notifications** | **str** | Tracking Notifications Enhancement&lt;br /&gt;Available for Domestic Special Delivery and Domestic Tracked services only.&lt;br /&gt;Returns an error if requested and the service does not allow it. | [optional] 
**recorded_signed_for** | **bool** | Recorded Signed For&lt;br /&gt;Available for all Domestic Services that are not Special Delivery, Tracked or BFPO.&lt;br /&gt;This is an enhancement for services that don&#x27;t have an in-built signature service like Special Delivery and Tracked.&lt;br /&gt;Returns an error if requested and the service does not allow it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

