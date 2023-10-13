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

class RoyalMailGetOfflineBarcodingResponse(object):
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
        'prefix': 'str',
        'barcode_range_start': 'str',
        'barcode_range_end': 'str',
        'suffix': 'str',
        'channel_id': 'str'
    }

    attribute_map = {
        'prefix': 'Prefix',
        'barcode_range_start': 'BarcodeRangeStart',
        'barcode_range_end': 'BarcodeRangeEnd',
        'suffix': 'Suffix',
        'channel_id': 'ChannelId'
    }

    def __init__(self, prefix=None, barcode_range_start=None, barcode_range_end=None, suffix=None, channel_id=None):  # noqa: E501
        """RoyalMailGetOfflineBarcodingResponse - a model defined in Swagger"""  # noqa: E501
        self._prefix = None
        self._barcode_range_start = None
        self._barcode_range_end = None
        self._suffix = None
        self._channel_id = None
        self.discriminator = None
        if prefix is not None:
            self.prefix = prefix
        if barcode_range_start is not None:
            self.barcode_range_start = barcode_range_start
        if barcode_range_end is not None:
            self.barcode_range_end = barcode_range_end
        if suffix is not None:
            self.suffix = suffix
        if channel_id is not None:
            self.channel_id = channel_id

    @property
    def prefix(self):
        """Gets the prefix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501

        Barcode prefix  # noqa: E501

        :return: The prefix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this RoyalMailGetOfflineBarcodingResponse.

        Barcode prefix  # noqa: E501

        :param prefix: The prefix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def barcode_range_start(self):
        """Gets the barcode_range_start of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501

        Start of barcode number range  # noqa: E501

        :return: The barcode_range_start of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :rtype: str
        """
        return self._barcode_range_start

    @barcode_range_start.setter
    def barcode_range_start(self, barcode_range_start):
        """Sets the barcode_range_start of this RoyalMailGetOfflineBarcodingResponse.

        Start of barcode number range  # noqa: E501

        :param barcode_range_start: The barcode_range_start of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :type: str
        """

        self._barcode_range_start = barcode_range_start

    @property
    def barcode_range_end(self):
        """Gets the barcode_range_end of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501

        End of barcode number range  # noqa: E501

        :return: The barcode_range_end of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :rtype: str
        """
        return self._barcode_range_end

    @barcode_range_end.setter
    def barcode_range_end(self, barcode_range_end):
        """Sets the barcode_range_end of this RoyalMailGetOfflineBarcodingResponse.

        End of barcode number range  # noqa: E501

        :param barcode_range_end: The barcode_range_end of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :type: str
        """

        self._barcode_range_end = barcode_range_end

    @property
    def suffix(self):
        """Gets the suffix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501

        Fixed value - always GB  # noqa: E501

        :return: The suffix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this RoyalMailGetOfflineBarcodingResponse.

        Fixed value - always GB  # noqa: E501

        :param suffix: The suffix of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def channel_id(self):
        """Gets the channel_id of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501

        The Channel ID sent in the request, If none was sent in the request, then it will be populated with the Channel Id assigned in the system to the customer account.  # noqa: E501

        :return: The channel_id of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this RoyalMailGetOfflineBarcodingResponse.

        The Channel ID sent in the request, If none was sent in the request, then it will be populated with the Channel Id assigned in the system to the customer account.  # noqa: E501

        :param channel_id: The channel_id of this RoyalMailGetOfflineBarcodingResponse.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

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
        if issubclass(RoyalMailGetOfflineBarcodingResponse, dict):
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
        if not isinstance(other, RoyalMailGetOfflineBarcodingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
