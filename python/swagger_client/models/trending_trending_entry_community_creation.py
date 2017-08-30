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


class TrendingTrendingEntryCommunityCreation(object):
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
        'media': 'str',
        'title': 'str',
        'author': 'str',
        'author_membership_id': 'int',
        'post_id': 'int',
        'body': 'str',
        'upvotes': 'int'
    }

    attribute_map = {
        'media': 'media',
        'title': 'title',
        'author': 'author',
        'author_membership_id': 'authorMembershipId',
        'post_id': 'postId',
        'body': 'body',
        'upvotes': 'upvotes'
    }

    def __init__(self, media=None, title=None, author=None, author_membership_id=None, post_id=None, body=None, upvotes=None):
        """
        TrendingTrendingEntryCommunityCreation - a model defined in Swagger
        """

        self._media = None
        self._title = None
        self._author = None
        self._author_membership_id = None
        self._post_id = None
        self._body = None
        self._upvotes = None

        if media is not None:
          self.media = media
        if title is not None:
          self.title = title
        if author is not None:
          self.author = author
        if author_membership_id is not None:
          self.author_membership_id = author_membership_id
        if post_id is not None:
          self.post_id = post_id
        if body is not None:
          self.body = body
        if upvotes is not None:
          self.upvotes = upvotes

    @property
    def media(self):
        """
        Gets the media of this TrendingTrendingEntryCommunityCreation.

        :return: The media of this TrendingTrendingEntryCommunityCreation.
        :rtype: str
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this TrendingTrendingEntryCommunityCreation.

        :param media: The media of this TrendingTrendingEntryCommunityCreation.
        :type: str
        """

        self._media = media

    @property
    def title(self):
        """
        Gets the title of this TrendingTrendingEntryCommunityCreation.

        :return: The title of this TrendingTrendingEntryCommunityCreation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this TrendingTrendingEntryCommunityCreation.

        :param title: The title of this TrendingTrendingEntryCommunityCreation.
        :type: str
        """

        self._title = title

    @property
    def author(self):
        """
        Gets the author of this TrendingTrendingEntryCommunityCreation.

        :return: The author of this TrendingTrendingEntryCommunityCreation.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this TrendingTrendingEntryCommunityCreation.

        :param author: The author of this TrendingTrendingEntryCommunityCreation.
        :type: str
        """

        self._author = author

    @property
    def author_membership_id(self):
        """
        Gets the author_membership_id of this TrendingTrendingEntryCommunityCreation.

        :return: The author_membership_id of this TrendingTrendingEntryCommunityCreation.
        :rtype: int
        """
        return self._author_membership_id

    @author_membership_id.setter
    def author_membership_id(self, author_membership_id):
        """
        Sets the author_membership_id of this TrendingTrendingEntryCommunityCreation.

        :param author_membership_id: The author_membership_id of this TrendingTrendingEntryCommunityCreation.
        :type: int
        """

        self._author_membership_id = author_membership_id

    @property
    def post_id(self):
        """
        Gets the post_id of this TrendingTrendingEntryCommunityCreation.

        :return: The post_id of this TrendingTrendingEntryCommunityCreation.
        :rtype: int
        """
        return self._post_id

    @post_id.setter
    def post_id(self, post_id):
        """
        Sets the post_id of this TrendingTrendingEntryCommunityCreation.

        :param post_id: The post_id of this TrendingTrendingEntryCommunityCreation.
        :type: int
        """

        self._post_id = post_id

    @property
    def body(self):
        """
        Gets the body of this TrendingTrendingEntryCommunityCreation.

        :return: The body of this TrendingTrendingEntryCommunityCreation.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this TrendingTrendingEntryCommunityCreation.

        :param body: The body of this TrendingTrendingEntryCommunityCreation.
        :type: str
        """

        self._body = body

    @property
    def upvotes(self):
        """
        Gets the upvotes of this TrendingTrendingEntryCommunityCreation.

        :return: The upvotes of this TrendingTrendingEntryCommunityCreation.
        :rtype: int
        """
        return self._upvotes

    @upvotes.setter
    def upvotes(self, upvotes):
        """
        Sets the upvotes of this TrendingTrendingEntryCommunityCreation.

        :param upvotes: The upvotes of this TrendingTrendingEntryCommunityCreation.
        :type: int
        """

        self._upvotes = upvotes

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
        if not isinstance(other, TrendingTrendingEntryCommunityCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
