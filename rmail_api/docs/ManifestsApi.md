# rmail_apiv3.ManifestsApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manifests_create**](ManifestsApi.md#manifests_create) | **POST** /manifests | Manifest All Shipments
[**manifests_create_by_carrier**](ManifestsApi.md#manifests_create_by_carrier) | **POST** /manifests/bycarrier | Manifest by Carrier Code(s)
[**manifests_create_by_service**](ManifestsApi.md#manifests_create_by_service) | **POST** /manifests/byservice | Manifest by Service Code(s)

# **manifests_create**
> ManifestResponse manifests_create(body, x_rmg_auth_token)

Manifest All Shipments

Manifest all shipments that are ready to manifest for a single Posting Location.<br />             <br />Required to confirm parcels are ready to despatch.<br />Generates the required paperwork to despatch your parcels. <br />One or more manifests, including the base 64 encoded PDF and manifest number will be returned.<br />            <br />*Note: All average weight shipments are ignored and need to be closed out via Shipment Processing*

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
api_instance = rmail_apiv3.ManifestsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.ManifestRequest() # ManifestRequest | Request
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Manifest All Shipments
    api_response = api_instance.manifests_create(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->manifests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManifestRequest**](ManifestRequest.md)| Request | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ManifestResponse**](ManifestResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manifests_create_by_carrier**
> ManifestResponse manifests_create_by_carrier(body, x_rmg_auth_token)

Manifest by Carrier Code(s)

Manifest shipments created with the given carrier codes that are ready to manifest for a single Posting Location.<br />            <br />Required to confirm parcels are ready to despatch.<br />Generates the required paperwork to despatch your parcels. <br />One or more manifests, including the base 64 encoded PDF and manifest number will be returned.<br />            <br />*Note: All average weight shipments are ignored and need to be closed out via Shipment Processing*

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
api_instance = rmail_apiv3.ManifestsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.ManifestCarrierCodesRequest() # ManifestCarrierCodesRequest | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Manifest by Carrier Code(s)
    api_response = api_instance.manifests_create_by_carrier(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->manifests_create_by_carrier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManifestCarrierCodesRequest**](ManifestCarrierCodesRequest.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ManifestResponse**](ManifestResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manifests_create_by_service**
> ManifestResponse manifests_create_by_service(body, x_rmg_auth_token)

Manifest by Service Code(s)

Manifest shipments created with the given service codes that are ready to manifest for a single Posting Location.<br />            <br />Required to confirm parcels are ready to despatch.<br />Generates the required paperwork to despatch your parcels. <br />One or more manifests, including the base 64 encoded PDF and manifest number will be returned.<br />            <br />*Note: All average weight shipments are ignored and need to be closed out via Shipment Processing*

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
api_instance = rmail_apiv3.ManifestsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.ManifestServiceCodesRequest() # ManifestServiceCodesRequest | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Manifest by Service Code(s)
    api_response = api_instance.manifests_create_by_service(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->manifests_create_by_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManifestServiceCodesRequest**](ManifestServiceCodesRequest.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ManifestResponse**](ManifestResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

