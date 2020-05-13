# coding: utf-8

"""
    Royal Mail API Shipping V3 (REST)

    This API specification details the requirements for integrating with **Royal Mail API Shipping V3**.<br><br>It specifically covers how the Royal Mail API Shipping V3 can be used by business customers to conduct shipping activity with Royal Mail and provides the technical information to build this integration. This specification must be used with the relevant accompanying specifications for customers wishing to interface their systems with Royal Mail services.<br><br>Royal Mail API Shipping V3 exposes a fully RESTful service that allows account customers to create shipments, produce labels, and produce documentation for all the tasks required to ship domestic items with Royal Mail.<br><br>Built on industry standards, Royal Mail API Shipping V3 provides a simple and low cost method for customers to integrate with Royal Mail, and allows them to get shipping quickly. The API offers data streaming and offline barcoding to allow customers greater flexibility when generating their labels. There are no costs to customers for using the Royal Mail API Shipping V3 services, however customers’ own development costs must be covered by the customer developing the solution. Royal Mail will not accept any responsibility for these development, implementation and testing costs. Customers should address initial enquiries regarding development of systems for these purposes to their account handler.<br><br>This API can be used in conjunction with Royal Mail Pro Shipping, a GUI based shipping platform. For more details on Royal Mail Pro Shipping, including videos on and briefs on updating/ cancelling a shipment and Manifesting please refer to http://www.royalmail.com/pro-shipping-help.  # noqa: E501

    OpenAPI spec version: 3.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Manifest(object):
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
        'manifest_number': 'str',
        'manifest_image': 'str',
        'carrier_code': 'str',
        'service_code': 'str',
        'total_weight': 'float',
        'total_packages': 'int'
    }

    attribute_map = {
        'manifest_number': 'ManifestNumber',
        'manifest_image': 'ManifestImage',
        'carrier_code': 'CarrierCode',
        'service_code': 'ServiceCode',
        'total_weight': 'TotalWeight',
        'total_packages': 'TotalPackages'
    }

    def __init__(self, manifest_number=None, manifest_image=None, carrier_code=None, service_code=None, total_weight=None, total_packages=None):  # noqa: E501
        """Manifest - a model defined in Swagger"""  # noqa: E501
        self._manifest_number = None
        self._manifest_image = None
        self._carrier_code = None
        self._service_code = None
        self._total_weight = None
        self._total_packages = None
        self.discriminator = None
        if manifest_number is not None:
            self.manifest_number = manifest_number
        if manifest_image is not None:
            self.manifest_image = manifest_image
        if carrier_code is not None:
            self.carrier_code = carrier_code
        if service_code is not None:
            self.service_code = service_code
        if total_weight is not None:
            self.total_weight = total_weight
        if total_packages is not None:
            self.total_packages = total_packages

    @property
    def manifest_number(self):
        """Gets the manifest_number of this Manifest.  # noqa: E501

        Manifest Number  # noqa: E501

        :return: The manifest_number of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._manifest_number

    @manifest_number.setter
    def manifest_number(self, manifest_number):
        """Sets the manifest_number of this Manifest.

        Manifest Number  # noqa: E501

        :param manifest_number: The manifest_number of this Manifest.  # noqa: E501
        :type: str
        """

        self._manifest_number = manifest_number

    @property
    def manifest_image(self):
        """Gets the manifest_image of this Manifest.  # noqa: E501

        Manifest Image<br />A base 64 encoded string of the manifest PDF.  # noqa: E501

        :return: The manifest_image of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._manifest_image

    @manifest_image.setter
    def manifest_image(self, manifest_image):
        """Sets the manifest_image of this Manifest.

        Manifest Image<br />A base 64 encoded string of the manifest PDF.  # noqa: E501

        :param manifest_image: The manifest_image of this Manifest.  # noqa: E501
        :type: str
        """

        self._manifest_image = manifest_image

    @property
    def carrier_code(self):
        """Gets the carrier_code of this Manifest.  # noqa: E501

        Carrier Code<br />The carrier that this manifest is for.  # noqa: E501

        :return: The carrier_code of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this Manifest.

        Carrier Code<br />The carrier that this manifest is for.  # noqa: E501

        :param carrier_code: The carrier_code of this Manifest.  # noqa: E501
        :type: str
        """

        self._carrier_code = carrier_code

    @property
    def service_code(self):
        """Gets the service_code of this Manifest.  # noqa: E501

        Service Code<br />The service included in this Manifest. If more than one, Mixed will be returned.  # noqa: E501

        :return: The service_code of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this Manifest.

        Service Code<br />The service included in this Manifest. If more than one, Mixed will be returned.  # noqa: E501

        :param service_code: The service_code of this Manifest.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

    @property
    def total_weight(self):
        """Gets the total_weight of this Manifest.  # noqa: E501

        Total Weight<br />Sum of the weight of all the packages included on the Manifest in KGs.  # noqa: E501

        :return: The total_weight of this Manifest.  # noqa: E501
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this Manifest.

        Total Weight<br />Sum of the weight of all the packages included on the Manifest in KGs.  # noqa: E501

        :param total_weight: The total_weight of this Manifest.  # noqa: E501
        :type: float
        """

        self._total_weight = total_weight

    @property
    def total_packages(self):
        """Gets the total_packages of this Manifest.  # noqa: E501

        Total Packages<br />The total number of packages included on the Manifest.  # noqa: E501

        :return: The total_packages of this Manifest.  # noqa: E501
        :rtype: int
        """
        return self._total_packages

    @total_packages.setter
    def total_packages(self, total_packages):
        """Sets the total_packages of this Manifest.

        Total Packages<br />The total number of packages included on the Manifest.  # noqa: E501

        :param total_packages: The total_packages of this Manifest.  # noqa: E501
        :type: int
        """

        self._total_packages = total_packages

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
        if issubclass(Manifest, dict):
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
        if not isinstance(other, Manifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
