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

class DestinationDetails(object):
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
        'country_code': 'str',
        'postcode': 'str'
    }

    attribute_map = {
        'country_code': 'CountryCode',
        'postcode': 'Postcode'
    }

    def __init__(self, country_code=None, postcode=None):  # noqa: E501
        """DestinationDetails - a model defined in Swagger"""  # noqa: E501
        self._country_code = None
        self._postcode = None
        self.discriminator = None
        self.country_code = country_code
        if postcode is not None:
            self.postcode = postcode

    @property
    def country_code(self):
        """Gets the country_code of this DestinationDetails.  # noqa: E501

        Country Code <br />2 Digit ISO Country Code, per ISO 3166 Standard.  # noqa: E501

        :return: The country_code of this DestinationDetails.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this DestinationDetails.

        Country Code <br />2 Digit ISO Country Code, per ISO 3166 Standard.  # noqa: E501

        :param country_code: The country_code of this DestinationDetails.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def postcode(self):
        """Gets the postcode of this DestinationDetails.  # noqa: E501

        Postcode / Zip <br />Required for United Kingdom addresses and some international addresses. <br />The Countries API can be used to check whether postcode/zip code is required for a country.  <br />Up to 20 characters may be allowed, however it is carrier dependent and some carriers may allow less. <br />Royal Mail: 9 characters.  # noqa: E501

        :return: The postcode of this DestinationDetails.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DestinationDetails.

        Postcode / Zip <br />Required for United Kingdom addresses and some international addresses. <br />The Countries API can be used to check whether postcode/zip code is required for a country.  <br />Up to 20 characters may be allowed, however it is carrier dependent and some carriers may allow less. <br />Royal Mail: 9 characters.  # noqa: E501

        :param postcode: The postcode of this DestinationDetails.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

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
        if issubclass(DestinationDetails, dict):
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
        if not isinstance(other, DestinationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
