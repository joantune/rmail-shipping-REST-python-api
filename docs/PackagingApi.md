# rmail_apiv3.PackagingApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packaging_create**](PackagingApi.md#packaging_create) | **POST** /packaging | Create Packaging
[**packaging_delete**](PackagingApi.md#packaging_delete) | **DELETE** /packaging/{packagingId} | Delete Packaging
[**packaging_get**](PackagingApi.md#packaging_get) | **GET** /packaging/{packagingId} | Get Packaging
[**packaging_get_all**](PackagingApi.md#packaging_get_all) | **GET** /packaging | Get All Packaging
[**packaging_update**](PackagingApi.md#packaging_update) | **PUT** /packaging/{packagingId} | Update packaging

# **packaging_create**
> PackagingResponse packaging_create(body, x_rmg_auth_token)

Create Packaging

Add new packaging to your stored packaging details that you can then use in your shipment requests.

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
api_instance = rmail_apiv3.PackagingApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Packaging() # Packaging | The packaging details.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create Packaging
    api_response = api_instance.packaging_create(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagingApi->packaging_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Packaging**](Packaging.md)| The packaging details. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**PackagingResponse**](PackagingResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packaging_delete**
> PackagingResponse packaging_delete(x_rmg_auth_token, packaging_id)

Delete Packaging

Deletes the specified packaging.

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
api_instance = rmail_apiv3.PackagingApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
packaging_id = 'packaging_id_example' # str | Your unique Packaging ID of the packaging details to delete.

try:
    # Delete Packaging
    api_response = api_instance.packaging_delete(x_rmg_auth_token, packaging_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagingApi->packaging_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **packaging_id** | **str**| Your unique Packaging ID of the packaging details to delete. | 

### Return type

[**PackagingResponse**](PackagingResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packaging_get**
> Packaging packaging_get(x_rmg_auth_token, packaging_id)

Get Packaging

Get the packaging details specified by your unique Packaging ID.

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
api_instance = rmail_apiv3.PackagingApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
packaging_id = 'packaging_id_example' # str | Your Unique Packaging ID.

try:
    # Get Packaging
    api_response = api_instance.packaging_get(x_rmg_auth_token, packaging_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagingApi->packaging_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **packaging_id** | **str**| Your Unique Packaging ID. | 

### Return type

[**Packaging**](Packaging.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packaging_get_all**
> list[Packaging] packaging_get_all(x_rmg_auth_token)

Get All Packaging

Get all of your stored packaging details

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
api_instance = rmail_apiv3.PackagingApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Get All Packaging
    api_response = api_instance.packaging_get_all(x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagingApi->packaging_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**list[Packaging]**](Packaging.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packaging_update**
> PackagingResponse packaging_update(body, x_rmg_auth_token, packaging_id)

Update packaging

Update packaging details that is already stored with new details. All details will be replaced with new details.

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
api_instance = rmail_apiv3.PackagingApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Packaging() # Packaging | The packaging with the updated details.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
packaging_id = 'packaging_id_example' # str | Your unique Packaging ID of the packaging details to update.

try:
    # Update packaging
    api_response = api_instance.packaging_update(body, x_rmg_auth_token, packaging_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagingApi->packaging_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Packaging**](Packaging.md)| The packaging with the updated details. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **packaging_id** | **str**| Your unique Packaging ID of the packaging details to update. | 

### Return type

[**PackagingResponse**](PackagingResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

