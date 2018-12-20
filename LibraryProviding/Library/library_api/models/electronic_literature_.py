# coding: utf-8

from __future__ import absolute_import
import re  # noqa: F401,E501


class ElectronicLiterature():
    def __init__(self, electronic_address: str=None):  # noqa: E501

        self._electronic_address = electronic_address

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
