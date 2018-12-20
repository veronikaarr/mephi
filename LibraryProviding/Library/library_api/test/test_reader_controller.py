# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from library_api.models.ticket import Ticket  # noqa: E501
from library_api.test import BaseTestCase


class TestReaderController(BaseTestCase):
    """ReaderController integration test stubs"""

    def test_post_reader(self):
        """Test case for post_reader

        BPMN 1
        """
        data = dict(firstName='firstName_example',
                    lastName='lastName_example',
                    email='email_example')
        response = self.client.open(
            '/v2/reader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
