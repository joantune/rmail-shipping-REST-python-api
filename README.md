# rmail-apiv4
# Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> --> 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v4.0-RM
- Package version: 0.0.4
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rmail_apiv4 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rmail_apiv4
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = rmail_apiv4.OfflineBarcodingApi(rmail_apiv4.ApiClient(configuration))
body = rmail_apiv4.RoyalMailGetOfflineBarcodingRequest() # RoyalMailGetOfflineBarcodingRequest | The request. (optional)

try:
    # Get Barcode Range
    api_response = api_instance.v4_offline_barcode_number_range_rm_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfflineBarcodingApi->v4_offline_barcode_number_range_rm_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.proshipping.net/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OfflineBarcodingApi* | [**v4_offline_barcode_number_range_rm_post**](docs/OfflineBarcodingApi.md#v4_offline_barcode_number_range_rm_post) | **POST** /v4/offlineBarcodeNumberRange/rm | Get Barcode Range
*ShipmentsApi* | [**v4_shipments_defer_put**](docs/ShipmentsApi.md#v4_shipments_defer_put) | **PUT** /v4/shipments/defer | Defer Shipments
*ShipmentsApi* | [**v4_shipments_preallocate_tracking_number_rm_post**](docs/ShipmentsApi.md#v4_shipments_preallocate_tracking_number_rm_post) | **POST** /v4/shipments/preallocateTrackingNumber/rm | Pre Allocate Tracking Number
*ShipmentsApi* | [**v4_shipments_print_document_carrier_code_shipment_id_post**](docs/ShipmentsApi.md#v4_shipments_print_document_carrier_code_shipment_id_post) | **POST** /v4/shipments/printDocument/{carrierCode}/{shipmentId} | Print Document
*ShipmentsApi* | [**v4_shipments_print_label_rm_shipment_id_get**](docs/ShipmentsApi.md#v4_shipments_print_label_rm_shipment_id_get) | **GET** /v4/shipments/printLabel/rm/{shipmentId} | Print Label
*ShipmentsApi* | [**v4_shipments_print_my_label_qr_code_rm_shipment_id_get**](docs/ShipmentsApi.md#v4_shipments_print_my_label_qr_code_rm_shipment_id_get) | **GET** /v4/shipments/printMyLabelQRCode/rm/{shipmentId} | Print My Label QR Code
*ShipmentsApi* | [**v4_shipments_rm_post**](docs/ShipmentsApi.md#v4_shipments_rm_post) | **POST** /v4/shipments/rm | Create Shipment
*ShipmentsApi* | [**v4_shipments_shipping_location_id_get**](docs/ShipmentsApi.md#v4_shipments_shipping_location_id_get) | **GET** /v4/shipments/{shippingLocationId} | Get Shipments
*ShipmentsApi* | [**v4_shipments_status_put**](docs/ShipmentsApi.md#v4_shipments_status_put) | **PUT** /v4/shipments/status | Update Status
*ShippingAccountsApi* | [**v4_shipping_accounts_carrier_code_shipping_account_id_delete**](docs/ShippingAccountsApi.md#v4_shipping_accounts_carrier_code_shipping_account_id_delete) | **DELETE** /v4/shippingAccounts/{carrierCode}/{shippingAccountId} | Delete Account
*ShippingAccountsApi* | [**v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put**](docs/ShippingAccountsApi.md#v4_shipping_accounts_carrier_code_shipping_account_id_unlink_locations_put) | **PUT** /v4/shippingAccounts/{carrierCode}/{shippingAccountId}/unlinkLocations | Unlink Locations
*ShippingAccountsApi* | [**v4_shipping_accounts_get**](docs/ShippingAccountsApi.md#v4_shipping_accounts_get) | **GET** /v4/shippingAccounts | Get Accounts
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_get**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_get) | **GET** /v4/shippingAccounts/rm | Get Carrier Accounts
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_post**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_post) | **POST** /v4/shippingAccounts/rm | Add Account
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_get**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId} | Get Account
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_link_locations_post**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_link_locations_post) | **POST** /v4/shippingAccounts/rm/{shippingAccountId}/linkLocations | Link Locations
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_put**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_put) | **PUT** /v4/shippingAccounts/rm/{shippingAccountId} | Update Account
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations | Get Associated Locations
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_get) | **GET** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations/{shippingLocationId} | Get Associated Location
*ShippingAccountsApi* | [**v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put**](docs/ShippingAccountsApi.md#v4_shipping_accounts_rm_shipping_account_id_shipping_locations_shipping_location_id_put) | **PUT** /v4/shippingAccounts/rm/{shippingAccountId}/shippingLocations/{shippingLocationId} | Update Associated Location

## Documentation For Models

 - [AccountType](docs/AccountType.md)
 - [AddShippingAccountLocationNewLocation](docs/AddShippingAccountLocationNewLocation.md)
 - [AddShippingAccountResponse](docs/AddShippingAccountResponse.md)
 - [BusinessTransactionType](docs/BusinessTransactionType.md)
 - [ContentType](docs/ContentType.md)
 - [CreateShipmentAction](docs/CreateShipmentAction.md)
 - [Customs](docs/Customs.md)
 - [DeferShipmentRequest](docs/DeferShipmentRequest.md)
 - [Destination](docs/Destination.md)
 - [DestinationDetails](docs/DestinationDetails.md)
 - [Dimensions](docs/Dimensions.md)
 - [DimensionsUnitOfMeasure](docs/DimensionsUnitOfMeasure.md)
 - [DocumentFormat](docs/DocumentFormat.md)
 - [DocumentType](docs/DocumentType.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetShipmentsStatusType](docs/GetShipmentsStatusType.md)
 - [Item](docs/Item.md)
 - [OrderDirection](docs/OrderDirection.md)
 - [PreAllocateTrackingNumberRequest](docs/PreAllocateTrackingNumberRequest.md)
 - [PreAllocateTrackingNumberResponse](docs/PreAllocateTrackingNumberResponse.md)
 - [PrintDocumentRequest](docs/PrintDocumentRequest.md)
 - [PrintDocumentResponse](docs/PrintDocumentResponse.md)
 - [QRCodeResponse](docs/QRCodeResponse.md)
 - [ReturnToSender](docs/ReturnToSender.md)
 - [RoyalMailAccountLocationStatus](docs/RoyalMailAccountLocationStatus.md)
 - [RoyalMailAddShippingAccountLocation](docs/RoyalMailAddShippingAccountLocation.md)
 - [RoyalMailAddShippingAccountRequest](docs/RoyalMailAddShippingAccountRequest.md)
 - [RoyalMailDataStreamDetails](docs/RoyalMailDataStreamDetails.md)
 - [RoyalMailEnhancementCode](docs/RoyalMailEnhancementCode.md)
 - [RoyalMailGazetteerCodes](docs/RoyalMailGazetteerCodes.md)
 - [RoyalMailGetOfflineBarcodingRequest](docs/RoyalMailGetOfflineBarcodingRequest.md)
 - [RoyalMailGetOfflineBarcodingResponse](docs/RoyalMailGetOfflineBarcodingResponse.md)
 - [RoyalMailLabelFormat](docs/RoyalMailLabelFormat.md)
 - [RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse](docs/RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.md)
 - [RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse](docs/RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse.md)
 - [RoyalMailLabelFormatShipmentInformation](docs/RoyalMailLabelFormatShipmentInformation.md)
 - [RoyalMailLinkShippingAccountLocation](docs/RoyalMailLinkShippingAccountLocation.md)
 - [RoyalMailOfflineBarcode](docs/RoyalMailOfflineBarcode.md)
 - [RoyalMailOfflineBarcodingEnhancementCode](docs/RoyalMailOfflineBarcodingEnhancementCode.md)
 - [RoyalMailPackage](docs/RoyalMailPackage.md)
 - [RoyalMailPackageTypeCode](docs/RoyalMailPackageTypeCode.md)
 - [RoyalMailPreAllocatedTrackingNumberEnhancementCode](docs/RoyalMailPreAllocatedTrackingNumberEnhancementCode.md)
 - [RoyalMailServiceEnhancement](docs/RoyalMailServiceEnhancement.md)
 - [RoyalMailShipmentRequestCarrierSpecifics](docs/RoyalMailShipmentRequestCarrierSpecifics.md)
 - [RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest](docs/RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest.md)
 - [RoyalMailShipmentResponseCarrierSpecifics](docs/RoyalMailShipmentResponseCarrierSpecifics.md)
 - [RoyalMailShipmentResponseCarrierSpecificsPackageResponse](docs/RoyalMailShipmentResponseCarrierSpecificsPackageResponse.md)
 - [RoyalMailShippingAccount](docs/RoyalMailShippingAccount.md)
 - [RoyalMailShippingAccountShippingAccountsPagedResponse](docs/RoyalMailShippingAccountShippingAccountsPagedResponse.md)
 - [RoyalMailUpdateShippingAccountLocation](docs/RoyalMailUpdateShippingAccountLocation.md)
 - [RoyalMailUpdateShippingAccountRequest](docs/RoyalMailUpdateShippingAccountRequest.md)
 - [RoyalMailViewShippingAccountLocation](docs/RoyalMailViewShippingAccountLocation.md)
 - [RoyalMailViewShippingAccountLocationShippingLocationForAccount](docs/RoyalMailViewShippingAccountLocationShippingLocationForAccount.md)
 - [RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse](docs/RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse.md)
 - [ShipmentAddress](docs/ShipmentAddress.md)
 - [ShipmentResponse](docs/ShipmentResponse.md)
 - [ShipmentsPagedResponse](docs/ShipmentsPagedResponse.md)
 - [Shipper](docs/Shipper.md)
 - [ShipperAddress](docs/ShipperAddress.md)
 - [ShippingAccount](docs/ShippingAccount.md)
 - [ShippingAccountsPagedResponse](docs/ShippingAccountsPagedResponse.md)
 - [ShippingAccountsSortBy](docs/ShippingAccountsSortBy.md)
 - [ShippingLocationAddress](docs/ShippingLocationAddress.md)
 - [ShippingLocationIdRequest](docs/ShippingLocationIdRequest.md)
 - [ShippingLocationsSortBy](docs/ShippingLocationsSortBy.md)
 - [TermsOfTrade](docs/TermsOfTrade.md)
 - [UpdateStatusRequest](docs/UpdateStatusRequest.md)
 - [UpdateStatusType](docs/UpdateStatusType.md)
 - [WeightUnitOfMeasure](docs/WeightUnitOfMeasure.md)

## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 


## Author


