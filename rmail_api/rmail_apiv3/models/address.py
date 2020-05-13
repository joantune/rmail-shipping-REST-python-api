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


class Address(object):
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
        'address_id': 'str',
        'is_return_address': 'bool',
        'company_name': 'str',
        'contact_name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'town': 'str',
        'county': 'str',
        'country_code': 'str',
        'postcode': 'str',
        'phone_number': 'str',
        'email_address': 'str',
        'vat_number': 'str',
        'safeplace': 'str'
    }

    attribute_map = {
        'address_id': 'AddressId',
        'is_return_address': 'IsReturnAddress',
        'company_name': 'CompanyName',
        'contact_name': 'ContactName',
        'address_line1': 'AddressLine1',
        'address_line2': 'AddressLine2',
        'address_line3': 'AddressLine3',
        'town': 'Town',
        'county': 'County',
        'country_code': 'CountryCode',
        'postcode': 'Postcode',
        'phone_number': 'PhoneNumber',
        'email_address': 'EmailAddress',
        'vat_number': 'VatNumber',
        'safeplace': 'Safeplace'
    }

    def __init__(self, address_id=None, is_return_address=None, company_name=None, contact_name=None, address_line1=None, address_line2=None, address_line3=None, town=None, county=None, country_code=None, postcode=None, phone_number=None, email_address=None, vat_number=None, safeplace=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._address_id = None
        self._is_return_address = None
        self._company_name = None
        self._contact_name = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._town = None
        self._county = None
        self._country_code = None
        self._postcode = None
        self._phone_number = None
        self._email_address = None
        self._vat_number = None
        self._safeplace = None
        self.discriminator = None
        if address_id is not None:
            self.address_id = address_id
        self.is_return_address = is_return_address
        if company_name is not None:
            self.company_name = company_name
        self.contact_name = contact_name
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        self.town = town
        if county is not None:
            self.county = county
        self.country_code = country_code
        if postcode is not None:
            self.postcode = postcode
        if phone_number is not None:
            self.phone_number = phone_number
        if email_address is not None:
            self.email_address = email_address
        if vat_number is not None:
            self.vat_number = vat_number
        if safeplace is not None:
            self.safeplace = safeplace

    @property
    def address_id(self):
        """Gets the address_id of this Address.  # noqa: E501

        Address ID<br />Your unique identifier for this address.<br />If not provided, a GUID will be generated.  # noqa: E501

        :return: The address_id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this Address.

        Address ID<br />Your unique identifier for this address.<br />If not provided, a GUID will be generated.  # noqa: E501

        :param address_id: The address_id of this Address.  # noqa: E501
        :type: str
        """

        self._address_id = address_id

    @property
    def is_return_address(self):
        """Gets the is_return_address of this Address.  # noqa: E501

        Is Return Address<br />If true, then this address is also available as a return address.  # noqa: E501

        :return: The is_return_address of this Address.  # noqa: E501
        :rtype: bool
        """
        return self._is_return_address

    @is_return_address.setter
    def is_return_address(self, is_return_address):
        """Sets the is_return_address of this Address.

        Is Return Address<br />If true, then this address is also available as a return address.  # noqa: E501

        :param is_return_address: The is_return_address of this Address.  # noqa: E501
        :type: bool
        """
        if is_return_address is None:
            raise ValueError("Invalid value for `is_return_address`, must not be `None`")  # noqa: E501

        self._is_return_address = is_return_address

    @property
    def company_name(self):
        """Gets the company_name of this Address.  # noqa: E501

        Company Name<br />*Ignored if is a return address*  # noqa: E501

        :return: The company_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Address.

        Company Name<br />*Ignored if is a return address*  # noqa: E501

        :param company_name: The company_name of this Address.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_name(self):
        """Gets the contact_name of this Address.  # noqa: E501

        Contact Name / Return Name  # noqa: E501

        :return: The contact_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this Address.

        Contact Name / Return Name  # noqa: E501

        :param contact_name: The contact_name of this Address.  # noqa: E501
        :type: str
        """
        if contact_name is None:
            raise ValueError("Invalid value for `contact_name`, must not be `None`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        Address Line 1  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        Address Line 2  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this Address.  # noqa: E501

        Address Line 3  # noqa: E501

        :return: The address_line3 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this Address.

        Address Line 3  # noqa: E501

        :param address_line3: The address_line3 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line3 = address_line3

    @property
    def town(self):
        """Gets the town of this Address.  # noqa: E501

        Town  # noqa: E501

        :return: The town of this Address.  # noqa: E501
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """Sets the town of this Address.

        Town  # noqa: E501

        :param town: The town of this Address.  # noqa: E501
        :type: str
        """
        if town is None:
            raise ValueError("Invalid value for `town`, must not be `None`")  # noqa: E501

        self._town = town

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501

        County / State / Province<br />Conditional dependent on country.<br />USA, Australia and Canada all require a valid state code or name.  # noqa: E501

        :return: The county of this Address.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.

        County / State / Province<br />Conditional dependent on country.<br />USA, Australia and Canada all require a valid state code or name.  # noqa: E501

        :param county: The county of this Address.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        Country Code<br />[ISO Alpha-2 Country Code](https://www.nationsonline.org/oneworld/country_code_list.htm) per ISO 3166 Standard<br />*Required to be GB if is a return address*  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        Country Code<br />[ISO Alpha-2 Country Code](https://www.nationsonline.org/oneworld/country_code_list.htm) per ISO 3166 Standard<br />*Required to be GB if is a return address*  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def postcode(self):
        """Gets the postcode of this Address.  # noqa: E501

        Postcode / Zip<br />Required for domestic addresses and some international addresses.  # noqa: E501

        :return: The postcode of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this Address.

        Postcode / Zip<br />Required for domestic addresses and some international addresses.  # noqa: E501

        :param postcode: The postcode of this Address.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def phone_number(self):
        """Gets the phone_number of this Address.  # noqa: E501

        Contact Phone Number<br />Required for destination addresses where SMS notifications are requested.<br />(Service Enhancement Code 13 or 16)<br />*Ignored if is a return address*  # noqa: E501

        :return: The phone_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Address.

        Contact Phone Number<br />Required for destination addresses where SMS notifications are requested.<br />(Service Enhancement Code 13 or 16)<br />*Ignored if is a return address*  # noqa: E501

        :param phone_number: The phone_number of this Address.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email_address(self):
        """Gets the email_address of this Address.  # noqa: E501

        Contact Email Address<br />Required for destination addresses where email notifications are requested.<br />(Service Enhancement Code 14 or 16)<br />*Ignored if is a Return Address*  # noqa: E501

        :return: The email_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Address.

        Contact Email Address<br />Required for destination addresses where email notifications are requested.<br />(Service Enhancement Code 14 or 16)<br />*Ignored if is a Return Address*  # noqa: E501

        :param email_address: The email_address of this Address.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def vat_number(self):
        """Gets the vat_number of this Address.  # noqa: E501

        VAT Number<br />*Ignored if is a return address*  # noqa: E501

        :return: The vat_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this Address.

        VAT Number<br />*Ignored if is a return address*  # noqa: E501

        :param vat_number: The vat_number of this Address.  # noqa: E501
        :type: str
        """

        self._vat_number = vat_number

    @property
    def safeplace(self):
        """Gets the safeplace of this Address.  # noqa: E501

        Safeplace<br />Free text to describe a safe place to leave the parcel if the service allows it.<br />*Ignored if is a return address*  # noqa: E501

        :return: The safeplace of this Address.  # noqa: E501
        :rtype: str
        """
        return self._safeplace

    @safeplace.setter
    def safeplace(self, safeplace):
        """Sets the safeplace of this Address.

        Safeplace<br />Free text to describe a safe place to leave the parcel if the service allows it.<br />*Ignored if is a return address*  # noqa: E501

        :param safeplace: The safeplace of this Address.  # noqa: E501
        :type: str
        """

        self._safeplace = safeplace

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
