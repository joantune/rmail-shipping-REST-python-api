# rmail_apiv4.ShipmentsApi

All URIs are relative to *https://api.proshipping.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_shipments_defer_put**](ShipmentsApi.md#v4_shipments_defer_put) | **PUT** /v4/shipments/defer | Defer Shipments
[**v4_shipments_preallocate_tracking_number_rm_post**](ShipmentsApi.md#v4_shipments_preallocate_tracking_number_rm_post) | **POST** /v4/shipments/preallocateTrackingNumber/rm | Pre Allocate Tracking Number
[**v4_shipments_print_document_carrier_code_shipment_id_post**](ShipmentsApi.md#v4_shipments_print_document_carrier_code_shipment_id_post) | **POST** /v4/shipments/printDocument/{carrierCode}/{shipmentId} | Print Document
[**v4_shipments_print_label_rm_shipment_id_get**](ShipmentsApi.md#v4_shipments_print_label_rm_shipment_id_get) | **GET** /v4/shipments/printLabel/rm/{shipmentId} | Print Label
[**v4_shipments_print_my_label_qr_code_rm_shipment_id_get**](ShipmentsApi.md#v4_shipments_print_my_label_qr_code_rm_shipment_id_get) | **GET** /v4/shipments/printMyLabelQRCode/rm/{shipmentId} | Print My Label QR Code
[**v4_shipments_rm_post**](ShipmentsApi.md#v4_shipments_rm_post) | **POST** /v4/shipments/rm | Create Shipment
[**v4_shipments_shipping_location_id_get**](ShipmentsApi.md#v4_shipments_shipping_location_id_get) | **GET** /v4/shipments/{shippingLocationId} | Get Shipments
[**v4_shipments_status_put**](ShipmentsApi.md#v4_shipments_status_put) | **PUT** /v4/shipments/status | Update Status

# **v4_shipments_defer_put**
> v4_shipments_defer_put(body=body)

Defer Shipments

Used to update the shipment shipping data for a current shipment. <br />A shipment can be deferred by a maximum of 28 days from the date of the request. <br />This service can only be used before the shipment has been manifested. <br />There can be a maximum of 99 defer requests per call.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
body = [rmail_apiv4.DeferShipmentRequest()] # list[DeferShipmentRequest] | Defer shipment requests (optional)

try:
    # Defer Shipments
    api_instance.v4_shipments_defer_put(body=body)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_defer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DeferShipmentRequest]**](DeferShipmentRequest.md)| Defer shipment requests | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_preallocate_tracking_number_rm_post**
> PreAllocateTrackingNumberResponse v4_shipments_preallocate_tracking_number_rm_post(body=body)

Pre Allocate Tracking Number

This service can be used to receive a Royal Mail Tracking Number that will be pre-allocated to the service and destination supplied in the request. No shipment or label will be produced from this service. <br />This service can only be used for services that are assigned a tracking number. <br />This service must be used in conjunction with CreateShipment service populating the TrackingNumber in the CarrierSpecifics /PreAllocatedBarcode section with the pre-allocated TrackingNumber returned in this service response.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.PreAllocateTrackingNumberRequest() # PreAllocateTrackingNumberRequest | The request. (optional)

try:
    # Pre Allocate Tracking Number
    api_response = api_instance.v4_shipments_preallocate_tracking_number_rm_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_preallocate_tracking_number_rm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreAllocateTrackingNumberRequest**](PreAllocateTrackingNumberRequest.md)| The request. | [optional] 

### Return type

[**PreAllocateTrackingNumberResponse**](PreAllocateTrackingNumberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_print_document_carrier_code_shipment_id_post**
> PrintDocumentResponse v4_shipments_print_document_carrier_code_shipment_id_post(carrier_code, shipment_id, body=body)

Print Document

Request the associated Customs Documents for the printed label.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
carrier_code = 'carrier_code_example' # str | Carrier Code
shipment_id = 'shipment_id_example' # str | Shipment Id <br />The Shipment Id may be an id or a tracking/barcode number.
body = rmail_apiv4.PrintDocumentRequest() # PrintDocumentRequest | Print Document Request (optional)

try:
    # Print Document
    api_response = api_instance.v4_shipments_print_document_carrier_code_shipment_id_post(carrier_code, shipment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_print_document_carrier_code_shipment_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_code** | **str**| Carrier Code | 
 **shipment_id** | **str**| Shipment Id &lt;br /&gt;The Shipment Id may be an id or a tracking/barcode number. | 
 **body** | [**PrintDocumentRequest**](PrintDocumentRequest.md)| Print Document Request | [optional] 

### Return type

[**PrintDocumentResponse**](PrintDocumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_print_label_rm_shipment_id_get**
> RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse v4_shipments_print_label_rm_shipment_id_get(shipment_id, label_format=label_format)

Print Label

This changes the status of the shipment to label printed. This should be done at the time of actual printing or label creation dependent on how you operate in reality. Shipments must be updated to printed status prior to manifesting.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
shipment_id = 'shipment_id_example' # str | Shipment Id <br />The Shipment Id may be an id or a tracking/barcode number.
label_format = rmail_apiv4.RoyalMailLabelFormat() # RoyalMailLabelFormat | Label Format <br />             <br />**PDF** Base 64 encoded PDF <br />**PNG** Base 64 encoded PNG <br />**DATASTREAM** - Label components broken down into a data-stream, for you to draw your own label <br />**ZPL203DPI** Base 64 encoded text for Zebra printer at 203 DPI <br />**ZPL300DPI** Base 64 encoded text for Zebra printer at 300 DPI <br />             <br />*DATASTREAM is only available if it has been activated on your account.* <br />             <br />Defaults To PDF (optional)

try:
    # Print Label
    api_response = api_instance.v4_shipments_print_label_rm_shipment_id_get(shipment_id, label_format=label_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_print_label_rm_shipment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| Shipment Id &lt;br /&gt;The Shipment Id may be an id or a tracking/barcode number. | 
 **label_format** | [**RoyalMailLabelFormat**](.md)| Label Format &lt;br /&gt;             &lt;br /&gt;**PDF** Base 64 encoded PDF &lt;br /&gt;**PNG** Base 64 encoded PNG &lt;br /&gt;**DATASTREAM** - Label components broken down into a data-stream, for you to draw your own label &lt;br /&gt;**ZPL203DPI** Base 64 encoded text for Zebra printer at 203 DPI &lt;br /&gt;**ZPL300DPI** Base 64 encoded text for Zebra printer at 300 DPI &lt;br /&gt;             &lt;br /&gt;*DATASTREAM is only available if it has been activated on your account.* &lt;br /&gt;             &lt;br /&gt;Defaults To PDF | [optional] 

### Return type

[**RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse**](RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_print_my_label_qr_code_rm_shipment_id_get**
> QRCodeResponse v4_shipments_print_my_label_qr_code_rm_shipment_id_get(shipment_id)

Print My Label QR Code

Request associated QR Code for the associated label in the print label call. <br />This is only available for Royal Mail Tracked Return Services.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
shipment_id = 'shipment_id_example' # str | Shipment Id <br />The Shipment Id may be an id or a tracking/barcode number.

try:
    # Print My Label QR Code
    api_response = api_instance.v4_shipments_print_my_label_qr_code_rm_shipment_id_get(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_print_my_label_qr_code_rm_shipment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| Shipment Id &lt;br /&gt;The Shipment Id may be an id or a tracking/barcode number. | 

### Return type

[**QRCodeResponse**](QRCodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_rm_post**
> RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse v4_shipments_rm_post(body=body)

Create Shipment

Create a Royal Mail shipment. This will return an image of the shipping label in PDF, PNG or ZPL format.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest() # RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest | Shipment Details (optional)

try:
    # Create Shipment
    api_response = api_instance.v4_shipments_rm_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_rm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest**](RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest.md)| Shipment Details | [optional] 

### Return type

[**RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse**](RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_shipping_location_id_get**
> ShipmentsPagedResponse v4_shipments_shipping_location_id_get(shipping_location_id, shipping_account_id=shipping_account_id, carrier_code=carrier_code, status=status, destination_country_code=destination_country_code, date_from=date_from, date_to=date_to, page_size=page_size, page_number=page_number)

Get Shipments

Provides a list of shipments for the specified shipping location in a given time period.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
shipping_location_id = 'shipping_location_id_example' # str | Shipping Location Id <br />PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you). <br />Filter by shipping location.
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Id <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). <br />Filter by shipping account. (optional)
carrier_code = 'carrier_code_example' # str | Carrier Code <br />If shippingAccountId and carrier are both provided, then the value sent in the carrier field will be ignored and the carrier associated with the shipping account will be used. (optional)
status = rmail_apiv4.GetShipmentsStatusType() # GetShipmentsStatusType | Status <br />Filter by shipment status. (optional)
destination_country_code = 'destination_country_code_example' # str | Country Code <br />ISO Alpha-2 Country Code per ISO 3166 Standard. (optional)
date_from = '2013-10-20' # date | Date From <br />Defaults to Today's date if not provided. <br />Format: YYYY-MM-DD (optional)
date_to = '2013-10-20' # date | Date To <br />Defaults to Today's date if not provided. <br />Format: YYYY-MM-DD (optional)
page_size = 100 # int | The maximum number of records per page. (optional) (default to 100)
page_number = 1 # int | The number of the requested page, starting at 1. (optional) (default to 1)

try:
    # Get Shipments
    api_response = api_instance.v4_shipments_shipping_location_id_get(shipping_location_id, shipping_account_id=shipping_account_id, carrier_code=carrier_code, status=status, destination_country_code=destination_country_code, date_from=date_from, date_to=date_to, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_shipping_location_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_location_id** | **str**| Shipping Location Id &lt;br /&gt;PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you). &lt;br /&gt;Filter by shipping location. | 
 **shipping_account_id** | **str**| Shipping Account Id &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). &lt;br /&gt;Filter by shipping account. | [optional] 
 **carrier_code** | **str**| Carrier Code &lt;br /&gt;If shippingAccountId and carrier are both provided, then the value sent in the carrier field will be ignored and the carrier associated with the shipping account will be used. | [optional] 
 **status** | [**GetShipmentsStatusType**](.md)| Status &lt;br /&gt;Filter by shipment status. | [optional] 
 **destination_country_code** | **str**| Country Code &lt;br /&gt;ISO Alpha-2 Country Code per ISO 3166 Standard. | [optional] 
 **date_from** | **date**| Date From &lt;br /&gt;Defaults to Today&#x27;s date if not provided. &lt;br /&gt;Format: YYYY-MM-DD | [optional] 
 **date_to** | **date**| Date To &lt;br /&gt;Defaults to Today&#x27;s date if not provided. &lt;br /&gt;Format: YYYY-MM-DD | [optional] 
 **page_size** | **int**| The maximum number of records per page. | [optional] [default to 100]
 **page_number** | **int**| The number of the requested page, starting at 1. | [optional] [default to 1]

### Return type

[**ShipmentsPagedResponse**](ShipmentsPagedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipments_status_put**
> v4_shipments_status_put(body=body)

Update Status

**Hold** - Put the shipments on hold for up to 28 days. Shipments on hold for longer than 28 days will be cancelled. A shipment on hold will not be included in an closeouts/manifests, but instead will remain in its current state. You can only put shipments on hold that are in the 'LabelPrinted' status as only shipments with this status are included in manifests. <br />             <br />**Cancel** - Use to cancel/void one or more current shipments. This can only be used before a shipment has been confirmed by being manifested. <br />             <br />**Release** - Use to release shipments from hold and shipments cancelled for less than 24 hours. Once released, the shipment will be included in the next manifest. <br />             <br />**Picked** - Set the shipment to picked. This means this shipment will only be manifested if you choose to manifest 'Picked' shipments.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv4
from rmail_apiv4.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = rmail_apiv4.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rmail_apiv4.ShipmentsApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.UpdateStatusRequest() # UpdateStatusRequest | Update Status Request (optional)

try:
    # Update Status
    api_instance.v4_shipments_status_put(body=body)
except ApiException as e:
    print("Exception when calling ShipmentsApi->v4_shipments_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStatusRequest**](UpdateStatusRequest.md)| Update Status Request | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

