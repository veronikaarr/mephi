# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from library_api.models.order_book import OrderBook  # noqa: E501
from library_api.test import BaseTestCase


class TestOrderBookController(BaseTestCase):
    """OrderBookController integration test stubs"""

    def test_add_order_book(self):
        """Test case for add_order_book

        BPMN 2 step 2
        """
        data = dict(firstName='firstName_example')
        response = self.client.open(
            '/v2/orderBook/{task_id}'.format(task_id=56),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleter_order_book(self):
        """Test case for deleter_order_book

        BPMN 3
        """
        response = self.client.open(
            '/v2/orderBook/delete/{id_literature}'.format(id_literature=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
