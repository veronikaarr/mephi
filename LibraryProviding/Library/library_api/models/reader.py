# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from library_api.models.base_model_ import Model
from library_api import util

import re


class Reader(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, patronymic: str=None, pasport_id: str=None, pasport_series: str=None, phone_number: str=None, email: str=None):  # noqa: E501
        """Reader - a model defined in Swagger

        :param id: The id of this Reader.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this Reader.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Reader.  # noqa: E501
        :type last_name: str
        :param patronymic: The patronymic of this Reader.  # noqa: E501
        :type patronymic: str
        :param pasport_id: The pasport_id of this Reader.  # noqa: E501
        :type pasport_id: str
        :param pasport_series: The pasport_series of this Reader.  # noqa: E501
        :type pasport_series: str
        :param phone_number: The phone_number of this Reader.  # noqa: E501
        :type phone_number: str
        :param email: The email of this Reader.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'patronymic': str,
            'pasport_id': str,
            'pasport_series': str,
            'phone_number': str,
            'email': str
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'patronymic': 'patronymic',
            'pasport_id': 'pasport_id',
            'pasport_series': 'pasport_series',
            'phone_number': 'phone_number',
            'email': 'email'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._patronymic = patronymic
        self._pasport_id = pasport_id
        self._pasport_series = pasport_series
        self._phone_number = phone_number
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'Reader':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Reader of this Reader.  # noqa: E501
        :rtype: Reader
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Reader.


        :return: The id of this Reader.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Reader.


        :param id: The id of this Reader.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Reader.


        :return: The first_name of this Reader.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Reader.


        :param first_name: The first_name of this Reader.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Reader.


        :return: The last_name of this Reader.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Reader.


        :param last_name: The last_name of this Reader.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def patronymic(self) -> str:
        """Gets the patronymic of this Reader.


        :return: The patronymic of this Reader.
        :rtype: str
        """
        return self._patronymic

    @patronymic.setter
    def patronymic(self, patronymic: str):
        """Sets the patronymic of this Reader.


        :param patronymic: The patronymic of this Reader.
        :type patronymic: str
        """

        self._patronymic = patronymic

    @property
    def pasport_id(self) -> str:
        """Gets the pasport_id of this Reader.


        :return: The pasport_id of this Reader.
        :rtype: str
        """
        return self._pasport_id

    @pasport_id.setter
    def pasport_id(self, pasport_id: str):
        """Sets the pasport_id of this Reader.


        :param pasport_id: The pasport_id of this Reader.
        :type pasport_id: str
        """

        self._pasport_id = pasport_id

    @property
    def pasport_series(self) -> str:
        """Gets the pasport_series of this Reader.


        :return: The pasport_series of this Reader.
        :rtype: str
        """
        return self._pasport_series

    @pasport_series.setter
    def pasport_series(self, pasport_series: str):
        """Sets the pasport_series of this Reader.


        :param pasport_series: The pasport_series of this Reader.
        :type pasport_series: str
        """

        self._pasport_series = pasport_series

    @property
    def phone_number(self) -> str:
        """Gets the phone_number of this Reader.


        :return: The phone_number of this Reader.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """Sets the phone_number of this Reader.


        :param phone_number: The phone_number of this Reader.
        :type phone_number: str
        """
        if phone_number is not None and not re.search('^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$', phone_number):  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must be a follow pattern or equal to `/^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$/`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def email(self) -> str:
        """Gets the email of this Reader.


        :return: The email of this Reader.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Reader.


        :param email: The email of this Reader.
        :type email: str
        """
        if email is not None and not re.search('^.*@.*\\..*$', email):  # noqa: E501
            raise ValueError("Invalid value for `email`, must be a follow pattern or equal to `/^.*@.*\\..*$/`")  # noqa: E501

        self._email = email