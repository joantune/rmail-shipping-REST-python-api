# rmail_api.ManifestApi

All URIs are relative to *///shipping/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manifest_post**](ManifestApi.md#manifest_post) | **POST** /manifest | Create shipping manifest.
[**manifest_put**](ManifestApi.md#manifest_put) | **PUT** /manifest | Create manifest image.

# **manifest_post**
> ManifestResponse manifest_post(body, x_rmg_auth_token)

Create shipping manifest.

This method creates a shipping manifest

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
api_instance = rmail_api.ManifestApi(rmail_api.ApiClient(configuration))
body = rmail_api.ManifestRequest() # ManifestRequest | 
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create shipping manifest.
    api_response = api_instance.manifest_post(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestApi->manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManifestRequest**](ManifestRequest.md)|  | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ManifestResponse**](ManifestResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manifest_put**
> PrintManifestResponse manifest_put(x_rmg_auth_token, sales_order_number=sales_order_number, manifest_batch_number=manifest_batch_number)

Create manifest image.

This method return a manifest image for a previously manifested shipment.

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
api_instance = rmail_api.ManifestApi(rmail_api.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
sales_order_number = 'sales_order_number_example' # str | The Sales Order Number, which is available via the GUI the day after the manifest was created. (optional)
manifest_batch_number = 'manifest_batch_number_example' # str | This is the batch number to print and is returned by a prior call to create manifest operation. (optional)

try:
    # Create manifest image.
    api_response = api_instance.manifest_put(x_rmg_auth_token, sales_order_number=sales_order_number, manifest_batch_number=manifest_batch_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestApi->manifest_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **sales_order_number** | **str**| The Sales Order Number, which is available via the GUI the day after the manifest was created. | [optional] 
 **manifest_batch_number** | **str**| This is the batch number to print and is returned by a prior call to create manifest operation. | [optional] 

### Return type

[**PrintManifestResponse**](PrintManifestResponse.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

