# rmail_api.ShipmentApi

All URIs are relative to *///shipping/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domestic_post**](ShipmentApi.md#domestic_post) | **POST** /domestic | Create a domestic shipment.
[**shipment_number_delete**](ShipmentApi.md#shipment_number_delete) | **DELETE** /{shipmentNumber} | Cancel a shipment.
[**shipment_number_label_put**](ShipmentApi.md#shipment_number_label_put) | **PUT** /{shipmentNumber}/label | Create shipment label.
[**shipment_number_put**](ShipmentApi.md#shipment_number_put) | **PUT** /{shipmentNumber} | Update a shipment.
[**shipments_post**](ShipmentApi.md#shipments_post) | **POST** /shipments | Create an international or domestic shipment.
[**shipments_shipment_number_documents_put**](ShipmentApi.md#shipments_shipment_number_documents_put) | **PUT** /shipments/{shipmentNumber}/documents | Create international documents.

# **domestic_post**
> CreatedShipmentResponse domestic_post(body, x_rmg_auth_token)

Create a domestic shipment.

This operation will take a domestic shipment request in the message body and return the newly created shipment numbers and item details. **Offline Shipment Not Currently Available.**

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
body = rmail_api.Shipment() # Shipment | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create a domestic shipment.
    api_response = api_instance.domestic_post(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->domestic_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Shipment**](Shipment.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**CreatedShipmentResponse**](CreatedShipmentResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_number_delete**
> CancelOrUpdateShipmentResponse shipment_number_delete(shipment_number, x_rmg_auth_token)

Cancel a shipment.

Cancel a shipment with the specified *shipmentNumber*.

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
shipment_number = 'shipment_number_example' # str | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Cancel a shipment.
    api_response = api_instance.shipment_number_delete(shipment_number, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_number_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_number** | **str**|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**CancelOrUpdateShipmentResponse**](CancelOrUpdateShipmentResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_number_label_put**
> LabelResponse shipment_number_label_put(shipment_number, x_rmg_auth_token, output_format)

Create shipment label.

This method returns a label for the shipment identifier passed in the url.

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
shipment_number = 'shipment_number_example' # str | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
output_format = 'output_format_example' # str | Label Format Type. The content of the response.  > Unspecified / PDF: returns the standard Base64 Encoded PDF Label   DS: returns a data stream  DSPDF: returns both the data stream and the Base64 Encoded PDF Label.  PNG: returns Base64 Encoded PNG images of the 2D Data Matric and 1D Linear Barcode.  DSPNG: returns both the data stream and the Base64 Encoded PNG images of the 2D Data Matric and 1D Linear Barcode.

try:
    # Create shipment label.
    api_response = api_instance.shipment_number_label_put(shipment_number, x_rmg_auth_token, output_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_number_label_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_number** | **str**|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **output_format** | **str**| Label Format Type. The content of the response.  &gt; Unspecified / PDF: returns the standard Base64 Encoded PDF Label   DS: returns a data stream  DSPDF: returns both the data stream and the Base64 Encoded PDF Label.  PNG: returns Base64 Encoded PNG images of the 2D Data Matric and 1D Linear Barcode.  DSPNG: returns both the data stream and the Base64 Encoded PNG images of the 2D Data Matric and 1D Linear Barcode. | 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_number_put**
> CancelOrUpdateShipmentResponse shipment_number_put(body, x_rmg_auth_token, shipment_number)

Update a shipment.

Update a shipment with the specified *shipmentNumber*. Fields to be updated populated in the body. Service related information cannot be updated, and if passed as part of request, will be ignored.  On successful update, the shipment number updated is returned. 

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
body = rmail_api.Shipment() # Shipment | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
shipment_number = 'shipment_number_example' # str | 

try:
    # Update a shipment.
    api_response = api_instance.shipment_number_put(body, x_rmg_auth_token, shipment_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipment_number_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Shipment**](Shipment.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **shipment_number** | **str**|  | 

### Return type

[**CancelOrUpdateShipmentResponse**](CancelOrUpdateShipmentResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_post**
> CreatedShipmentResponse shipments_post(body, x_rmg_auth_token)

Create an international or domestic shipment.

This operation will accept a shipment request(domestic or international) in the message body and return the newly created shipment numbers and item details.

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
body = rmail_api.ShipmentsRequest() # ShipmentsRequest | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create an international or domestic shipment.
    api_response = api_instance.shipments_post(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentsRequest**](ShipmentsRequest.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**CreatedShipmentResponse**](CreatedShipmentResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_shipment_number_documents_put**
> object shipments_shipment_number_documents_put(body, x_rmg_auth_token, shipment_number)

Create international documents.

Create base64 encoded PDF international documents for the given shipment number.

### Example
```python
from __future__ import print_function
import time
import rmail_api
from rmail_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'
# Configure API key authorization: clientSecret
configuration = rmail_api.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_api.ShipmentApi(rmail_api.ApiClient(configuration))
body = rmail_api.DocumentsRequest() # DocumentsRequest | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
shipment_number = 'shipment_number_example' # str | 

try:
    # Create international documents.
    api_response = api_instance.shipments_shipment_number_documents_put(body, x_rmg_auth_token, shipment_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->shipments_shipment_number_documents_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsRequest**](DocumentsRequest.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **shipment_number** | **str**|  | 

### Return type

**object**

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

