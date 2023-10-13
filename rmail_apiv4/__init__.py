# coding: utf-8

# flake8: noqa

"""
    PRO SHIPPING API

    # Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> -->   # noqa: E501

    OpenAPI spec version: v4.0-RM
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from rmail_apiv4.api.offline_barcoding_api import OfflineBarcodingApi
from rmail_apiv4.api.shipments_api import ShipmentsApi
from rmail_apiv4.api.shipping_accounts_api import ShippingAccountsApi
# import ApiClient
from rmail_apiv4.api_client import ApiClient
from rmail_apiv4.configuration import Configuration
# import models into sdk package
from rmail_apiv4.models.account_type import AccountType
from rmail_apiv4.models.add_shipping_account_location_new_location import AddShippingAccountLocationNewLocation
from rmail_apiv4.models.add_shipping_account_response import AddShippingAccountResponse
from rmail_apiv4.models.business_transaction_type import BusinessTransactionType
from rmail_apiv4.models.content_type import ContentType
from rmail_apiv4.models.create_shipment_action import CreateShipmentAction
from rmail_apiv4.models.customs import Customs
from rmail_apiv4.models.defer_shipment_request import DeferShipmentRequest
from rmail_apiv4.models.destination import Destination
from rmail_apiv4.models.destination_details import DestinationDetails
from rmail_apiv4.models.dimensions import Dimensions
from rmail_apiv4.models.dimensions_unit_of_measure import DimensionsUnitOfMeasure
from rmail_apiv4.models.document_format import DocumentFormat
from rmail_apiv4.models.document_type import DocumentType
from rmail_apiv4.models.error_detail import ErrorDetail
from rmail_apiv4.models.error_response import ErrorResponse
from rmail_apiv4.models.get_shipments_status_type import GetShipmentsStatusType
from rmail_apiv4.models.item import Item
from rmail_apiv4.models.order_direction import OrderDirection
from rmail_apiv4.models.pre_allocate_tracking_number_request import PreAllocateTrackingNumberRequest
from rmail_apiv4.models.pre_allocate_tracking_number_response import PreAllocateTrackingNumberResponse
from rmail_apiv4.models.print_document_request import PrintDocumentRequest
from rmail_apiv4.models.print_document_response import PrintDocumentResponse
from rmail_apiv4.models.qr_code_response import QRCodeResponse
from rmail_apiv4.models.return_to_sender import ReturnToSender
from rmail_apiv4.models.royal_mail_account_location_status import RoyalMailAccountLocationStatus
from rmail_apiv4.models.royal_mail_add_shipping_account_location import RoyalMailAddShippingAccountLocation
from rmail_apiv4.models.royal_mail_add_shipping_account_request import RoyalMailAddShippingAccountRequest
from rmail_apiv4.models.royal_mail_data_stream_details import RoyalMailDataStreamDetails
from rmail_apiv4.models.royal_mail_enhancement_code import RoyalMailEnhancementCode
from rmail_apiv4.models.royal_mail_gazetteer_codes import RoyalMailGazetteerCodes
from rmail_apiv4.models.royal_mail_get_offline_barcoding_request import RoyalMailGetOfflineBarcodingRequest
from rmail_apiv4.models.royal_mail_get_offline_barcoding_response import RoyalMailGetOfflineBarcodingResponse
from rmail_apiv4.models.royal_mail_label_format import RoyalMailLabelFormat
from rmail_apiv4.models.royal_mail_label_format_royal_mail_shipment_response_carrier_specifics_package_response_create_shipment_response import RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse
from rmail_apiv4.models.royal_mail_label_format_royal_mail_shipment_response_carrier_specifics_print_label_response import RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPrintLabelResponse
from rmail_apiv4.models.royal_mail_label_format_shipment_information import RoyalMailLabelFormatShipmentInformation
from rmail_apiv4.models.royal_mail_link_shipping_account_location import RoyalMailLinkShippingAccountLocation
from rmail_apiv4.models.royal_mail_offline_barcode import RoyalMailOfflineBarcode
from rmail_apiv4.models.royal_mail_offline_barcoding_enhancement_code import RoyalMailOfflineBarcodingEnhancementCode
from rmail_apiv4.models.royal_mail_package import RoyalMailPackage
from rmail_apiv4.models.royal_mail_package_type_code import RoyalMailPackageTypeCode
from rmail_apiv4.models.royal_mail_pre_allocated_tracking_number_enhancement_code import RoyalMailPreAllocatedTrackingNumberEnhancementCode
from rmail_apiv4.models.royal_mail_service_enhancement import RoyalMailServiceEnhancement
from rmail_apiv4.models.royal_mail_shipment_request_carrier_specifics import RoyalMailShipmentRequestCarrierSpecifics
from rmail_apiv4.models.royal_mail_shipment_request_carrier_specifics_royal_mail_package_royal_mail_label_format_create_shipment_request import RoyalMailShipmentRequestCarrierSpecificsRoyalMailPackageRoyalMailLabelFormatCreateShipmentRequest
from rmail_apiv4.models.royal_mail_shipment_response_carrier_specifics import RoyalMailShipmentResponseCarrierSpecifics
from rmail_apiv4.models.royal_mail_shipment_response_carrier_specifics_package_response import RoyalMailShipmentResponseCarrierSpecificsPackageResponse
from rmail_apiv4.models.royal_mail_shipping_account import RoyalMailShippingAccount
from rmail_apiv4.models.royal_mail_shipping_account_shipping_accounts_paged_response import RoyalMailShippingAccountShippingAccountsPagedResponse
from rmail_apiv4.models.royal_mail_update_shipping_account_location import RoyalMailUpdateShippingAccountLocation
from rmail_apiv4.models.royal_mail_update_shipping_account_request import RoyalMailUpdateShippingAccountRequest
from rmail_apiv4.models.royal_mail_view_shipping_account_location import RoyalMailViewShippingAccountLocation
from rmail_apiv4.models.royal_mail_view_shipping_account_location_shipping_location_for_account import RoyalMailViewShippingAccountLocationShippingLocationForAccount
from rmail_apiv4.models.royal_mail_view_shipping_account_location_shipping_locations_for_account_paged_response import RoyalMailViewShippingAccountLocationShippingLocationsForAccountPagedResponse
from rmail_apiv4.models.shipment_address import ShipmentAddress
from rmail_apiv4.models.shipment_response import ShipmentResponse
from rmail_apiv4.models.shipments_paged_response import ShipmentsPagedResponse
from rmail_apiv4.models.shipper import Shipper
from rmail_apiv4.models.shipper_address import ShipperAddress
from rmail_apiv4.models.shipping_account import ShippingAccount
from rmail_apiv4.models.shipping_accounts_paged_response import ShippingAccountsPagedResponse
from rmail_apiv4.models.shipping_accounts_sort_by import ShippingAccountsSortBy
from rmail_apiv4.models.shipping_location_address import ShippingLocationAddress
from rmail_apiv4.models.shipping_location_id_request import ShippingLocationIdRequest
from rmail_apiv4.models.shipping_locations_sort_by import ShippingLocationsSortBy
from rmail_apiv4.models.terms_of_trade import TermsOfTrade
from rmail_apiv4.models.update_status_request import UpdateStatusRequest
from rmail_apiv4.models.update_status_type import UpdateStatusType
from rmail_apiv4.models.weight_unit_of_measure import WeightUnitOfMeasure
