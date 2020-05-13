# rmail_apiv3.ShipmentsApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipments_cancel**](ShipmentsApi.md#shipments_cancel) | **PUT** /shipments/cancel | Cancel Shipments
[**shipments_create**](ShipmentsApi.md#shipments_create) | **POST** /shipments | Create Shipment
[**shipments_defer**](ShipmentsApi.md#shipments_defer) | **PUT** /shipments/defer | Defer Shipments
[**shipments_hold**](ShipmentsApi.md#shipments_hold) | **PUT** /shipments/hold | Hold Shipments
[**shipments_print_document**](ShipmentsApi.md#shipments_print_document) | **PUT** /shipments/{shipmentId}/printDocument | Print Document
[**shipments_print_label**](ShipmentsApi.md#shipments_print_label) | **PUT** /shipments/{shipmentId}/printLabel | Print Label
[**shipments_release**](ShipmentsApi.md#shipments_release) | **PUT** /shipments/release | Release Shipments
[**shipments_service_availability**](ShipmentsApi.md#shipments_service_availability) | **POST** /shipments/serviceAvailability | Service Availability

# **shipments_cancel**
> ShipmentsCancelResponse shipments_cancel(body, x_rmg_auth_token)

Cancel Shipments

Can be used to cancel/void one or more current shipping labels.<br />This service can only be used before the shipment has been confirmed either by calling the manifest create request or by closing out via the User Interface.<br />There can be a maximum of 99 cancellation requests per call.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = [rmail_apiv3.ShipmentCancelRequest()] # list[ShipmentCancelRequest] | Shipment Cancel Requests
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Cancel Shipments
    api_response = api_instance.shipments_cancel(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ShipmentCancelRequest]**](ShipmentCancelRequest.md)| Shipment Cancel Requests | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ShipmentsCancelResponse**](ShipmentsCancelResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_create**
> ShipmentCreateResponse shipments_create(body, x_rmg_auth_token)

Create Shipment

Use to generate the final delivery label for your packages.<br />            <br />The request is split into several sections:<br />            <br />**Shipper** - who and where the parcel is coming from - optional if the posting location is to be used.<br />**Destination** - who and where the parcel is going to.<br />**Shipment Information** - overall package details, individual item details and requested service information.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.CreateShipmentShipment() # CreateShipmentShipment | The shipment.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create Shipment
    api_response = api_instance.shipments_create(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateShipmentShipment**](CreateShipmentShipment.md)| The shipment. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ShipmentCreateResponse**](ShipmentCreateResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_defer**
> ShipmentsDeferResponse shipments_defer(body, x_rmg_auth_token)

Defer Shipments

Used to update the shipment shipping date for a current shipment.<br />A shipment can be deferred by a maximum of 28 days from the date of the request.<br />This service can only be used before the shipment has been confirmed either by calling the manifest create request or by closing out via the User Interface.<br />There can be a maximum of 99 defer requests per call.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = [rmail_apiv3.ShipmentDeferRequest()] # list[ShipmentDeferRequest] | The shipments to defer.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Defer Shipments
    api_response = api_instance.shipments_defer(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_defer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ShipmentDeferRequest]**](ShipmentDeferRequest.md)| The shipments to defer. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ShipmentsDeferResponse**](ShipmentsDeferResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_hold**
> ShipmentsHoldResponse shipments_hold(body, x_rmg_auth_token)

Hold Shipments

Used to put a shipment on hold indefinitely.<br />A shipment on hold will not be included in any closeouts, but instead will remain in its current state.<br />Calling printLabel will release the shipment from being held.<br />This service can only be used before the shipment has been confirmed either by calling the manifest create request or by closing out via the User Interface.<br />            <br />A hold reason must be provided and must match those set in Pro Shipping under your maintenance screens.<br />If no hold reasons exist, then shipments cannot be put on hold.<br />            <br />There can be a maximum of 99 hold requests per call.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = [rmail_apiv3.ShipmentHoldRequest()] # list[ShipmentHoldRequest] | The shipments to hold.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Hold Shipments
    api_response = api_instance.shipments_hold(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_hold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ShipmentHoldRequest]**](ShipmentHoldRequest.md)| The shipments to hold. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ShipmentsHoldResponse**](ShipmentsHoldResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_print_document**
> PrintDocumentResponse shipments_print_document(body, x_rmg_auth_token, shipment_id)

Print Document

Prints the requested document for the shipment.<br />If item information, description of goods or reason for export have not been provided then the document cannot be printed.<br />            <br />This service can only be used before the shipment has been confirmed either by calling the manifest create request or by closing out via the User Interface.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.PrintDocumentRequest() # PrintDocumentRequest | Print Document Request
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
shipment_id = 'shipment_id_example' # str | Shipment Id<br />The tracking number or Unique Id of the shipment to print.

try:
    # Print Document
    api_response = api_instance.shipments_print_document(body, x_rmg_auth_token, shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_print_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrintDocumentRequest**](PrintDocumentRequest.md)| Print Document Request | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **shipment_id** | **str**| Shipment Id&lt;br /&gt;The tracking number or Unique Id of the shipment to print. | 

### Return type

[**PrintDocumentResponse**](PrintDocumentResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_print_label**
> PrintLabelResponse shipments_print_label(body, x_rmg_auth_token, shipment_id)

Print Label

Prints the label for the shipment.<br />Moves the shipment to processed, ready to manifest, if the shipment was not already in a processed state.<br />This service can only be used before the shipment has been confirmed either by calling the manifest create request or by closing out via the User Interface.<br />**On Hold Shipment**<br />Calling print label on a held shipment will release the shipment from hold and update the shipment date to today.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.PrintLabelRequest() # PrintLabelRequest | Print Label Request
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
shipment_id = 'shipment_id_example' # str | Shipment Id<br />The tracking number or Unique Id of the shipment to print.

try:
    # Print Label
    api_response = api_instance.shipments_print_label(body, x_rmg_auth_token, shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_print_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrintLabelRequest**](PrintLabelRequest.md)| Print Label Request | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **shipment_id** | **str**| Shipment Id&lt;br /&gt;The tracking number or Unique Id of the shipment to print. | 

### Return type

[**PrintLabelResponse**](PrintLabelResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_release**
> ShipmentsReleaseResponse shipments_release(body, x_rmg_auth_token)

Release Shipments

Used to release a shipment from being on hold.<br />This service can only be used for shipments on hold.<br />            <br />Releasing a shipment from hold will update the shipment date to today's date and if the shipment is processed it will be included the next requested manifest.<br />            <br />There can be a maximum of 99 release requests per call.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.ShipmentsReleaseRequest() # ShipmentsReleaseRequest | Shipments Release Request
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Release Shipments
    api_response = api_instance.shipments_release(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentsReleaseRequest**](ShipmentsReleaseRequest.md)| Shipments Release Request | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ShipmentsReleaseResponse**](ShipmentsReleaseResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipments_service_availability**
> ServiceAvailabilityResponse shipments_service_availability(body, x_rmg_auth_token)

Service Availability

Retrieve a list of available services for a potential shipment.<br />            <br />**Destination** - where the parcel is going to.<br />**Shipment Information** - overall package details and requested service requirements.

### Example
```python
from __future__ import print_function
import time
import rmail_apiv3
from rmail_apiv3.rest import ApiException
from pprint import pprint

# Configure API key authorization: clientID
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Id'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.ShipmentsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.ServiceAvailabilityShipment() # ServiceAvailabilityShipment | The shipment.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Service Availability
    api_response = api_instance.shipments_service_availability(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->shipments_service_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAvailabilityShipment**](ServiceAvailabilityShipment.md)| The shipment. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ServiceAvailabilityResponse**](ServiceAvailabilityResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

