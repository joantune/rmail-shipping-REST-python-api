# coding: utf-8

"""
    PRO SHIPPING API

    # Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> -->   # noqa: E501

    OpenAPI spec version: v4.0-RM
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rmail_apiv4
from rmail_apiv4.api.shipments_api import ShipmentsApi  # noqa: E501
from rmail_apiv4.rest import ApiException


class TestShipmentsApi(unittest.TestCase):
    """ShipmentsApi unit test stubs"""

    def setUp(self):
        self.api = ShipmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v4_shipments_defer_put(self):
        """Test case for v4_shipments_defer_put

        Defer Shipments  # noqa: E501
        """
        pass

    def test_v4_shipments_preallocate_tracking_number_rm_post(self):
        """Test case for v4_shipments_preallocate_tracking_number_rm_post

        Pre Allocate Tracking Number  # noqa: E501
        """
        pass

    def test_v4_shipments_print_document_carrier_code_shipment_id_post(self):
        """Test case for v4_shipments_print_document_carrier_code_shipment_id_post

        Print Document  # noqa: E501
        """
        pass

    def test_v4_shipments_print_label_rm_shipment_id_get(self):
        """Test case for v4_shipments_print_label_rm_shipment_id_get

        Print Label  # noqa: E501
        """
        pass

    def test_v4_shipments_print_my_label_qr_code_rm_shipment_id_get(self):
        """Test case for v4_shipments_print_my_label_qr_code_rm_shipment_id_get

        Print My Label QR Code  # noqa: E501
        """
        pass

    def test_v4_shipments_rm_post(self):
        """Test case for v4_shipments_rm_post

        Create Shipment  # noqa: E501
        """
        pass

    def test_v4_shipments_shipping_location_id_get(self):
        """Test case for v4_shipments_shipping_location_id_get

        Get Shipments  # noqa: E501
        """
        pass

    def test_v4_shipments_status_put(self):
        """Test case for v4_shipments_status_put

        Update Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
