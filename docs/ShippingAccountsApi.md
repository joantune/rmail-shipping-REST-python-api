# rmail_apiv4.ShippingAccountsApi

All URIs are relative to *https://api.proshipping.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_shipping_accounts_carrier_code_shipping_account_id_delete**](ShippingAccountsApi.md#v4_shipping_accounts_carrier_code_shipping_account_id_delete) | **DELETE** /v4/shippingAccounts/{carrierCode}/{shippingAccountId} | Delete Account
[**v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put**](ShippingAccountsApi.md#v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put) | **PUT** /v4/shippingAccounts/{carrierCode}/{shippingAccountId}/unlinkLocations | Unlink Locations
[**v4_shipping_accounts_get**](ShippingAccountsApi.md#v4_shipping_accounts_get) | **GET** /v4/shippingAccounts | Get Accounts
[**v4_shipping_accounts_rm_get**](ShippingAccountsApi.md#v4_shipping_accounts_rm_get) | **GET** /v4/shippingAccounts/rm | Get Carrier Accounts
[**v4_shipping_accounts_rm_post**](ShippingAccountsApi.md#v4_shipping_accounts_rm_post) | **POST** /v4/shippingAccounts/rm | Add Account
[**v4_shipping_accounts_rm_shipping_account_id_get**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId} | Get Account
[**v4_shipping_accounts_rm_shipping_account_id_link_locations_post**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_link_locations_post) | **POST** /v4/shippingAccounts/rm/{shippingAccountId}/linkLocations | Link Locations
[**v4_shipping_accounts_rm_shipping_account_id_put**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_put) | **PUT** /v4/shippingAccounts/rm/{shippingAccountId} | Update Account
[**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations | Get Associated Locations
[**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations/{shippingLocationId} | Get Associated Location
[**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put**](ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put) | **PUT** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations/{shippingLocationId} | Update Associated Location

# **v4_shipping_accounts_carrier_code_shipping_account_id_delete**
> v4_shipping_accounts_carrier_code_shipping_account_id_delete(carrier_code, shipping_account_id)

Delete Account

Delete a specific shipping account.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
carrier_code = 'carrier_code_example' # str | Carrier Code
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).

try:
    # Delete Account
    api_instance.v4_shipping_accounts_carrier_code_shipping_account_id_delete(carrier_code, shipping_account_id)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_carrier_code_shipping_account_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_code** | **str**| Carrier Code | 
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put**
> v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put(carrier_code, shipping_account_id, body=body)

Unlink Locations

Unlink one or more shipping location from a specific carrier shipping account.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
carrier_code = 'carrier_code_example' # str | Carrier Code
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
body = [rmail_apiv4.ShippingLocationIdRequest()] # list[ShippingLocationIdRequest] | Shipping Locations
The locations to remove from the account.
At least one location must be provided. (optional)

try:
    # Unlink Locations
    api_instance.v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put(carrier_code, shipping_account_id, body=body)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_code** | **str**| Carrier Code | 
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **body** | [**list[ShippingLocationIdRequest]**](ShippingLocationIdRequest.md)| Shipping Locations
The locations to remove from the account.
At least one location must be provided. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_get**
> ShippingAccountsPagedResponse v4_shipping_accounts_get(search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)

Get Accounts

Provides a list of all shipping accounts for all carriers (created on your customer account). <br />Information about the associated carrier, account number, account type, and contact details is included in the response.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
search_term = 'search_term_example' # str | Search Term (optional)
page_size = 100 # int | The maximum number of records per page. (optional) (default to 100)
page_number = 1 # int | The number of the requested page, starting at 1. (optional) (default to 1)
sort_by = rmail_apiv4.ShippingAccountsSortBy() # ShippingAccountsSortBy | Sort By <br />Default: Name (optional)
sort_dir = rmail_apiv4.OrderDirection() # OrderDirection | Sort Direction <br />Default: Ascending (optional)

try:
    # Get Accounts
    api_response = api_instance.v4_shipping_accounts_get(search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Search Term | [optional] 
 **page_size** | **int**| The maximum number of records per page. | [optional] [default to 100]
 **page_number** | **int**| The number of the requested page, starting at 1. | [optional] [default to 1]
 **sort_by** | [**ShippingAccountsSortBy**](.md)| Sort By &lt;br /&gt;Default: Name | [optional] 
 **sort_dir** | [**OrderDirection**](.md)| Sort Direction &lt;br /&gt;Default: Ascending | [optional] 

### Return type

[**ShippingAccountsPagedResponse**](ShippingAccountsPagedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_get**
> RoyalMailShippingAccountShippingAccountsPagedResponse v4_shipping_accounts_rm_get(search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)

Get Carrier Accounts

Provides a list of Royal Mail shipping accounts only. <br />Information about the account number, account type, and contact details is included in the response.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
search_term = 'search_term_example' # str | Search Term (optional)
page_size = 100 # int | The maximum number of records per page. (optional) (default to 100)
page_number = 1 # int | The number of the requested page, starting at 1. (optional) (default to 1)
sort_by = rmail_apiv4.ShippingAccountsSortBy() # ShippingAccountsSortBy | Sort By <br />Default: Name (optional)
sort_dir = rmail_apiv4.OrderDirection() # OrderDirection | Sort Direction <br />Default: Ascending (optional)

try:
    # Get Carrier Accounts
    api_response = api_instance.v4_shipping_accounts_rm_get(search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Search Term | [optional] 
 **page_size** | **int**| The maximum number of records per page. | [optional] [default to 100]
 **page_number** | **int**| The number of the requested page, starting at 1. | [optional] [default to 1]
 **sort_by** | [**ShippingAccountsSortBy**](.md)| Sort By &lt;br /&gt;Default: Name | [optional] 
 **sort_dir** | [**OrderDirection**](.md)| Sort Direction &lt;br /&gt;Default: Ascending | [optional] 

### Return type

[**RoyalMailShippingAccountShippingAccountsPagedResponse**](RoyalMailShippingAccountShippingAccountsPagedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_post**
> AddShippingAccountResponse v4_shipping_accounts_rm_post(body=body)

Add Account

Add a shipping account for Royal Mail and link it with an existing shipping location. <br />Ensure to have required carrier details ready like Royal Mail account number, Posting Location, OBA access codes and receiving hub, so that you can use the account for shipping with Royal Mail.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.RoyalMailAddShippingAccountRequest() # RoyalMailAddShippingAccountRequest | Add Shipping Account Request (optional)

try:
    # Add Account
    api_response = api_instance.v4_shipping_accounts_rm_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoyalMailAddShippingAccountRequest**](RoyalMailAddShippingAccountRequest.md)| Add Shipping Account Request | [optional] 

### Return type

[**AddShippingAccountResponse**](AddShippingAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_get**
> RoyalMailShippingAccount v4_shipping_accounts_rm_shipping_account_id_get(shipping_account_id)

Get Account

Provides details for a Royal Mail account. <br />Information about the account number, alias, account type, and contact details is included in the response.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).

try:
    # Get Account
    api_response = api_instance.v4_shipping_accounts_rm_shipping_account_id_get(shipping_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 

### Return type

[**RoyalMailShippingAccount**](RoyalMailShippingAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_link_locations_post**
> v4_shipping_accounts_rm_shipping_account_id_link_locations_post(shipping_account_id, body=body)

Link Locations

Link one or more shipping locations with a Royal Mail shipping account. <br />Ensure to have required carrier details ready: Royal Mail Posting Location number, OBA access codes and receiving hub, so that you can link it successfully.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
body = [rmail_apiv4.RoyalMailLinkShippingAccountLocation()] # list[RoyalMailLinkShippingAccountLocation] | Shipping Locations
The locations to associate with this shipping account. (optional)

try:
    # Link Locations
    api_instance.v4_shipping_accounts_rm_shipping_account_id_link_locations_post(shipping_account_id, body=body)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_link_locations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **body** | [**list[RoyalMailLinkShippingAccountLocation]**](RoyalMailLinkShippingAccountLocation.md)| Shipping Locations
The locations to associate with this shipping account. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_put**
> v4_shipping_accounts_rm_shipping_account_id_put(shipping_account_id, body=body)

Update Account

Update shipping account details. <br />Note: All required fields must be populated in the request, regardless if they need updating or not.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
body = rmail_apiv4.RoyalMailUpdateShippingAccountRequest() # RoyalMailUpdateShippingAccountRequest | Shipping Account Details (optional)

try:
    # Update Account
    api_instance.v4_shipping_accounts_rm_shipping_account_id_put(shipping_account_id, body=body)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **body** | [**RoyalMailUpdateShippingAccountRequest**](RoyalMailUpdateShippingAccountRequest.md)| Shipping Account Details | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get**
> RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get(shipping_account_id, search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)

Get Associated Locations

Provides a list of all shipping locations associated with a Royal Mail shipping account.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
search_term = 'search_term_example' # str | Search Term (optional)
page_size = 100 # int | The maximum number of records per page. (optional) (default to 100)
page_number = 1 # int | The number of the requested page, starting at 1. (optional) (default to 1)
sort_by = rmail_apiv4.ShippingLocationsSortBy() # ShippingLocationsSortBy | Sort By <br />Default: Name (optional)
sort_dir = rmail_apiv4.OrderDirection() # OrderDirection | Sort Direction <br />Default: Ascending (optional)

try:
    # Get Associated Locations
    api_response = api_instance.v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get(shipping_account_id, search_term=search_term, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **search_term** | **str**| Search Term | [optional] 
 **page_size** | **int**| The maximum number of records per page. | [optional] [default to 100]
 **page_number** | **int**| The number of the requested page, starting at 1. | [optional] [default to 1]
 **sort_by** | [**ShippingLocationsSortBy**](.md)| Sort By &lt;br /&gt;Default: Name | [optional] 
 **sort_dir** | [**OrderDirection**](.md)| Sort Direction &lt;br /&gt;Default: Ascending | [optional] 

### Return type

[**RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse**](RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get**
> RoyalMailViewShippingAccountLocationShippingLocationForAccount v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get(shipping_account_id, shipping_location_id)

Get Associated Location

Provides information for a specific shipping location linked to a Royal Mail shipping account including location alias, Royal Mail specific details, timezone, address, when it was last updated, and by who.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
shipping_location_id = 'shipping_location_id_example' # str | Shipping Location Identifier <br />PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you).

try:
    # Get Associated Location
    api_response = api_instance.v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get(shipping_account_id, shipping_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **shipping_location_id** | **str**| Shipping Location Identifier &lt;br /&gt;PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 

### Return type

[**RoyalMailViewShippingAccountLocationShippingLocationForAccount**](RoyalMailViewShippingAccountLocationShippingLocationForAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put**
> v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put(shipping_account_id, shipping_location_id, body=body)

Update Associated Location

Update a shipping location associated with a specific Royal Mail shipping account with carrier specific details like Posting Location, OBA access code and receiving hub. <br />Note: All required fields must be populated in the request, regardless if they need updating or not.

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
api_instance = rmail_apiv4.ShippingAccountsApi(rmail_apiv4.ApiClient(configuration))
shipping_account_id = 'shipping_account_id_example' # str | Shipping Account Identifier <br />PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you).
shipping_location_id = 'shipping_location_id_example' # str | Shipping Location Identifier <br />PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you).
body = rmail_apiv4.RoyalMailUpdateShippingAccountLocation() # RoyalMailUpdateShippingAccountLocation | Location Details (optional)

try:
    # Update Associated Location
    api_instance.v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put(shipping_account_id, shipping_location_id, body=body)
except ApiException as e:
    print("Exception when calling ShippingAccountsApi->v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_account_id** | **str**| Shipping Account Identifier &lt;br /&gt;PRO SHIPPING Shipping Account Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **shipping_location_id** | **str**| Shipping Location Identifier &lt;br /&gt;PRO SHIPPING Shipping Location Id (assigned by PRO SHIPPING) or Alias (assigned by you). | 
 **body** | [**RoyalMailUpdateShippingAccountLocation**](RoyalMailUpdateShippingAccountLocation.md)| Location Details | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

