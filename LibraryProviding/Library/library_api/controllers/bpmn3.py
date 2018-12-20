from library_api.controllers.reader_controller import get_reader
from library_api.controllers.reader_controller import post_reader
from library_api.controllers.ticket_controller import get_ticket
from datetime import date
from library_api.controllers.order_book_controller import add_order_book
from library_api.controllers.tasks_controller import add_task
from library_api.controllers.utils.user_interface import *
from library_api.controllers.utils.sql_request import sql_get_ticket_bpmn3, sql_get_bpmn3_all


def bmpn3():
    ticket_id, literature_id = user_get_bpmn3()
    return_ticket = get_ticket(ticket_id)
    if return_ticket is None:
        raise ValueError("Ticket not exist")
    return_sql = sql_get_ticket_bpmn3(return_ticket, literature_id)
    if return_sql is not None:
            return_sql.status = 0
            return 200
    else:
        ticket_reader = sql_get_bpmn3_all()
        if ticket_reader is not None:
            raise ValueError("The book is {} reader".format(ticket_reader.reader))
        else:
            raise ValueError("The book not from this library")
