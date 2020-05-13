# rmail_apiv3.AddressesApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addresses_create**](AddressesApi.md#addresses_create) | **POST** /addresses | Create Address
[**addresses_delete**](AddressesApi.md#addresses_delete) | **DELETE** /addresses/{addressId} | Delete Address
[**addresses_get**](AddressesApi.md#addresses_get) | **GET** /addresses/{addressId} | Get Address
[**addresses_get_all**](AddressesApi.md#addresses_get_all) | **GET** /addresses | Get Addresses
[**addresses_update**](AddressesApi.md#addresses_update) | **PUT** /addresses/{addressId} | Update address

# **addresses_create**
> AddressResponse addresses_create(body, x_rmg_auth_token)

Create Address

Add a new address to your address book that you can then use in your shipment requests.

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
api_instance = rmail_apiv3.AddressesApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Address() # Address | The address.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create Address
    api_response = api_instance.addresses_create(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| The address. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_delete**
> AddressResponse addresses_delete(x_rmg_auth_token, address_id)

Delete Address

Deletes the specified address.

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
api_instance = rmail_apiv3.AddressesApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
address_id = 'address_id_example' # str | Your unique Address ID of the address to delete.

try:
    # Delete Address
    api_response = api_instance.addresses_delete(x_rmg_auth_token, address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **address_id** | **str**| Your unique Address ID of the address to delete. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_get**
> Address addresses_get(x_rmg_auth_token, address_id)

Get Address

Get the address specified by your unique Address ID.

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
api_instance = rmail_apiv3.AddressesApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
address_id = 'address_id_example' # str | Your unique Address ID.

try:
    # Get Address
    api_response = api_instance.addresses_get(x_rmg_auth_token, address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **address_id** | **str**| Your unique Address ID. | 

### Return type

[**Address**](Address.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_get_all**
> list[Address] addresses_get_all(x_rmg_auth_token)

Get Addresses

Get all of your stored addresses

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
api_instance = rmail_apiv3.AddressesApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Get Addresses
    api_response = api_instance.addresses_get_all(x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**list[Address]**](Address.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_update**
> AddressResponse addresses_update(body, x_rmg_auth_token, address_id)

Update address

Update an address that is already in your address book with new details. The whole address will be replaced with<br />new details.

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
api_instance = rmail_apiv3.AddressesApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Address() # Address | The address with the updated details.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
address_id = 'address_id_example' # str | Your unique Address ID of the address to update.

try:
    # Update address
    api_response = api_instance.addresses_update(body, x_rmg_auth_token, address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| The address with the updated details. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **address_id** | **str**| Your unique Address ID of the address to update. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

