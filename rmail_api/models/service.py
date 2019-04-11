# coding: utf-8

"""
    Royal Mail API Shipping V2 (REST)

    This API specification details the requirements for integrating with Royal Mail API Shipping V2 (REST). It specifically covers how the Royal Mail API Shipping V2 (REST) can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.  Royal Mail API Shipping V2 (REST) exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail. Built on industry standards, Royal Mail API Shipping V2 (REST) provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels.  There are no costs to customers for using the Royal Mail API Shipping V2 (REST) services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.  This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating cancelling a shipment and manifesting click here&#58; www.royalmail.com/pro-shipping-help  # noqa: E501

    OpenAPI spec version: 1.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from rmail_api.models.service_enhancements import ServiceEnhancements  # noqa: F401,E501


class Service(object):
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
        'format': 'str',
        'occurrence': 'str',
        'offering': 'str',
        'type': 'str',
        'signature': 'str',
        'enhancements': 'ServiceEnhancements'
    }

    attribute_map = {
        'format': 'format',
        'occurrence': 'occurrence',
        'offering': 'offering',
        'type': 'type',
        'signature': 'signature',
        'enhancements': 'enhancements'
    }

    def __init__(self, format=None, occurrence=None, offering=None, type=None, signature=None, enhancements=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._occurrence = None
        self._offering = None
        self._type = None
        self._signature = None
        self._enhancements = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if occurrence is not None:
            self.occurrence = occurrence
        self.offering = offering
        self.type = type
        if signature is not None:
            self.signature = signature
        if enhancements is not None:
            self.enhancements = enhancements

    @property
    def format(self):
        """Gets the format of this Service.  # noqa: E501

        The Service Format code for the shipment. Note that this field is case sensitive. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer) Portal and refer to Shipping API Reference Data.  # noqa: E501

        :return: The format of this Service.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Service.

        The Service Format code for the shipment. Note that this field is case sensitive. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer) Portal and refer to Shipping API Reference Data.  # noqa: E501

        :param format: The format of this Service.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def occurrence(self):
        """Gets the occurrence of this Service.  # noqa: E501

        Part of the customer’s contract identifier. In conjunction with the Service Offering it identifies an agreement line on the customer’s account. If only one Service Reference exists then this is not required. No leading zero is required.  # noqa: E501

        :return: The occurrence of this Service.  # noqa: E501
        :rtype: str
        """
        return self._occurrence

    @occurrence.setter
    def occurrence(self, occurrence):
        """Sets the occurrence of this Service.

        Part of the customer’s contract identifier. In conjunction with the Service Offering it identifies an agreement line on the customer’s account. If only one Service Reference exists then this is not required. No leading zero is required.  # noqa: E501

        :param occurrence: The occurrence of this Service.  # noqa: E501
        :type: str
        """

        self._occurrence = occurrence

    @property
    def offering(self):
        """Gets the offering of this Service.  # noqa: E501

        The Service Offering code for the mail item ordered. Please note that this field is case sensitive. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer) Portal and refer to Shipping API Reference Data  # noqa: E501

        :return: The offering of this Service.  # noqa: E501
        :rtype: str
        """
        return self._offering

    @offering.setter
    def offering(self, offering):
        """Sets the offering of this Service.

        The Service Offering code for the mail item ordered. Please note that this field is case sensitive. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer) Portal and refer to Shipping API Reference Data  # noqa: E501

        :param offering: The offering of this Service.  # noqa: E501
        :type: str
        """
        if offering is None:
            raise ValueError("Invalid value for `offering`, must not be `None`")  # noqa: E501

        self._offering = offering

    @property
    def type(self):
        """Gets the type of this Service.  # noqa: E501

        The system Service Type of the shipment. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer)  and refer to Shipping API Reference Data.  # noqa: E501

        :return: The type of this Service.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Service.

        The system Service Type of the shipment. For the list of permissible values, please go to Pro Shipping V2 API page on the Royal Mail API (Developer)  and refer to Shipping API Reference Data.  # noqa: E501

        :param type: The type of this Service.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def signature(self):
        """Gets the signature of this Service.  # noqa: E501

        For RM Tracked items only, this element specifies whether a signature is required on delivery. If this element is not included then it defaults to false.  # noqa: E501

        :return: The signature of this Service.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this Service.

        For RM Tracked items only, this element specifies whether a signature is required on delivery. If this element is not included then it defaults to false.  # noqa: E501

        :param signature: The signature of this Service.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def enhancements(self):
        """Gets the enhancements of this Service.  # noqa: E501


        :return: The enhancements of this Service.  # noqa: E501
        :rtype: ServiceEnhancements
        """
        return self._enhancements

    @enhancements.setter
    def enhancements(self, enhancements):
        """Sets the enhancements of this Service.


        :param enhancements: The enhancements of this Service.  # noqa: E501
        :type: ServiceEnhancements
        """

        self._enhancements = enhancements

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
        if issubclass(Service, dict):
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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other