# rmail_apiv3.TokenApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_post**](TokenApi.md#authenticate_post) | **POST** /token | Authenticates a User and provides token.

# **authenticate_post**
> authenticate_post(x_rmg_security_username, x_rmg_security_password)

Authenticates a User and provides token.

Provides security token.

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
# Configure API key authorization: clientSecret
configuration = rmail_apiv3.Configuration()
configuration.api_key['X-IBM-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-IBM-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = rmail_apiv3.TokenApi(rmail_apiv3.ApiClient(configuration))
x_rmg_security_username = 'x_rmg_security_username_example' # str | User Name
x_rmg_security_password = 'x_rmg_security_password_example' # str | Password in plain text

try:
    # Authenticates a User and provides token.
    api_instance.authenticate_post(x_rmg_security_username, x_rmg_security_password)
except ApiException as e:
    print("Exception when calling TokenApi->authenticate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_security_username** | **str**| User Name | 
 **x_rmg_security_password** | **str**| Password in plain text | 

### Return type

void (empty response body)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

