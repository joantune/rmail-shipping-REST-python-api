# Parcel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | [**Measurement**](Measurement.md) |  | [optional] 
**length** | [**Measurement**](Measurement.md) |  | [optional] 
**height** | [**Measurement**](Measurement.md) |  | [optional] 
**width** | [**Measurement**](Measurement.md) |  | [optional] 
**purpose_of_shipment** | **str** | Purpose of shipment (also known as Nature of Goods). These are 2-3 character codes as defined below&amp;#58;   \&quot;21\&quot; for Returned Goods  “31” for Gift “32” for Commercial Sample \&quot;91\&quot; for Documents  “991” for Mixed Content \&quot;999\&quot; for Other | [optional] 
**explanation** | **str** | Comments regarding the parcel | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**export_license_number** | **str** | Export licence number | [optional] 
**certificate_number** | **str** | Certificate number | [optional] 
**content_details** | [**list[ContentDetail]**](ContentDetail.md) | Content details list. | 
**fees** | [**BigDecimal**](BigDecimal.md) | Parcel fees | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

