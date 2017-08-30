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


class ContentContentItemPublicContract(object):
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
        'content_id': 'int',
        'c_type': 'str',
        'cms_path': 'str',
        'creation_date': 'datetime',
        'modify_date': 'datetime',
        'allow_comments': 'bool',
        'has_age_gate': 'bool',
        'minimum_age': 'int',
        'rating_image_path': 'str',
        'author': 'UserGeneralUser',
        'auto_english_property_fallback': 'bool',
        'properties': 'dict(str, object)',
        'representations': 'list[ContentContentRepresentation]',
        'tags': 'list[str]',
        'comment_summary': 'ContentCommentSummary'
    }

    attribute_map = {
        'content_id': 'contentId',
        'c_type': 'cType',
        'cms_path': 'cmsPath',
        'creation_date': 'creationDate',
        'modify_date': 'modifyDate',
        'allow_comments': 'allowComments',
        'has_age_gate': 'hasAgeGate',
        'minimum_age': 'minimumAge',
        'rating_image_path': 'ratingImagePath',
        'author': 'author',
        'auto_english_property_fallback': 'autoEnglishPropertyFallback',
        'properties': 'properties',
        'representations': 'representations',
        'tags': 'tags',
        'comment_summary': 'commentSummary'
    }

    def __init__(self, content_id=None, c_type=None, cms_path=None, creation_date=None, modify_date=None, allow_comments=None, has_age_gate=None, minimum_age=None, rating_image_path=None, author=None, auto_english_property_fallback=None, properties=None, representations=None, tags=None, comment_summary=None):
        """
        ContentContentItemPublicContract - a model defined in Swagger
        """

        self._content_id = None
        self._c_type = None
        self._cms_path = None
        self._creation_date = None
        self._modify_date = None
        self._allow_comments = None
        self._has_age_gate = None
        self._minimum_age = None
        self._rating_image_path = None
        self._author = None
        self._auto_english_property_fallback = None
        self._properties = None
        self._representations = None
        self._tags = None
        self._comment_summary = None

        if content_id is not None:
          self.content_id = content_id
        if c_type is not None:
          self.c_type = c_type
        if cms_path is not None:
          self.cms_path = cms_path
        if creation_date is not None:
          self.creation_date = creation_date
        if modify_date is not None:
          self.modify_date = modify_date
        if allow_comments is not None:
          self.allow_comments = allow_comments
        if has_age_gate is not None:
          self.has_age_gate = has_age_gate
        if minimum_age is not None:
          self.minimum_age = minimum_age
        if rating_image_path is not None:
          self.rating_image_path = rating_image_path
        if author is not None:
          self.author = author
        if auto_english_property_fallback is not None:
          self.auto_english_property_fallback = auto_english_property_fallback
        if properties is not None:
          self.properties = properties
        if representations is not None:
          self.representations = representations
        if tags is not None:
          self.tags = tags
        if comment_summary is not None:
          self.comment_summary = comment_summary

    @property
    def content_id(self):
        """
        Gets the content_id of this ContentContentItemPublicContract.

        :return: The content_id of this ContentContentItemPublicContract.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """
        Sets the content_id of this ContentContentItemPublicContract.

        :param content_id: The content_id of this ContentContentItemPublicContract.
        :type: int
        """

        self._content_id = content_id

    @property
    def c_type(self):
        """
        Gets the c_type of this ContentContentItemPublicContract.

        :return: The c_type of this ContentContentItemPublicContract.
        :rtype: str
        """
        return self._c_type

    @c_type.setter
    def c_type(self, c_type):
        """
        Sets the c_type of this ContentContentItemPublicContract.

        :param c_type: The c_type of this ContentContentItemPublicContract.
        :type: str
        """

        self._c_type = c_type

    @property
    def cms_path(self):
        """
        Gets the cms_path of this ContentContentItemPublicContract.

        :return: The cms_path of this ContentContentItemPublicContract.
        :rtype: str
        """
        return self._cms_path

    @cms_path.setter
    def cms_path(self, cms_path):
        """
        Sets the cms_path of this ContentContentItemPublicContract.

        :param cms_path: The cms_path of this ContentContentItemPublicContract.
        :type: str
        """

        self._cms_path = cms_path

    @property
    def creation_date(self):
        """
        Gets the creation_date of this ContentContentItemPublicContract.

        :return: The creation_date of this ContentContentItemPublicContract.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this ContentContentItemPublicContract.

        :param creation_date: The creation_date of this ContentContentItemPublicContract.
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this ContentContentItemPublicContract.

        :return: The modify_date of this ContentContentItemPublicContract.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this ContentContentItemPublicContract.

        :param modify_date: The modify_date of this ContentContentItemPublicContract.
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def allow_comments(self):
        """
        Gets the allow_comments of this ContentContentItemPublicContract.

        :return: The allow_comments of this ContentContentItemPublicContract.
        :rtype: bool
        """
        return self._allow_comments

    @allow_comments.setter
    def allow_comments(self, allow_comments):
        """
        Sets the allow_comments of this ContentContentItemPublicContract.

        :param allow_comments: The allow_comments of this ContentContentItemPublicContract.
        :type: bool
        """

        self._allow_comments = allow_comments

    @property
    def has_age_gate(self):
        """
        Gets the has_age_gate of this ContentContentItemPublicContract.

        :return: The has_age_gate of this ContentContentItemPublicContract.
        :rtype: bool
        """
        return self._has_age_gate

    @has_age_gate.setter
    def has_age_gate(self, has_age_gate):
        """
        Sets the has_age_gate of this ContentContentItemPublicContract.

        :param has_age_gate: The has_age_gate of this ContentContentItemPublicContract.
        :type: bool
        """

        self._has_age_gate = has_age_gate

    @property
    def minimum_age(self):
        """
        Gets the minimum_age of this ContentContentItemPublicContract.

        :return: The minimum_age of this ContentContentItemPublicContract.
        :rtype: int
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, minimum_age):
        """
        Sets the minimum_age of this ContentContentItemPublicContract.

        :param minimum_age: The minimum_age of this ContentContentItemPublicContract.
        :type: int
        """

        self._minimum_age = minimum_age

    @property
    def rating_image_path(self):
        """
        Gets the rating_image_path of this ContentContentItemPublicContract.

        :return: The rating_image_path of this ContentContentItemPublicContract.
        :rtype: str
        """
        return self._rating_image_path

    @rating_image_path.setter
    def rating_image_path(self, rating_image_path):
        """
        Sets the rating_image_path of this ContentContentItemPublicContract.

        :param rating_image_path: The rating_image_path of this ContentContentItemPublicContract.
        :type: str
        """

        self._rating_image_path = rating_image_path

    @property
    def author(self):
        """
        Gets the author of this ContentContentItemPublicContract.

        :return: The author of this ContentContentItemPublicContract.
        :rtype: UserGeneralUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this ContentContentItemPublicContract.

        :param author: The author of this ContentContentItemPublicContract.
        :type: UserGeneralUser
        """

        self._author = author

    @property
    def auto_english_property_fallback(self):
        """
        Gets the auto_english_property_fallback of this ContentContentItemPublicContract.

        :return: The auto_english_property_fallback of this ContentContentItemPublicContract.
        :rtype: bool
        """
        return self._auto_english_property_fallback

    @auto_english_property_fallback.setter
    def auto_english_property_fallback(self, auto_english_property_fallback):
        """
        Sets the auto_english_property_fallback of this ContentContentItemPublicContract.

        :param auto_english_property_fallback: The auto_english_property_fallback of this ContentContentItemPublicContract.
        :type: bool
        """

        self._auto_english_property_fallback = auto_english_property_fallback

    @property
    def properties(self):
        """
        Gets the properties of this ContentContentItemPublicContract.
        Firehose content is really a collection of metadata and \"properties\", which are  the potentially-but-not-strictly localizable data that comprises the meat of  whatever content is being shown.    As Cole Porter would have crooned, \"Anything Goes\" with Firehose properties.  They are most often strings, but they can theoretically be anything.  They are JSON  encoded, and could be JSON structures, simple strings, numbers etc...  The Content Type  of the item (cType) will describe the properties, and thus how they ought to be deserialized.

        :return: The properties of this ContentContentItemPublicContract.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ContentContentItemPublicContract.
        Firehose content is really a collection of metadata and \"properties\", which are  the potentially-but-not-strictly localizable data that comprises the meat of  whatever content is being shown.    As Cole Porter would have crooned, \"Anything Goes\" with Firehose properties.  They are most often strings, but they can theoretically be anything.  They are JSON  encoded, and could be JSON structures, simple strings, numbers etc...  The Content Type  of the item (cType) will describe the properties, and thus how they ought to be deserialized.

        :param properties: The properties of this ContentContentItemPublicContract.
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def representations(self):
        """
        Gets the representations of this ContentContentItemPublicContract.

        :return: The representations of this ContentContentItemPublicContract.
        :rtype: list[ContentContentRepresentation]
        """
        return self._representations

    @representations.setter
    def representations(self, representations):
        """
        Sets the representations of this ContentContentItemPublicContract.

        :param representations: The representations of this ContentContentItemPublicContract.
        :type: list[ContentContentRepresentation]
        """

        self._representations = representations

    @property
    def tags(self):
        """
        Gets the tags of this ContentContentItemPublicContract.

        :return: The tags of this ContentContentItemPublicContract.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ContentContentItemPublicContract.

        :param tags: The tags of this ContentContentItemPublicContract.
        :type: list[str]
        """

        self._tags = tags

    @property
    def comment_summary(self):
        """
        Gets the comment_summary of this ContentContentItemPublicContract.

        :return: The comment_summary of this ContentContentItemPublicContract.
        :rtype: ContentCommentSummary
        """
        return self._comment_summary

    @comment_summary.setter
    def comment_summary(self, comment_summary):
        """
        Sets the comment_summary of this ContentContentItemPublicContract.

        :param comment_summary: The comment_summary of this ContentContentItemPublicContract.
        :type: ContentCommentSummary
        """

        self._comment_summary = comment_summary

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
        if not isinstance(other, ContentContentItemPublicContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
