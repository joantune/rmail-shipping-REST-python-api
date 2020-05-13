# rmail_apiv3.ItemsApi

All URIs are relative to */shipping/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_create**](ItemsApi.md#items_create) | **POST** /items | Create Item
[**items_delete**](ItemsApi.md#items_delete) | **DELETE** /items/{itemId} | Delete Item
[**items_get**](ItemsApi.md#items_get) | **GET** /items/{itemId} | Get Item
[**items_get_all**](ItemsApi.md#items_get_all) | **GET** /items | Get Items
[**items_update**](ItemsApi.md#items_update) | **PUT** /items/{itemId} | Update item

# **items_create**
> ItemResponse items_create(body, x_rmg_auth_token)

Create Item

Add a new item to your stored items that you can then use in your shipment requests.

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
api_instance = rmail_apiv3.ItemsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Item() # Item | The item.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Create Item
    api_response = api_instance.items_create(body, x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Item**](Item.md)| The item. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_delete**
> ItemResponse items_delete(x_rmg_auth_token, item_id)

Delete Item

Deletes the specified item.

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
api_instance = rmail_apiv3.ItemsApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
item_id = 'item_id_example' # str | Your unique Item ID of the item to delete.

try:
    # Delete Item
    api_response = api_instance.items_delete(x_rmg_auth_token, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **item_id** | **str**| Your unique Item ID of the item to delete. | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_get**
> Item items_get(x_rmg_auth_token, item_id)

Get Item

Get the item specified by your unique Item ID.

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
api_instance = rmail_apiv3.ItemsApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
item_id = 'item_id_example' # str | Your unique Item ID.

try:
    # Get Item
    api_response = api_instance.items_get(x_rmg_auth_token, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **item_id** | **str**| Your unique Item ID. | 

### Return type

[**Item**](Item.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_get_all**
> list[Item] items_get_all(x_rmg_auth_token)

Get Items

Get all of your stored items

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
api_instance = rmail_apiv3.ItemsApi(rmail_apiv3.ApiClient(configuration))
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.

try:
    # Get Items
    api_response = api_instance.items_get_all(x_rmg_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 

### Return type

[**list[Item]**](Item.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_update**
> ItemResponse items_update(body, x_rmg_auth_token, item_id)

Update item

Update an item that is already stored with new details. The whole item will be replaced with new details.

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
api_instance = rmail_apiv3.ItemsApi(rmail_apiv3.ApiClient(configuration))
body = rmail_apiv3.Item() # Item | The item with the updated details.
x_rmg_auth_token = 'x_rmg_auth_token_example' # str | Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation.
item_id = 'item_id_example' # str | Your unique Item ID of the item to update.

try:
    # Update item
    api_response = api_instance.items_update(body, x_rmg_auth_token, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Item**](Item.md)| The item with the updated details. | 
 **x_rmg_auth_token** | **str**| Authorisation token required to invoke this operation. Can be retrieved by invoking the **/token** operation. | 
 **item_id** | **str**| Your unique Item ID of the item to update. | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[clientID](../README.md#clientID)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

