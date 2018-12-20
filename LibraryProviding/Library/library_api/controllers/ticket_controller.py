import connexion
import six

from library_api.models.ticket import Ticket  # noqa: E501
from library_api import util
from library_api.controllers.utils.sql_request import sql_select_ticket


def deleter_ticket(ticket_id):  # noqa: E501
    """User case \&quot;Удаление анкеты\&quot;

    Delete reader ticket # noqa: E501

    :param ticket_id: Delete reader and his ticket
    :type ticket_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_ticket(ticket_id):  # noqa: E501
    """BPMN 4

    Get reader ticket with message of debt for sending message # noqa: E501

    :param ticket_id: Delete reader and his ticket
    :type ticket_id: int

    :rtype: Ticket
    """
    'функция в БД - в заглушку'
    res = sql_select_ticket(ticket_id)
    return res


def put_ticket(ticket_id, firstName=None, lastName=None, email=None):  # noqa: E501
    """User case \&quot;Редактирование анкеты\&quot;

    Update reader ticket with form data # noqa: E501

    :param ticket_id: Reader that need to be update
    :type ticket_id: int
    :param firstName: Update first name of Reader
    :type firstName: str
    :param lastName: Update last name of Reader
    :type lastName: str
    :param email: Update email of Reader
    :type email: str

    :rtype: None
    """
    return 'do some magic!'
