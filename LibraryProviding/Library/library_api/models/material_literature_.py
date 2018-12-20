# coding: utf-8

from __future__ import absolute_import


class MaterialLiterature():
    def __init__(self, number_literature: int=None):  # noqa: E501
        self._number_literature = number_literature

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
