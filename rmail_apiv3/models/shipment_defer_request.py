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


class ShipmentDeferRequest(object):
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
        'shipment_id': 'str',
        'shipment_date': 'date'
    }

    attribute_map = {
        'shipment_id': 'ShipmentId',
        'shipment_date': 'ShipmentDate'
    }

    def __init__(self, shipment_id=None, shipment_date=None):  # noqa: E501
        """ShipmentDeferRequest - a model defined in Swagger"""  # noqa: E501
        self._shipment_id = None
        self._shipment_date = None
        self.discriminator = None
        self.shipment_id = shipment_id
        self.shipment_date = shipment_date

    @property
    def shipment_id(self):
        """Gets the shipment_id of this ShipmentDeferRequest.  # noqa: E501

        Shipment Id<br />The tracking number or Unique Id of the shipment to defer.  # noqa: E501

        :return: The shipment_id of this ShipmentDeferRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this ShipmentDeferRequest.

        Shipment Id<br />The tracking number or Unique Id of the shipment to defer.  # noqa: E501

        :param shipment_id: The shipment_id of this ShipmentDeferRequest.  # noqa: E501
        :type: str
        """
        if shipment_id is None:
            raise ValueError("Invalid value for `shipment_id`, must not be `None`")  # noqa: E501

        self._shipment_id = shipment_id

    @property
    def shipment_date(self):
        """Gets the shipment_date of this ShipmentDeferRequest.  # noqa: E501

        Shipment Date<br />Date of despatch – YYYY-MM-DD<br />Cannot be in the past. Max 28 days in the future.  # noqa: E501

        :return: The shipment_date of this ShipmentDeferRequest.  # noqa: E501
        :rtype: date
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this ShipmentDeferRequest.

        Shipment Date<br />Date of despatch – YYYY-MM-DD<br />Cannot be in the past. Max 28 days in the future.  # noqa: E501

        :param shipment_date: The shipment_date of this ShipmentDeferRequest.  # noqa: E501
        :type: date
        """
        if shipment_date is None:
            raise ValueError("Invalid value for `shipment_date`, must not be `None`")  # noqa: E501

        self._shipment_date = shipment_date

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
        if issubclass(ShipmentDeferRequest, dict):
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
        if not isinstance(other, ShipmentDeferRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other