# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.1.1
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.partnerships_partnership_type import PartnershipsPartnershipType  # noqa: F401,E501
from swagger_client.models.user_user_info_card import UserUserInfoCard  # noqa: F401,E501


class CommunityCommunityLiveStatus(object):
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
        'date_status_updated': 'datetime',
        'url': 'str',
        'partnership_identifier': 'str',
        'partnership_type': 'PartnershipsPartnershipType',
        'thumbnail': 'str',
        'thumbnail_small': 'str',
        'thumbnail_large': 'str',
        'destiny_character_id': 'int',
        'user_info': 'UserUserInfoCard',
        'current_activity_hash': 'int',
        'date_last_played': 'datetime',
        'date_stream_started': 'datetime',
        'locale': 'str',
        'current_viewers': 'int',
        'followers': 'int',
        'overall_viewers': 'int',
        'is_featured': 'bool',
        'title': 'str',
        'activity_mode_hash': 'int',
        'date_featured': 'datetime',
        'trending_value': 'float',
        'is_subscribable': 'bool'
    }

    attribute_map = {
        'date_status_updated': 'dateStatusUpdated',
        'url': 'url',
        'partnership_identifier': 'partnershipIdentifier',
        'partnership_type': 'partnershipType',
        'thumbnail': 'thumbnail',
        'thumbnail_small': 'thumbnailSmall',
        'thumbnail_large': 'thumbnailLarge',
        'destiny_character_id': 'destinyCharacterId',
        'user_info': 'userInfo',
        'current_activity_hash': 'currentActivityHash',
        'date_last_played': 'dateLastPlayed',
        'date_stream_started': 'dateStreamStarted',
        'locale': 'locale',
        'current_viewers': 'currentViewers',
        'followers': 'followers',
        'overall_viewers': 'overallViewers',
        'is_featured': 'isFeatured',
        'title': 'title',
        'activity_mode_hash': 'activityModeHash',
        'date_featured': 'dateFeatured',
        'trending_value': 'trendingValue',
        'is_subscribable': 'isSubscribable'
    }

    def __init__(self, date_status_updated=None, url=None, partnership_identifier=None, partnership_type=None, thumbnail=None, thumbnail_small=None, thumbnail_large=None, destiny_character_id=None, user_info=None, current_activity_hash=None, date_last_played=None, date_stream_started=None, locale=None, current_viewers=None, followers=None, overall_viewers=None, is_featured=None, title=None, activity_mode_hash=None, date_featured=None, trending_value=None, is_subscribable=None):  # noqa: E501
        """CommunityCommunityLiveStatus - a model defined in Swagger"""  # noqa: E501

        self._date_status_updated = None
        self._url = None
        self._partnership_identifier = None
        self._partnership_type = None
        self._thumbnail = None
        self._thumbnail_small = None
        self._thumbnail_large = None
        self._destiny_character_id = None
        self._user_info = None
        self._current_activity_hash = None
        self._date_last_played = None
        self._date_stream_started = None
        self._locale = None
        self._current_viewers = None
        self._followers = None
        self._overall_viewers = None
        self._is_featured = None
        self._title = None
        self._activity_mode_hash = None
        self._date_featured = None
        self._trending_value = None
        self._is_subscribable = None
        self.discriminator = None

        if date_status_updated is not None:
            self.date_status_updated = date_status_updated
        if url is not None:
            self.url = url
        if partnership_identifier is not None:
            self.partnership_identifier = partnership_identifier
        if partnership_type is not None:
            self.partnership_type = partnership_type
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if thumbnail_small is not None:
            self.thumbnail_small = thumbnail_small
        if thumbnail_large is not None:
            self.thumbnail_large = thumbnail_large
        if destiny_character_id is not None:
            self.destiny_character_id = destiny_character_id
        if user_info is not None:
            self.user_info = user_info
        if current_activity_hash is not None:
            self.current_activity_hash = current_activity_hash
        if date_last_played is not None:
            self.date_last_played = date_last_played
        if date_stream_started is not None:
            self.date_stream_started = date_stream_started
        if locale is not None:
            self.locale = locale
        if current_viewers is not None:
            self.current_viewers = current_viewers
        if followers is not None:
            self.followers = followers
        if overall_viewers is not None:
            self.overall_viewers = overall_viewers
        if is_featured is not None:
            self.is_featured = is_featured
        if title is not None:
            self.title = title
        if activity_mode_hash is not None:
            self.activity_mode_hash = activity_mode_hash
        if date_featured is not None:
            self.date_featured = date_featured
        if trending_value is not None:
            self.trending_value = trending_value
        if is_subscribable is not None:
            self.is_subscribable = is_subscribable

    @property
    def date_status_updated(self):
        """Gets the date_status_updated of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The date_status_updated of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._date_status_updated

    @date_status_updated.setter
    def date_status_updated(self, date_status_updated):
        """Sets the date_status_updated of this CommunityCommunityLiveStatus.


        :param date_status_updated: The date_status_updated of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: datetime
        """

        self._date_status_updated = date_status_updated

    @property
    def url(self):
        """Gets the url of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The url of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CommunityCommunityLiveStatus.


        :param url: The url of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def partnership_identifier(self):
        """Gets the partnership_identifier of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The partnership_identifier of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._partnership_identifier

    @partnership_identifier.setter
    def partnership_identifier(self, partnership_identifier):
        """Sets the partnership_identifier of this CommunityCommunityLiveStatus.


        :param partnership_identifier: The partnership_identifier of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._partnership_identifier = partnership_identifier

    @property
    def partnership_type(self):
        """Gets the partnership_type of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The partnership_type of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: PartnershipsPartnershipType
        """
        return self._partnership_type

    @partnership_type.setter
    def partnership_type(self, partnership_type):
        """Sets the partnership_type of this CommunityCommunityLiveStatus.


        :param partnership_type: The partnership_type of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: PartnershipsPartnershipType
        """

        self._partnership_type = partnership_type

    @property
    def thumbnail(self):
        """Gets the thumbnail of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The thumbnail of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this CommunityCommunityLiveStatus.


        :param thumbnail: The thumbnail of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def thumbnail_small(self):
        """Gets the thumbnail_small of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The thumbnail_small of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_small

    @thumbnail_small.setter
    def thumbnail_small(self, thumbnail_small):
        """Sets the thumbnail_small of this CommunityCommunityLiveStatus.


        :param thumbnail_small: The thumbnail_small of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._thumbnail_small = thumbnail_small

    @property
    def thumbnail_large(self):
        """Gets the thumbnail_large of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The thumbnail_large of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_large

    @thumbnail_large.setter
    def thumbnail_large(self, thumbnail_large):
        """Sets the thumbnail_large of this CommunityCommunityLiveStatus.


        :param thumbnail_large: The thumbnail_large of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._thumbnail_large = thumbnail_large

    @property
    def destiny_character_id(self):
        """Gets the destiny_character_id of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The destiny_character_id of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._destiny_character_id

    @destiny_character_id.setter
    def destiny_character_id(self, destiny_character_id):
        """Sets the destiny_character_id of this CommunityCommunityLiveStatus.


        :param destiny_character_id: The destiny_character_id of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._destiny_character_id = destiny_character_id

    @property
    def user_info(self):
        """Gets the user_info of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The user_info of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: UserUserInfoCard
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this CommunityCommunityLiveStatus.


        :param user_info: The user_info of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: UserUserInfoCard
        """

        self._user_info = user_info

    @property
    def current_activity_hash(self):
        """Gets the current_activity_hash of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The current_activity_hash of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_activity_hash

    @current_activity_hash.setter
    def current_activity_hash(self, current_activity_hash):
        """Sets the current_activity_hash of this CommunityCommunityLiveStatus.


        :param current_activity_hash: The current_activity_hash of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._current_activity_hash = current_activity_hash

    @property
    def date_last_played(self):
        """Gets the date_last_played of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The date_last_played of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_played

    @date_last_played.setter
    def date_last_played(self, date_last_played):
        """Sets the date_last_played of this CommunityCommunityLiveStatus.


        :param date_last_played: The date_last_played of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: datetime
        """

        self._date_last_played = date_last_played

    @property
    def date_stream_started(self):
        """Gets the date_stream_started of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The date_stream_started of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._date_stream_started

    @date_stream_started.setter
    def date_stream_started(self, date_stream_started):
        """Sets the date_stream_started of this CommunityCommunityLiveStatus.


        :param date_stream_started: The date_stream_started of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: datetime
        """

        self._date_stream_started = date_stream_started

    @property
    def locale(self):
        """Gets the locale of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The locale of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CommunityCommunityLiveStatus.


        :param locale: The locale of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def current_viewers(self):
        """Gets the current_viewers of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The current_viewers of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_viewers

    @current_viewers.setter
    def current_viewers(self, current_viewers):
        """Sets the current_viewers of this CommunityCommunityLiveStatus.


        :param current_viewers: The current_viewers of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._current_viewers = current_viewers

    @property
    def followers(self):
        """Gets the followers of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The followers of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this CommunityCommunityLiveStatus.


        :param followers: The followers of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._followers = followers

    @property
    def overall_viewers(self):
        """Gets the overall_viewers of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The overall_viewers of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._overall_viewers

    @overall_viewers.setter
    def overall_viewers(self, overall_viewers):
        """Sets the overall_viewers of this CommunityCommunityLiveStatus.


        :param overall_viewers: The overall_viewers of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._overall_viewers = overall_viewers

    @property
    def is_featured(self):
        """Gets the is_featured of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The is_featured of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """Sets the is_featured of this CommunityCommunityLiveStatus.


        :param is_featured: The is_featured of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: bool
        """

        self._is_featured = is_featured

    @property
    def title(self):
        """Gets the title of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The title of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CommunityCommunityLiveStatus.


        :param title: The title of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def activity_mode_hash(self):
        """Gets the activity_mode_hash of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The activity_mode_hash of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: int
        """
        return self._activity_mode_hash

    @activity_mode_hash.setter
    def activity_mode_hash(self, activity_mode_hash):
        """Sets the activity_mode_hash of this CommunityCommunityLiveStatus.


        :param activity_mode_hash: The activity_mode_hash of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: int
        """

        self._activity_mode_hash = activity_mode_hash

    @property
    def date_featured(self):
        """Gets the date_featured of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The date_featured of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._date_featured

    @date_featured.setter
    def date_featured(self, date_featured):
        """Sets the date_featured of this CommunityCommunityLiveStatus.


        :param date_featured: The date_featured of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: datetime
        """

        self._date_featured = date_featured

    @property
    def trending_value(self):
        """Gets the trending_value of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The trending_value of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: float
        """
        return self._trending_value

    @trending_value.setter
    def trending_value(self, trending_value):
        """Sets the trending_value of this CommunityCommunityLiveStatus.


        :param trending_value: The trending_value of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: float
        """

        self._trending_value = trending_value

    @property
    def is_subscribable(self):
        """Gets the is_subscribable of this CommunityCommunityLiveStatus.  # noqa: E501


        :return: The is_subscribable of this CommunityCommunityLiveStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribable

    @is_subscribable.setter
    def is_subscribable(self, is_subscribable):
        """Sets the is_subscribable of this CommunityCommunityLiveStatus.


        :param is_subscribable: The is_subscribable of this CommunityCommunityLiveStatus.  # noqa: E501
        :type: bool
        """

        self._is_subscribable = is_subscribable

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommunityCommunityLiveStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
