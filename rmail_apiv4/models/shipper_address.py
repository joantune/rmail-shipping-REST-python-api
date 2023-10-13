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

class ShipperAddress(object):
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
        'contact_name': 'str',
        'company_name': 'str',
        'contact_email': 'str',
        'contact_phone': 'str',
        'line1': 'str',
        'line2': 'str',
        'line3': 'str',
        'town': 'str',
        'postcode': 'str',
        'county': 'str',
        'country_code': 'str',
        'what3_words': 'str'
    }

    attribute_map = {
        'contact_name': 'ContactName',
        'company_name': 'CompanyName',
        'contact_email': 'ContactEmail',
        'contact_phone': 'ContactPhone',
        'line1': 'Line1',
        'line2': 'Line2',
        'line3': 'Line3',
        'town': 'Town',
        'postcode': 'Postcode',
        'county': 'County',
        'country_code': 'CountryCode',
        'what3_words': 'What3Words'
    }

    def __init__(self, contact_name=None, company_name=None, contact_email=None, contact_phone=None, line1=None, line2=None, line3=None, town=None, postcode=None, county=None, country_code=None, what3_words=None):  # noqa: E501
        """ShipperAddress - a model defined in Swagger"""  # noqa: E501
        self._contact_name = None
        self._company_name = None
        self._contact_email = None
        self._contact_phone = None
        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._town = None
        self._postcode = None
        self._county = None
        self._country_code = None
        self._what3_words = None
        self.discriminator = None
        if contact_name is not None:
            self.contact_name = contact_name
        if company_name is not None:
            self.company_name = company_name
        if contact_email is not None:
            self.contact_email = contact_email
        if contact_phone is not None:
            self.contact_phone = contact_phone
        self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if line3 is not None:
            self.line3 = line3
        self.town = town
        if postcode is not None:
            self.postcode = postcode
        if county is not None:
            self.county = county
        self.country_code = country_code
        if what3_words is not None:
            self.what3_words = what3_words

    @property
    def contact_name(self):
        """Gets the contact_name of this ShipperAddress.  # noqa: E501

        Either Contact Name or Company Name must be provided. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The contact_name of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this ShipperAddress.

        Either Contact Name or Company Name must be provided. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param contact_name: The contact_name of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def company_name(self):
        """Gets the company_name of this ShipperAddress.  # noqa: E501

        Either Contact Name or Company Name must be provided. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The company_name of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ShipperAddress.

        Either Contact Name or Company Name must be provided. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param company_name: The company_name of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_email(self):
        """Gets the contact_email of this ShipperAddress.  # noqa: E501

        Email address.  # noqa: E501

        :return: The contact_email of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this ShipperAddress.

        Email address.  # noqa: E501

        :param contact_email: The contact_email of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_phone(self):
        """Gets the contact_phone of this ShipperAddress.  # noqa: E501

        Phone number.  # noqa: E501

        :return: The contact_phone of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this ShipperAddress.

        Phone number.  # noqa: E501

        :param contact_phone: The contact_phone of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def line1(self):
        """Gets the line1 of this ShipperAddress.  # noqa: E501

        First Line Address <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The line1 of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this ShipperAddress.

        First Line Address <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param line1: The line1 of this ShipperAddress.  # noqa: E501
        :type: str
        """
        if line1 is None:
            raise ValueError("Invalid value for `line1`, must not be `None`")  # noqa: E501

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this ShipperAddress.  # noqa: E501

        Second Line Address, if applicable <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The line2 of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this ShipperAddress.

        Second Line Address, if applicable <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param line2: The line2 of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def line3(self):
        """Gets the line3 of this ShipperAddress.  # noqa: E501

        Third Line Address, if applicable <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The line3 of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """Sets the line3 of this ShipperAddress.

        Third Line Address, if applicable <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param line3: The line3 of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._line3 = line3

    @property
    def town(self):
        """Gets the town of this ShipperAddress.  # noqa: E501

        Town <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The town of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """Sets the town of this ShipperAddress.

        Town <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param town: The town of this ShipperAddress.  # noqa: E501
        :type: str
        """
        if town is None:
            raise ValueError("Invalid value for `town`, must not be `None`")  # noqa: E501

        self._town = town

    @property
    def postcode(self):
        """Gets the postcode of this ShipperAddress.  # noqa: E501

        Postcode / Zip <br />Required for United Kingdom addresses and some international addresses. <br />The Countries API can be used to check whether postcode/zip code is required for a country. <br />Up to 20 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 10 characters  # noqa: E501

        :return: The postcode of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this ShipperAddress.

        Postcode / Zip <br />Required for United Kingdom addresses and some international addresses. <br />The Countries API can be used to check whether postcode/zip code is required for a country. <br />Up to 20 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 10 characters  # noqa: E501

        :param postcode: The postcode of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def county(self):
        """Gets the county of this ShipperAddress.  # noqa: E501

        County / State / Province <br />May be required depending on the country. <br />USA, Australia and Canada all require a valid state code or name. <br />The Countries API can be used to check whether county/state is required for a country. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :return: The county of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ShipperAddress.

        County / State / Province <br />May be required depending on the country. <br />USA, Australia and Canada all require a valid state code or name. <br />The Countries API can be used to check whether county/state is required for a country. <br />Up to 50 characters may be allowed, however it is carrier dependent and some carriers may allow less.<br>Royal Mail: 40 characters  # noqa: E501

        :param county: The county of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def country_code(self):
        """Gets the country_code of this ShipperAddress.  # noqa: E501

        Country Code <br />2 Digit ISO Country Code, per ISO 3166 Standard.  # noqa: E501

        :return: The country_code of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ShipperAddress.

        Country Code <br />2 Digit ISO Country Code, per ISO 3166 Standard.  # noqa: E501

        :param country_code: The country_code of this ShipperAddress.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def what3_words(self):
        """Gets the what3_words of this ShipperAddress.  # noqa: E501

        The what3words identifier for this address.  # noqa: E501

        :return: The what3_words of this ShipperAddress.  # noqa: E501
        :rtype: str
        """
        return self._what3_words

    @what3_words.setter
    def what3_words(self, what3_words):
        """Sets the what3_words of this ShipperAddress.

        The what3words identifier for this address.  # noqa: E501

        :param what3_words: The what3_words of this ShipperAddress.  # noqa: E501
        :type: str
        """

        self._what3_words = what3_words

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
        if issubclass(ShipperAddress, dict):
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
        if not isinstance(other, ShipperAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
