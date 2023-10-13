# rmail_apiv4.OfflineBarcodingApi

All URIs are relative to *https://api.proshipping.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_offline_barcode_number_range_rm_post**](OfflineBarcodingApi.md#v4_offline_barcode_number_range_rm_post) | **POST** /v4/offlineBarcodeNumberRange/rm | Get Barcode Range

# **v4_offline_barcode_number_range_rm_post**
> list[RoyalMailGetOfflineBarcodingResponse] v4_offline_barcode_number_range_rm_post(body=body)

Get Barcode Range

Get barcode ranges for offline barcoding. <br />Offline Barcoding is only available if it has been activated on your customer account in the GUI.

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
api_instance = rmail_apiv4.OfflineBarcodingApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.RoyalMailGetOfflineBarcodingRequest() # RoyalMailGetOfflineBarcodingRequest | The request. (optional)

try:
    # Get Barcode Range
    api_response = api_instance.v4_offline_barcode_number_range_rm_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfflineBarcodingApi->v4_offline_barcode_number_range_rm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoyalMailGetOfflineBarcodingRequest**](RoyalMailGetOfflineBarcodingRequest.md)| The request. | [optional] 

### Return type

[**list[RoyalMailGetOfflineBarcodingResponse]**](RoyalMailGetOfflineBarcodingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

