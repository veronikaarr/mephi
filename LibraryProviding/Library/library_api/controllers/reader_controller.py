import connexion
import six

from library_api.models.ticket import Ticket  # noqa: E501
from library_api.models.reader import Reader
from library_api import util
from datetime import date
from library_api.controllers.utils.sql_request import sql_select_reader, sql_insert_database


def get_reader(lastName=None, phone_number=None):  # noqa: E501
    """BPMN 1 step 1

    Find reader with form data # noqa: E501

    :rtype: Reader
    """
    new_reader = sql_select_reader(lastName, phone_number)
    return new_reader


def post_reader(body=None, data=None):  # noqa: E501
    """BPMN 1 step 2

    Registration reader with form data # noqa: E501

    :param body: Reader
    :type body: dict | bytes

    :rtype: Ticket
    """
    # if connexion.request.is_json and body is None:
    #     body = Reader.from_dict(connexion.request.get_json())  # noqa: E501
    ticket_prepare = Ticket(date_of_registration=date.today(), reader=data)
    ticket = sql_insert_database(ticket_prepare)
    return ticket
