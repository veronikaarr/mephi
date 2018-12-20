import connexion
import six

from library_api.models.order_book import OrderBook  # noqa: E501
from library_api import util
from library_api.controllers.utils.sql_request import sql_select_literature_bpmn2


def add_order_book(literature_id=None):  # noqa: E501
    """BPMN 2 step 2

    Add order book in task # noqa: E501

    :param task_id: Reader that need book
    :type task_id: int
    :param firstName: Update first name of Reader
    :type firstName: str

    :rtype: OrderBook
    """
    i = sql_select_literature_bpmn2(literature_id)
    if i == 0:
        return ValueError("Literature not exist (number)")
    if i is None:
        return ValueError("Literature not exist")
    order_book = OrderBook(id_literature=i)
    order_book.status = 1
    return order_book


def deleter_order_book(id_literature):  # noqa: E501
    """BPMN 3

    Delete order book from task # noqa: E501

    :param id_literature: Delete order book
    :type id_literature: int

    :rtype: None
    """
    return 'do some magic!'
