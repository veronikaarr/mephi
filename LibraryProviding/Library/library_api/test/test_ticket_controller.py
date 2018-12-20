# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from library_api.models.ticket import Ticket  # noqa: E501
from library_api.test import BaseTestCase


class TestTicketController(BaseTestCase):
    """TicketController integration test stubs"""

    def test_deleter_ticket(self):
        """Test case for deleter_ticket

        User case \"Удаление анкеты\"
        """
        response = self.client.open(
            '/v2/ticket/{ticket_id}'.format(ticket_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ticket(self):
        """Test case for get_ticket

        BPMN 4
        """
        response = self.client.open(
            '/v2/ticket/{ticket_id}'.format(ticket_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_ticket(self):
        """Test case for put_ticket

        User case \"Редактирование анкеты\"
        """
        data = dict(firstName='firstName_example',
                    lastName='lastName_example',
                    email='email_example')
        response = self.client.open(
            '/v2/ticket/{ticket_id}'.format(ticket_id=56),
            method='PUT',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
