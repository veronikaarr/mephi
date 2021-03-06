# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from library_api.models.base_model_ import Model
import re  # noqa: F401,E501
from library_api import util


class ElectronicLiterature(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, electronic_address: str=None):  # noqa: E501
        """ElectronicLiterature - a model defined in Swagger

        :param electronic_address: The electronic_address of this ElectronicLiterature.  # noqa: E501
        :type electronic_address: str
        """
        self.swagger_types = {
            'electronic_address': str
        }

        self.attribute_map = {
            'electronic_address': 'electronic_address'
        }

        self._electronic_address = electronic_address

    @classmethod
    def from_dict(cls, dikt) -> 'ElectronicLiterature':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ElectronicLiterature of this ElectronicLiterature.  # noqa: E501
        :rtype: ElectronicLiterature
        """
        return util.deserialize_model(dikt, cls)

    @property
    def electronic_address(self) -> str:
        """Gets the electronic_address of this ElectronicLiterature.


        :return: The electronic_address of this ElectronicLiterature.
        :rtype: str
        """
        return self._electronic_address

    @electronic_address.setter
    def electronic_address(self, electronic_address: str):
        """Sets the electronic_address of this ElectronicLiterature.


        :param electronic_address: The electronic_address of this ElectronicLiterature.
        :type electronic_address: str
        """
        if electronic_address is not None and not re.search('.*\..*', electronic_address):  # noqa: E501
            raise ValueError("Invalid value for `electronic_address`, must be a follow pattern or equal to `/.*\\..*/`")  # noqa: E501

        self._electronic_address = electronic_address
