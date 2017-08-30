# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20033(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'response': 'dict(str, DestinyMilestonesDestinyPublicMilestone)',
        'error_code': 'ExceptionsPlatformErrorCodes',
        'throttle_seconds': 'int',
        'error_status': 'str',
        'message': 'str',
        'message_data': 'dict(str, str)'
    }

    attribute_map = {
        'response': 'Response',
        'error_code': 'ErrorCode',
        'throttle_seconds': 'ThrottleSeconds',
        'error_status': 'ErrorStatus',
        'message': 'Message',
        'message_data': 'MessageData'
    }

    def __init__(self, response=None, error_code=None, throttle_seconds=None, error_status=None, message=None, message_data=None):
        """
        InlineResponse20033 - a model defined in Swagger
        """

        self._response = None
        self._error_code = None
        self._throttle_seconds = None
        self._error_status = None
        self._message = None
        self._message_data = None

        if response is not None:
          self.response = response
        if error_code is not None:
          self.error_code = error_code
        if throttle_seconds is not None:
          self.throttle_seconds = throttle_seconds
        if error_status is not None:
          self.error_status = error_status
        if message is not None:
          self.message = message
        if message_data is not None:
          self.message_data = message_data

    @property
    def response(self):
        """
        Gets the response of this InlineResponse20033.

        :return: The response of this InlineResponse20033.
        :rtype: dict(str, DestinyMilestonesDestinyPublicMilestone)
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this InlineResponse20033.

        :param response: The response of this InlineResponse20033.
        :type: dict(str, DestinyMilestonesDestinyPublicMilestone)
        """

        self._response = response

    @property
    def error_code(self):
        """
        Gets the error_code of this InlineResponse20033.

        :return: The error_code of this InlineResponse20033.
        :rtype: ExceptionsPlatformErrorCodes
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this InlineResponse20033.

        :param error_code: The error_code of this InlineResponse20033.
        :type: ExceptionsPlatformErrorCodes
        """

        self._error_code = error_code

    @property
    def throttle_seconds(self):
        """
        Gets the throttle_seconds of this InlineResponse20033.

        :return: The throttle_seconds of this InlineResponse20033.
        :rtype: int
        """
        return self._throttle_seconds

    @throttle_seconds.setter
    def throttle_seconds(self, throttle_seconds):
        """
        Sets the throttle_seconds of this InlineResponse20033.

        :param throttle_seconds: The throttle_seconds of this InlineResponse20033.
        :type: int
        """

        self._throttle_seconds = throttle_seconds

    @property
    def error_status(self):
        """
        Gets the error_status of this InlineResponse20033.

        :return: The error_status of this InlineResponse20033.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """
        Sets the error_status of this InlineResponse20033.

        :param error_status: The error_status of this InlineResponse20033.
        :type: str
        """

        self._error_status = error_status

    @property
    def message(self):
        """
        Gets the message of this InlineResponse20033.

        :return: The message of this InlineResponse20033.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse20033.

        :param message: The message of this InlineResponse20033.
        :type: str
        """

        self._message = message

    @property
    def message_data(self):
        """
        Gets the message_data of this InlineResponse20033.

        :return: The message_data of this InlineResponse20033.
        :rtype: dict(str, str)
        """
        return self._message_data

    @message_data.setter
    def message_data(self, message_data):
        """
        Sets the message_data of this InlineResponse20033.

        :param message_data: The message_data of this InlineResponse20033.
        :type: dict(str, str)
        """

        self._message_data = message_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse20033):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
