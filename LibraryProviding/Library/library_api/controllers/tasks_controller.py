import connexion
import six

from library_api.models.tasks import Tasks  # noqa: E501
from library_api import util
import datetime


def add_task(order_book_es):  # noqa: E501
    """BPMN 2 step 1

    Creating a new task for the issuance of literature # noqa: E501

    :param ticket_id: Reader that need book
    :type ticket_id: int

    :rtype: Tasks
    """
    tasks = Tasks()
    tasks.order_book_list = []
    tasks.order_book_list.append(order_book_es)
    tasks.registration_date = datetime.date.today()
    return tasks

def get_tasks(ticket_id):  # noqa: E501
    """BPMN 2 step 3

    Get task for providing the reader with all the literature # noqa: E501

    :param ticket_id: Number of ticket
    :type ticket_id: int

    :rtype: Tasks
    """
    return 'do some magic!'
