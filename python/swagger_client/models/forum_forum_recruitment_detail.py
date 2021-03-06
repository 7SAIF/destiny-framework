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

from swagger_client.models.forum_forum_recruitment_intensity_label import ForumForumRecruitmentIntensityLabel  # noqa: F401,E501
from swagger_client.models.forum_forum_recruitment_tone_label import ForumForumRecruitmentToneLabel  # noqa: F401,E501
from swagger_client.models.user_general_user import UserGeneralUser  # noqa: F401,E501


class ForumForumRecruitmentDetail(object):
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
        'topic_id': 'int',
        'microphone_required': 'bool',
        'intensity': 'ForumForumRecruitmentIntensityLabel',
        'tone': 'ForumForumRecruitmentToneLabel',
        'approved': 'bool',
        'conversation_id': 'int',
        'player_slots_total': 'int',
        'player_slots_remaining': 'int',
        'fireteam': 'list[UserGeneralUser]',
        'kicked_player_ids': 'list[int]'
    }

    attribute_map = {
        'topic_id': 'topicId',
        'microphone_required': 'microphoneRequired',
        'intensity': 'intensity',
        'tone': 'tone',
        'approved': 'approved',
        'conversation_id': 'conversationId',
        'player_slots_total': 'playerSlotsTotal',
        'player_slots_remaining': 'playerSlotsRemaining',
        'fireteam': 'Fireteam',
        'kicked_player_ids': 'kickedPlayerIds'
    }

    def __init__(self, topic_id=None, microphone_required=None, intensity=None, tone=None, approved=None, conversation_id=None, player_slots_total=None, player_slots_remaining=None, fireteam=None, kicked_player_ids=None):  # noqa: E501
        """ForumForumRecruitmentDetail - a model defined in Swagger"""  # noqa: E501

        self._topic_id = None
        self._microphone_required = None
        self._intensity = None
        self._tone = None
        self._approved = None
        self._conversation_id = None
        self._player_slots_total = None
        self._player_slots_remaining = None
        self._fireteam = None
        self._kicked_player_ids = None
        self.discriminator = None

        if topic_id is not None:
            self.topic_id = topic_id
        if microphone_required is not None:
            self.microphone_required = microphone_required
        if intensity is not None:
            self.intensity = intensity
        if tone is not None:
            self.tone = tone
        if approved is not None:
            self.approved = approved
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if player_slots_total is not None:
            self.player_slots_total = player_slots_total
        if player_slots_remaining is not None:
            self.player_slots_remaining = player_slots_remaining
        if fireteam is not None:
            self.fireteam = fireteam
        if kicked_player_ids is not None:
            self.kicked_player_ids = kicked_player_ids

    @property
    def topic_id(self):
        """Gets the topic_id of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The topic_id of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: int
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this ForumForumRecruitmentDetail.


        :param topic_id: The topic_id of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: int
        """

        self._topic_id = topic_id

    @property
    def microphone_required(self):
        """Gets the microphone_required of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The microphone_required of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: bool
        """
        return self._microphone_required

    @microphone_required.setter
    def microphone_required(self, microphone_required):
        """Sets the microphone_required of this ForumForumRecruitmentDetail.


        :param microphone_required: The microphone_required of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: bool
        """

        self._microphone_required = microphone_required

    @property
    def intensity(self):
        """Gets the intensity of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The intensity of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: ForumForumRecruitmentIntensityLabel
        """
        return self._intensity

    @intensity.setter
    def intensity(self, intensity):
        """Sets the intensity of this ForumForumRecruitmentDetail.


        :param intensity: The intensity of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: ForumForumRecruitmentIntensityLabel
        """

        self._intensity = intensity

    @property
    def tone(self):
        """Gets the tone of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The tone of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: ForumForumRecruitmentToneLabel
        """
        return self._tone

    @tone.setter
    def tone(self, tone):
        """Sets the tone of this ForumForumRecruitmentDetail.


        :param tone: The tone of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: ForumForumRecruitmentToneLabel
        """

        self._tone = tone

    @property
    def approved(self):
        """Gets the approved of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The approved of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this ForumForumRecruitmentDetail.


        :param approved: The approved of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def conversation_id(self):
        """Gets the conversation_id of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The conversation_id of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: int
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this ForumForumRecruitmentDetail.


        :param conversation_id: The conversation_id of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: int
        """

        self._conversation_id = conversation_id

    @property
    def player_slots_total(self):
        """Gets the player_slots_total of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The player_slots_total of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: int
        """
        return self._player_slots_total

    @player_slots_total.setter
    def player_slots_total(self, player_slots_total):
        """Sets the player_slots_total of this ForumForumRecruitmentDetail.


        :param player_slots_total: The player_slots_total of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: int
        """

        self._player_slots_total = player_slots_total

    @property
    def player_slots_remaining(self):
        """Gets the player_slots_remaining of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The player_slots_remaining of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: int
        """
        return self._player_slots_remaining

    @player_slots_remaining.setter
    def player_slots_remaining(self, player_slots_remaining):
        """Sets the player_slots_remaining of this ForumForumRecruitmentDetail.


        :param player_slots_remaining: The player_slots_remaining of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: int
        """

        self._player_slots_remaining = player_slots_remaining

    @property
    def fireteam(self):
        """Gets the fireteam of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The fireteam of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: list[UserGeneralUser]
        """
        return self._fireteam

    @fireteam.setter
    def fireteam(self, fireteam):
        """Sets the fireteam of this ForumForumRecruitmentDetail.


        :param fireteam: The fireteam of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: list[UserGeneralUser]
        """

        self._fireteam = fireteam

    @property
    def kicked_player_ids(self):
        """Gets the kicked_player_ids of this ForumForumRecruitmentDetail.  # noqa: E501


        :return: The kicked_player_ids of this ForumForumRecruitmentDetail.  # noqa: E501
        :rtype: list[int]
        """
        return self._kicked_player_ids

    @kicked_player_ids.setter
    def kicked_player_ids(self, kicked_player_ids):
        """Sets the kicked_player_ids of this ForumForumRecruitmentDetail.


        :param kicked_player_ids: The kicked_player_ids of this ForumForumRecruitmentDetail.  # noqa: E501
        :type: list[int]
        """

        self._kicked_player_ids = kicked_player_ids

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
        if not isinstance(other, ForumForumRecruitmentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
