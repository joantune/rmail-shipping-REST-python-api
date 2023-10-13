# coding: utf-8

"""
    PRO SHIPPING API

    # Introduction Here you will find requirements for integrating with PRO SHIPPING API.  The documentation specifically covers how the API can be used by business customers to conduct shipping activity with available carriers and provides the technical information to build this integration. The API allows customers to create and manage shipments, produce labels, customs documentation, and collection manifests, retrieve reference data such as carriers and countries, and maintain their own data such as shipping account details.  Pro Shipping API is a fully RESTful service implemented using JSON messaging. You, as the customer are responsible for sending JSON messages and for maintaining the capability of receiving JSON messages in the format described in this specification. Request and response examples for each API service are included in this specification.  # Authentication  The PRO SHIPPING API uses OAuth2 authentication.  To request the authorization token you need to create API credentials (Client ID and Secret) on the system first. If you have not done it already, log into your account and go to API Credentials or follow the link [add a link here with the path to the API Credentials menu]. Use the credentials to retrieve the authorization token.  Note: Make sure you copy the Secret and keep it secure as you won't be able to view it again on the system.  <!-- ReDoc-Inject: <SecurityDefinitions /> -->   # noqa: E501

    OpenAPI spec version: v4.0-RM
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'consignment_shipment_id': 'str',
        'consignment_tracking_number': 'str',
        'consignment_carrier_tracking_url': 'str',
        'labels': 'str',
        'label_format': 'RoyalMailLabelFormat',
        'packages': 'list[RoyalMailShipmentResponseCarrierSpecificsPackageResponse]',
        'documents': 'str',
        'document_format': 'DocumentFormat'
    }

    attribute_map = {
        'consignment_shipment_id': 'ConsignmentShipmentId',
        'consignment_tracking_number': 'ConsignmentTrackingNumber',
        'consignment_carrier_tracking_url': 'ConsignmentCarrierTrackingUrl',
        'labels': 'Labels',
        'label_format': 'LabelFormat',
        'packages': 'Packages',
        'documents': 'Documents',
        'document_format': 'DocumentFormat'
    }

    def __init__(self, consignment_shipment_id=None, consignment_tracking_number=None, consignment_carrier_tracking_url=None, labels=None, label_format=None, packages=None, documents=None, document_format=None):  # noqa: E501
        """RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse - a model defined in Swagger"""  # noqa: E501
        self._consignment_shipment_id = None
        self._consignment_tracking_number = None
        self._consignment_carrier_tracking_url = None
        self._labels = None
        self._label_format = None
        self._packages = None
        self._documents = None
        self._document_format = None
        self.discriminator = None
        if consignment_shipment_id is not None:
            self.consignment_shipment_id = consignment_shipment_id
        if consignment_tracking_number is not None:
            self.consignment_tracking_number = consignment_tracking_number
        if consignment_carrier_tracking_url is not None:
            self.consignment_carrier_tracking_url = consignment_carrier_tracking_url
        if labels is not None:
            self.labels = labels
        if label_format is not None:
            self.label_format = label_format
        if packages is not None:
            self.packages = packages
        if documents is not None:
            self.documents = documents
        if document_format is not None:
            self.document_format = document_format

    @property
    def consignment_shipment_id(self):
        """Gets the consignment_shipment_id of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Consignment Shipment Id <br />Only populated if the service is a consignment service.  # noqa: E501

        :return: The consignment_shipment_id of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_shipment_id

    @consignment_shipment_id.setter
    def consignment_shipment_id(self, consignment_shipment_id):
        """Sets the consignment_shipment_id of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Consignment Shipment Id <br />Only populated if the service is a consignment service.  # noqa: E501

        :param consignment_shipment_id: The consignment_shipment_id of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._consignment_shipment_id = consignment_shipment_id

    @property
    def consignment_tracking_number(self):
        """Gets the consignment_tracking_number of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Consignment Tracking Number <br />Only populated if the service is a consignment service  # noqa: E501

        :return: The consignment_tracking_number of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_tracking_number

    @consignment_tracking_number.setter
    def consignment_tracking_number(self, consignment_tracking_number):
        """Sets the consignment_tracking_number of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Consignment Tracking Number <br />Only populated if the service is a consignment service  # noqa: E501

        :param consignment_tracking_number: The consignment_tracking_number of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._consignment_tracking_number = consignment_tracking_number

    @property
    def consignment_carrier_tracking_url(self):
        """Gets the consignment_carrier_tracking_url of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Consignment Carrier Tracking URL <br />Only populated if the service is a consignment service and is available  # noqa: E501

        :return: The consignment_carrier_tracking_url of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_carrier_tracking_url

    @consignment_carrier_tracking_url.setter
    def consignment_carrier_tracking_url(self, consignment_carrier_tracking_url):
        """Sets the consignment_carrier_tracking_url of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Consignment Carrier Tracking URL <br />Only populated if the service is a consignment service and is available  # noqa: E501

        :param consignment_carrier_tracking_url: The consignment_carrier_tracking_url of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._consignment_carrier_tracking_url = consignment_carrier_tracking_url

    @property
    def labels(self):
        """Gets the labels of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Labels <br />Populated if requested Action was 'Process'  # noqa: E501

        :return: The labels of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Labels <br />Populated if requested Action was 'Process'  # noqa: E501

        :param labels: The labels of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._labels = labels

    @property
    def label_format(self):
        """Gets the label_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501


        :return: The label_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: RoyalMailLabelFormat
        """
        return self._label_format

    @label_format.setter
    def label_format(self, label_format):
        """Sets the label_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.


        :param label_format: The label_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: RoyalMailLabelFormat
        """

        self._label_format = label_format

    @property
    def packages(self):
        """Gets the packages of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Packages <br />The details of each package.  # noqa: E501

        :return: The packages of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: list[RoyalMailShipmentResponseCarrierSpecificsPackageResponse]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Packages <br />The details of each package.  # noqa: E501

        :param packages: The packages of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: list[RoyalMailShipmentResponseCarrierSpecificsPackageResponse]
        """

        self._packages = packages

    @property
    def documents(self):
        """Gets the documents of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501

        Customs Documents <br />Populated if requested Action was 'Process' and shipment is dutiable  # noqa: E501

        :return: The documents of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.

        Customs Documents <br />Populated if requested Action was 'Process' and shipment is dutiable  # noqa: E501

        :param documents: The documents of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._documents = documents

    @property
    def document_format(self):
        """Gets the document_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501


        :return: The document_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :rtype: DocumentFormat
        """
        return self._document_format

    @document_format.setter
    def document_format(self, document_format):
        """Sets the document_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.


        :param document_format: The document_format of this RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse.  # noqa: E501
        :type: DocumentFormat
        """

        self._document_format = document_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoyalMailLabelFormatRoyalMailShipmentResponseCarrierSpecificsPackageResponseCreateShipmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
