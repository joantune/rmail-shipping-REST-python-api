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


class Packaging(object):
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
        'packaging_id': 'str',
        'name': 'str',
        'weight': 'float',
        'weight_unit_of_measure': 'str',
        'length': 'float',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'packaging_id': 'PackagingId',
        'name': 'Name',
        'weight': 'Weight',
        'weight_unit_of_measure': 'WeightUnitOfMeasure',
        'length': 'Length',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, packaging_id=None, name=None, weight=None, weight_unit_of_measure='KG', length=None, width=None, height=None):  # noqa: E501
        """Packaging - a model defined in Swagger"""  # noqa: E501
        self._packaging_id = None
        self._name = None
        self._weight = None
        self._weight_unit_of_measure = None
        self._length = None
        self._width = None
        self._height = None
        self.discriminator = None
        if packaging_id is not None:
            self.packaging_id = packaging_id
        self.name = name
        if weight is not None:
            self.weight = weight
        if weight_unit_of_measure is not None:
            self.weight_unit_of_measure = weight_unit_of_measure
        self.length = length
        self.width = width
        self.height = height

    @property
    def packaging_id(self):
        """Gets the packaging_id of this Packaging.  # noqa: E501

        Packaging Unique ID<br />Your unique identifier for these packaging details.<br />If not provided, a GUID will be generated.  # noqa: E501

        :return: The packaging_id of this Packaging.  # noqa: E501
        :rtype: str
        """
        return self._packaging_id

    @packaging_id.setter
    def packaging_id(self, packaging_id):
        """Sets the packaging_id of this Packaging.

        Packaging Unique ID<br />Your unique identifier for these packaging details.<br />If not provided, a GUID will be generated.  # noqa: E501

        :param packaging_id: The packaging_id of this Packaging.  # noqa: E501
        :type: str
        """

        self._packaging_id = packaging_id

    @property
    def name(self):
        """Gets the name of this Packaging.  # noqa: E501

        Name<br />The descriptive name of these packaging details  # noqa: E501

        :return: The name of this Packaging.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Packaging.

        Name<br />The descriptive name of these packaging details  # noqa: E501

        :param name: The name of this Packaging.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def weight(self):
        """Gets the weight of this Packaging.  # noqa: E501

        Packaging Weight<br />The weight of this packaging.<br />Min weight: 1 gram.  # noqa: E501

        :return: The weight of this Packaging.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Packaging.

        Packaging Weight<br />The weight of this packaging.<br />Min weight: 1 gram.  # noqa: E501

        :param weight: The weight of this Packaging.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def weight_unit_of_measure(self):
        """Gets the weight_unit_of_measure of this Packaging.  # noqa: E501

        Weight Unit of Measure  # noqa: E501

        :return: The weight_unit_of_measure of this Packaging.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit_of_measure

    @weight_unit_of_measure.setter
    def weight_unit_of_measure(self, weight_unit_of_measure):
        """Sets the weight_unit_of_measure of this Packaging.

        Weight Unit of Measure  # noqa: E501

        :param weight_unit_of_measure: The weight_unit_of_measure of this Packaging.  # noqa: E501
        :type: str
        """
        allowed_values = ["KG", "Grams"]  # noqa: E501
        if weight_unit_of_measure not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_unit_of_measure` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_unit_of_measure, allowed_values)
            )

        self._weight_unit_of_measure = weight_unit_of_measure

    @property
    def length(self):
        """Gets the length of this Packaging.  # noqa: E501

        Packaging Length<br />The length of this packaging in CM  # noqa: E501

        :return: The length of this Packaging.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Packaging.

        Packaging Length<br />The length of this packaging in CM  # noqa: E501

        :param length: The length of this Packaging.  # noqa: E501
        :type: float
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def width(self):
        """Gets the width of this Packaging.  # noqa: E501

        Packaging Width<br />The width of this packaging in CM  # noqa: E501

        :return: The width of this Packaging.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Packaging.

        Packaging Width<br />The width of this packaging in CM  # noqa: E501

        :param width: The width of this Packaging.  # noqa: E501
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this Packaging.  # noqa: E501

        Packaging Height<br />The height of this packaging in CM  # noqa: E501

        :return: The height of this Packaging.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Packaging.

        Packaging Height<br />The height of this packaging in CM  # noqa: E501

        :param height: The height of this Packaging.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

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
        if issubclass(Packaging, dict):
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
        if not isinstance(other, Packaging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
