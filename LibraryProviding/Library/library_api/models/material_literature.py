# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from library_api.models.base_model_ import Model
from library_api import util


class MaterialLiterature(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, number_literature: int=None):  # noqa: E501
        """MaterialLiterature - a model defined in Swagger

        :param number_literature: The number_literature of this MaterialLiterature.  # noqa: E501
        :type number_literature: int
        """
        self.swagger_types = {
            'number_literature': int
        }

        self.attribute_map = {
            'number_literature': 'number_liter'
        }

        self._number_literature = number_literature

    @classmethod
    def from_dict(cls, dikt) -> 'MaterialLiterature':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MaterialLiterature of this MaterialLiterature.  # noqa: E501
        :rtype: MaterialLiterature
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_literature(self) -> int:
        """Gets the number_literature of this MaterialLiterature.


        :return: The number_literature of this MaterialLiterature.
        :rtype: int
        """
        return self._number_literature

    @number_literature.setter
    def number_literature(self, number_literature: int):
        """Sets the number_literature of this MaterialLiterature.


        :param number_literature: The number_literature of this MaterialLiterature.
        :type number_literature: int
        """

        self._number_literature = number_literature
