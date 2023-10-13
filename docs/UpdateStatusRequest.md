# UpdateStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**UpdateStatusType**](UpdateStatusType.md) |  | 
**reason** | **str** | Reason &lt;br /&gt;The reason for this status update. &lt;br /&gt;             &lt;br /&gt;If the status you are updating to is &#x27;Hold&#x27; the reason is required and must be one of the following values: &lt;br /&gt;**Awaiting Dispatch** &lt;br /&gt;**Awaiting Payment** &lt;br /&gt;**Awaiting Stock** &lt;br /&gt;**Awaiting Customer Response** &lt;br /&gt;**Held for Shipping Day** &lt;br /&gt;**Weight Consolidation** &lt;br /&gt;**Warehouse Processing** &lt;br /&gt;             &lt;br /&gt;If the status you are updating to is &#x27;Cancel&#x27;, the reason is required and must be one of the following values: &lt;br /&gt;**Order Cancelled** &lt;br /&gt;**Packed in Error** &lt;br /&gt;**Repacked** | [optional] 
**shipment_ids** | **list[str]** | Shipment Ids &lt;br /&gt;The shipments to apply the change to. &lt;br /&gt;There must be at least 1 shipment and a maximum of 99. &lt;br /&gt;             &lt;br /&gt;The Shipment Id may be an id or a tracking/barcode number. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

