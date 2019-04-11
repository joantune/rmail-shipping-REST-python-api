# rmail_api.TokenApi

All URIs are relative to *///shipping/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](TokenApi.md#get_token) | **GET** /token | Method to get a JSON Web Token (JWT).

# **get_token**
> Token get_token(x_rmg_user_name, x_rmg_password)

Method to get a JSON Web Token (JWT).

This method accepts a Royal Mail issued user name and (encoded SHA-1 hash) password. On successful validation of the user's credentials, a JWT valid for 4 hours is returned. The user must send this JWT in the *X-RMG-Auth-Token* header when making subsequent calls to this API's business operations. > **Use the Password Generator utility attachment on the Developer Portal API Shipping V2 (REST) page to hash and encode the plain text password.** 

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
api_instance = rmail_api.TokenApi(rmail_api.ApiClient(configuration))
x_rmg_user_name = 'x_rmg_user_name_example' # str | User Name
x_rmg_password = 'x_rmg_password_example' # str | Encoded SHA-1 hashed password.

try:
    # Method to get a JSON Web Token (JWT).
    api_response = api_instance.get_token(x_rmg_user_name, x_rmg_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_user_name** | **str**| User Name | 
 **x_rmg_password** | **str**| Encoded SHA-1 hashed password. | 

### Return type

[**Token**](Token.md)

### Authorization

[clientID](../README.md#clientID), [clientSecret](../README.md#clientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

