# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from library_api.models.tasks import Tasks  # noqa: E501
from library_api.test import BaseTestCase


class TestTasksController(BaseTestCase):
    """TasksController integration test stubs"""

    def test_add_task(self):
        """Test case for add_task

        BPMN 2 step 1
        """
        response = self.client.open(
            '/v2/tasks/{ticket_id}'.format(ticket_id=56),
            method='POST',
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tasks(self):
        """Test case for get_tasks

        BPMN 2 step 3
        """
        response = self.client.open(
            '/v2/tasks/{ticket_id}'.format(ticket_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
