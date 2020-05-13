# coding: utf-8

# flake8: noqa
"""
    Royal Mail API Shipping V3 (REST)

    This API specification details the requirements for integrating with **Royal Mail API Shipping V3**.<br><br>It specifically covers how the Royal Mail API Shipping V3 can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.<br><br>Royal Mail API Shipping V3 exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail.<br><br>Built on industry standards, Royal Mail API Shipping V3 provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels. There are no costs to customers for using the Royal Mail API Shipping V3 services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.<br><br>This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating/ cancelling a shipment and Manifesting please refer to http://www.royalmail.com/pro-shipping-help.  # noqa: E501

    OpenAPI spec version: 3.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from rmail_apiv3.models.address import Address
from rmail_apiv3.models.address_response import AddressResponse
from rmail_apiv3.models.create_shipment_destination import CreateShipmentDestination
from rmail_apiv3.models.create_shipment_service_options import CreateShipmentServiceOptions
from rmail_apiv3.models.create_shipment_shipment import CreateShipmentShipment
from rmail_apiv3.models.create_shipment_shipment_information import CreateShipmentShipmentInformation
from rmail_apiv3.models.create_shipment_shipment_package import CreateShipmentShipmentPackage
from rmail_apiv3.models.error_detail import ErrorDetail
from rmail_apiv3.models.item import Item
from rmail_apiv3.models.item_response import ItemResponse
from rmail_apiv3.models.manifest import Manifest
from rmail_apiv3.models.manifest_carrier_codes_request import ManifestCarrierCodesRequest
from rmail_apiv3.models.manifest_request import ManifestRequest
from rmail_apiv3.models.manifest_response import ManifestResponse
from rmail_apiv3.models.manifest_service_codes_request import ManifestServiceCodesRequest
from rmail_apiv3.models.package_response import PackageResponse
from rmail_apiv3.models.packaging import Packaging
from rmail_apiv3.models.packaging_response import PackagingResponse
from rmail_apiv3.models.print_document_request import PrintDocumentRequest
from rmail_apiv3.models.print_document_response import PrintDocumentResponse
from rmail_apiv3.models.print_label_request import PrintLabelRequest
from rmail_apiv3.models.print_label_response import PrintLabelResponse
from rmail_apiv3.models.service_availability_destination import ServiceAvailabilityDestination
from rmail_apiv3.models.service_availability_format import ServiceAvailabilityFormat
from rmail_apiv3.models.service_availability_option import ServiceAvailabilityOption
from rmail_apiv3.models.service_availability_response import ServiceAvailabilityResponse
from rmail_apiv3.models.service_availability_service_options import ServiceAvailabilityServiceOptions
from rmail_apiv3.models.service_availability_shipment import ServiceAvailabilityShipment
from rmail_apiv3.models.service_availability_shipment_information import ServiceAvailabilityShipmentInformation
from rmail_apiv3.models.service_availability_shipment_package import ServiceAvailabilityShipmentPackage
from rmail_apiv3.models.shipment_cancel_request import ShipmentCancelRequest
from rmail_apiv3.models.shipment_create_response import ShipmentCreateResponse
from rmail_apiv3.models.shipment_defer_request import ShipmentDeferRequest
from rmail_apiv3.models.shipment_hold_request import ShipmentHoldRequest
from rmail_apiv3.models.shipment_item import ShipmentItem
from rmail_apiv3.models.shipments_cancel_response import ShipmentsCancelResponse
from rmail_apiv3.models.shipments_defer_response import ShipmentsDeferResponse
from rmail_apiv3.models.shipments_hold_response import ShipmentsHoldResponse
from rmail_apiv3.models.shipments_release_request import ShipmentsReleaseRequest
from rmail_apiv3.models.shipments_release_response import ShipmentsReleaseResponse
from rmail_apiv3.models.shipper import Shipper