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

class RoyalMailViewShippingAccountLocationShippingLocationForAccount(object):
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
        'shipping_location_id': 'str',
        'location_alias': 'str',
        'carrier_specifics': 'RoyalMailViewShippingAccountLocation',
        'timezone': 'str',
        'last_updated_date_utc': 'datetime',
        'last_updated_by': 'str',
        'address': 'ShippingLocationAddress'
    }

    attribute_map = {
        'shipping_location_id': 'ShippingLocationId',
        'location_alias': 'LocationAlias',
        'carrier_specifics': 'CarrierSpecifics',
        'timezone': 'Timezone',
        'last_updated_date_utc': 'LastUpdatedDateUtc',
        'last_updated_by': 'LastUpdatedBy',
        'address': 'Address'
    }

    def __init__(self, shipping_location_id=None, location_alias=None, carrier_specifics=None, timezone=None, last_updated_date_utc=None, last_updated_by=None, address=None):  # noqa: E501
        """RoyalMailViewShippingAccountLocationShippingLocationForAccount - a model defined in Swagger"""  # noqa: E501
        self._shipping_location_id = None
        self._location_alias = None
        self._carrier_specifics = None
        self._timezone = None
        self._last_updated_date_utc = None
        self._last_updated_by = None
        self._address = None
        self.discriminator = None
        self.shipping_location_id = shipping_location_id
        self.location_alias = location_alias
        self.carrier_specifics = carrier_specifics
        self.timezone = timezone
        self.last_updated_date_utc = last_updated_date_utc
        self.last_updated_by = last_updated_by
        self.address = address

    @property
    def shipping_location_id(self):
        """Gets the shipping_location_id of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501

        Shipping Location Id <br />The system identifier for this shipping location.  # noqa: E501

        :return: The shipping_location_id of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: str
        """
        return self._shipping_location_id

    @shipping_location_id.setter
    def shipping_location_id(self, shipping_location_id):
        """Sets the shipping_location_id of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.

        Shipping Location Id <br />The system identifier for this shipping location.  # noqa: E501

        :param shipping_location_id: The shipping_location_id of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: str
        """
        if shipping_location_id is None:
            raise ValueError("Invalid value for `shipping_location_id`, must not be `None`")  # noqa: E501

        self._shipping_location_id = shipping_location_id

    @property
    def location_alias(self):
        """Gets the location_alias of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501

        Shipping Location Alias <br />Your identifier for this shipping location. Must be unique.  # noqa: E501

        :return: The location_alias of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: str
        """
        return self._location_alias

    @location_alias.setter
    def location_alias(self, location_alias):
        """Sets the location_alias of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.

        Shipping Location Alias <br />Your identifier for this shipping location. Must be unique.  # noqa: E501

        :param location_alias: The location_alias of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: str
        """
        if location_alias is None:
            raise ValueError("Invalid value for `location_alias`, must not be `None`")  # noqa: E501

        self._location_alias = location_alias

    @property
    def carrier_specifics(self):
        """Gets the carrier_specifics of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501


        :return: The carrier_specifics of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: RoyalMailViewShippingAccountLocation
        """
        return self._carrier_specifics

    @carrier_specifics.setter
    def carrier_specifics(self, carrier_specifics):
        """Sets the carrier_specifics of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.


        :param carrier_specifics: The carrier_specifics of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: RoyalMailViewShippingAccountLocation
        """
        if carrier_specifics is None:
            raise ValueError("Invalid value for `carrier_specifics`, must not be `None`")  # noqa: E501

        self._carrier_specifics = carrier_specifics

    @property
    def timezone(self):
        """Gets the timezone of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501

        Time zone  # noqa: E501

        :return: The timezone of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.

        Time zone  # noqa: E501

        :param timezone: The timezone of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def last_updated_date_utc(self):
        """Gets the last_updated_date_utc of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501

        Last Updated Date UTC  # noqa: E501

        :return: The last_updated_date_utc of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date_utc

    @last_updated_date_utc.setter
    def last_updated_date_utc(self, last_updated_date_utc):
        """Sets the last_updated_date_utc of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.

        Last Updated Date UTC  # noqa: E501

        :param last_updated_date_utc: The last_updated_date_utc of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: datetime
        """
        if last_updated_date_utc is None:
            raise ValueError("Invalid value for `last_updated_date_utc`, must not be `None`")  # noqa: E501

        self._last_updated_date_utc = last_updated_date_utc

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501

        Last Updated By  # noqa: E501

        :return: The last_updated_by of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.

        Last Updated By  # noqa: E501

        :param last_updated_by: The last_updated_by of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: str
        """
        if last_updated_by is None:
            raise ValueError("Invalid value for `last_updated_by`, must not be `None`")  # noqa: E501

        self._last_updated_by = last_updated_by

    @property
    def address(self):
        """Gets the address of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501


        :return: The address of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :rtype: ShippingLocationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.


        :param address: The address of this RoyalMailViewShippingAccountLocationShippingLocationForAccount.  # noqa: E501
        :type: ShippingLocationAddress
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

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
        if issubclass(RoyalMailViewShippingAccountLocationShippingLocationForAccount, dict):
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
        if not isinstance(other, RoyalMailViewShippingAccountLocationShippingLocationForAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
